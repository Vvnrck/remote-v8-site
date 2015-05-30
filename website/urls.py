from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from . import views

urlpatterns = patterns('',
   url(r'^$', views.HomeView.as_view(), name='home'),
   url(r'^task=(?P<task_id>[a-zA-Z0-9]+)$', views.TaskView.as_view(), name='task'),
   url(r'^login$', views.log_in, name='login'),
   url(r'^logout$', views.log_out, name='logout'),
   url(r'^registerCustomer$', views.register_customer, name='register-customer'),

   url(r'customer/getScript', login_required(views.send_script_to_customer), name='customer-get-script'),
   url(r'customer/getData', login_required(views.send_data_to_customer), name='customer-get-data'),
   url(r'customer/getResult', login_required(views.send_result_to_customer), name='customer-get-result'),


   url(r'^getTask', views.assign_task_to_worker, name='get-task'),
   url(r'^getScript', views.get_task_script, name='get-task-script'),
   url(r'^getData', views.get_task_data, name='get-task-data'),
   url(r'^postTaskData', views.update_assignment, name='post-task-data'),
   url(r'^registerWorker', views.register_worker, name='register-worker')
)