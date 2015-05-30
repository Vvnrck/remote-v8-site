import datetime

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from . import forms, utils, models


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'form': forms.NewTask(),
            'log_in_form': forms.SignInForm(),
            'register_form': forms.RegisterForm()
        })
        if self.request.user.is_authenticated():
            context['tasks'] = models.Task.get_customer_tasks(self.request.user)
            context['balance'] = models.Task.get_user_balance(self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = forms.NewTask(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated():
            script = request.FILES['script']
            csv_data = request.FILES['csv_data']
            self.save_files_to_database(script, csv_data, user=request.user)
        return HttpResponseRedirect(reverse('home'))

    @staticmethod
    def save_files_to_database(script, csv_data, user=None):
        name = utils.get_random_string(10)
        task, created = models.Task.objects.get_or_create(
            customer=user,
            script=script, csv_data=csv_data,
            task_name=name, computed=False,
            create_date=datetime.datetime.now()
        )
        if created:
            task.save()
        return name


class TaskView(TemplateView):
    template_name = 'task.html'


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, 'Welcome, {}.'.format(user.username))
        else:
            messages.error(request, 'This account has been disabled.')
    else:
        messages.error(request, 'Login or password is invalid.')
    return HttpResponseRedirect(reverse('home'))


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register_customer(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
        user = User.objects.create_user(username, password=password)
    else:
        messages.error(request, 'Passwords do not match.')
    return HttpResponseRedirect(reverse('home'))


def send_script_to_customer(request):
    task_name = request.GET['task_name']
    task = models.Task.objects.get(task_name=task_name, customer=request.user)
    response = HttpResponse(task.script_file, content_type='application/javascript')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(task.script)
    return response


def send_data_to_customer(request):
    task_name = request.GET['task_name']
    task = models.Task.objects.get(task_name=task_name, customer=request.user)
    response = HttpResponse(task.csv_data_file, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(task.csv_data)
    return response


def send_result_to_customer(request):
    task_name = request.GET['task_name']
    task = models.Task.objects.get(task_name=task_name, customer=request.user)
    response = HttpResponse(task.result_file, content_type='text/txt')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(task.result)
    return response


def register_worker(request):
    worker_id = request.GET['worker_id']
    worker, _ = models.Worker.objects.get_or_create(worker_id=worker_id)
    worker.save()
    return HttpResponse(content='')


def assign_task_to_worker(request):
    """ Assigns a task to offline worker.
    :param request: serves url like getTask?worker_id=...
    :return: task assignment id
    """
    worker = models.Worker.get_worker(request.GET['worker_id'])
    if worker.benchmark_result is not None:
        assignment = models.TaskAssignment.assign_latest_task(worker)
    else:
        assignment = models.TaskAssignment.assign_benchmark_task(worker)
    return HttpResponse(content=str(assignment.id))


def get_task_script(request):
    """ Returns a file with a script to offline worker.
    :param request: serves url like getScript?task_assignment_id=...
    :return: task script file
    """
    task_assignment_id = request.GET.get('task_assignment_id')
    if task_assignment_id is not None:
        assignment = models.TaskAssignment.objects.filter(id=task_assignment_id).first()
        response = HttpResponse(assignment.task.script_file, content_type='application/javascript')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(assignment.task.script)
        response['X-File-Name'] = str(assignment.task.script)
        return response
    return HttpResponseServerError()


def get_task_data(request):
    """ Returns a file with data to offline worker.
    :param request: serves url like getData?task_assignment_id=...
    :return: task data file
    """
    task_assignment_id = request.GET.get('task_assignment_id')
    if task_assignment_id is not None:
        assignment = models.TaskAssignment.objects.filter(id=task_assignment_id).first()
        response = HttpResponse(assignment.task.csv_data_file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(assignment.task.csv_data)
        response['X-File-Name'] = str(assignment.task.csv_data)
        return response
    return HttpResponseServerError()


@csrf_exempt
def update_assignment(request):
    """ Accepts a file with resulting data from offline worker.
    :param request: POST (task_assignment_id, result_file)
    :return: 200 OK
    """
    print(list(request.POST.items()))
    task_assignment_id = request.POST['task_assignment_id']
    result = request.FILES['result_file']
    models.TaskAssignment.update_task(task_assignment_id, result)
    return HttpResponse(content='')
