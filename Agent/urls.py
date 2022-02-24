from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('Agent_login',views.Agent_login, name='Agent_login'),
    path('Service_taken_request',views.Service_taken_request, name='Service_taken_request'),
    path('Agent_home',views.Agent_home, name='Agent_home'),
    path('client_Update/<str:pk>',views.client_Update, name='client_Update'),
    path('Service_taken_Update/<str:pk>',views.Service_taken_Update, name='Service_taken_Update'),
    path('Service_taken_delete/<str:pk>',views.Service_taken_delete, name='Service_taken_delete'),
    path('client_Delete/<str:pk>',views.client_Delete, name='client_Delete'),
    path('client_add',views.client_add, name='client_add'),
    path('Service_taken_add',views.Service_taken_add, name='Service_taken_add'),
    path('Agent_trail',views.Agent_trail, name='Agent_trail'),
    path('Agent_trail_request',views.Agent_trail_request, name='Agent_trail_request'),
    path('Agent_Lead',views.Agent_Lead, name='Agent_Lead'),
    path('Agent_Lead_trail',views.Agent_Lead_trail, name='Agent_Lead_trail'),

]