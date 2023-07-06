from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'cloud'

urlpatterns = [
    path('', views.cloud_main, name='cloud_main'),
    path('delete/', views.content_delete, name='content_delete'),
    path('create/', views.content_create, name='content_create'),
    path('download/', views.file_download, name='file_download')
]
