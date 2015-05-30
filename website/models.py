from remoteV8Site import settings
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.timezone import now as utc_now

import datetime
import random
from . import utils


scripts_storage = FileSystemStorage(location='{}/scripts'.format(settings.MEDIA_ROOT))
csv_storage = FileSystemStorage(location='{}/csv'.format(settings.MEDIA_ROOT))
result_storage = FileSystemStorage(location='{}/results'.format(settings.MEDIA_ROOT))


class Worker(models.Model):
    worker_id = models.CharField(unique=True, max_length=100)
    benchmark_result = models.IntegerField(null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return '{} (benchmark {}, {} pts.)'\
            .format(self.worker_id, self.benchmark_result, self.points)

    @staticmethod
    def get_worker(worker_id):
        return Worker.objects.get(worker_id=worker_id)


class Task(models.Model):
    customer = models.ForeignKey(User, null=True)
    task_name = models.CharField(unique=True, max_length=100)
    script = models.FileField(storage=scripts_storage)
    csv_data = models.FileField(storage=csv_storage)
    result = models.FileField(storage=result_storage)
    computed = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=utc_now)
    is_benchmark = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    BENCHMARK_TASK_SCRIPT_PATH = "benchmark.js"
    BENCHMARK_TASK_DATA_PATH = "numbers.csv"

    def __str__(self):
        return '{} (done: {})'.format(self.task_name, self.computed)

    @property
    def assignment(self):
        return TaskAssignment.objects.filter(task=self.id).first()

    @property
    def script_file(self):
        return bytes(filter(lambda c: c != b'\r', self.script.read()))

    @property
    def csv_data_file(self):
        return bytes(filter(lambda c: c != b'\r', self.csv_data.read()))

    @property
    def result_file(self):
        return bytes(filter(lambda c: c != b'\r', self.result.read()))

    @staticmethod
    def get_benchmark_task():
        task, _ = Task.objects.get_or_create(
            task_name='benchmark', is_benchmark=True,
            script=Task.BENCHMARK_TASK_SCRIPT_PATH,
            csv_data=Task.BENCHMARK_TASK_DATA_PATH,
        )
        return task

    @staticmethod
    def get_customer_tasks(user):
        return Task.objects.filter(customer=user).order_by('-create_date')

    @staticmethod
    def get_user_balance(user):
        return Task.objects.filter(customer=user).aggregate(models.Sum('points'))['points__sum']


class TaskAssignment(models.Model):
    task = models.ForeignKey(Task)
    worker = models.ForeignKey(Worker)
    assignment_date = models.DateTimeField(default=utc_now)
    last_update = models.DateTimeField(default=utc_now)

    def __str__(self):
        return 'Assignment {} (task {}, worker {}, given {})'.format(
            self.id, self.task.id, self.worker.id, self.assignment_date)

    @staticmethod
    def assign_latest_task(worker, benchmark_probability=0.1):
        task = Task.objects.filter(computed=False).order_by('create_date').first()
        assign_benchmark = random.random() < benchmark_probability
        if assign_benchmark:
            return TaskAssignment.assign_benchmark_task(worker)
        elif task is not None:
            return TaskAssignment._assign_task(task, worker)
        else:
            return utils.Struct(id='no-task')

    @staticmethod
    def assign_benchmark_task(worker):
        return TaskAssignment._assign_task(Task.get_benchmark_task(), worker)

    @staticmethod
    def _assign_task(task, worker):
        assignment, _ = TaskAssignment.objects.get_or_create(
            worker=worker, task=task, assignment_date=utc_now()
        )
        return assignment

    @staticmethod
    def update_task(task_assignment_id, result):
        assignment = TaskAssignment.objects.get(id=task_assignment_id)
        assignment.task.result = result
        assignment.task.computed = True
        assignment.last_update = utc_now()
        timedelta = (assignment.last_update - assignment.assignment_date).seconds
        if assignment.task.is_benchmark:
            assignment.worker.benchmark_result = timedelta
        else:
            benchmark = assignment.worker.benchmark_result
            assignment.worker.points += int(round(timedelta / benchmark, 0))
            assignment.task.points += assignment.worker.points
        assignment.task.save()
        assignment.save()
        assignment.worker.save()


admin.site.register([Task, TaskAssignment, Worker])