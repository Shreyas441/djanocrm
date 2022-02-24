from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('administrator_login',views.administrator_login, name='administrator_login'),
    path('administrator_client_delete/<str:pk>',views.administrator_client_delete, name='administrator_client_delete'),
    path('administrator_client_Update/<str:pk>',views.administrator_client_Update, name='administrator_client_Update'),
    path('logout',views.logout_view, name='logout'),
    path('administrator_home',views.administrator_home, name='administrator_home'),
    path('Agent_Signup',views.Agent_Signup, name='Agent_Signup'),
    path('administrator_Signup',views.administrator_Signup, name='administrator_Signup'),
    path('Lead_details',views.Lead_details, name='Lead_details'),
    path('Client_details',views.Client_details, name='Client_details'),
    path('Trail_details',views.Trail_details, name='Trail_details'),
    path('service_sales',views.service_sales, name='service_sales'),
    path('service_sales_report',views.service_sales_report, name='service_sales_report'),
    path('Agent_report',views.Agent_report, name='Agent_report'),
    path('Services_taken_request_details',views.Services_taken_request_details, name='Services_taken_request_details'),
    path('service_add',views.service_add, name='service_add'),
    path('admin_Service_taken_add',views.admin_Service_taken_add, name='admin_Service_taken_add'),
    path('service_update/<str:pk>',views.service_update, name='service_update'),
    path('admin_Service_taken_delete/<str:pk>',views.admin_Service_taken_delete, name='admin_Service_taken_delete'),
    path('admin_Service_taken_Update/<str:pk>',views.admin_Service_taken_Update, name='admin_Service_taken_Update'),
    path('service_delete/<str:pk>',views.service_delete, name='service_delete'),
    path('approve_trial/<str:pk>',views.approve_trial, name='approve_trial'),
    path('Delete_trial/<str:pk>',views.Delete_trial, name='Delete_trial'),
    path('Reject_trial/<str:pk>',views.Reject_trial, name='Reject_trial'),
    path('Revenue',views.Revenue, name='Revenue'),
]