from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Bank'
urlpatterns = [
    path('', views.index, name='index'),
    path('ifsc/', views.get_name, name='ifsc_codes'),
    path('branch/', views.branch_name, name='branches'),
                ]
