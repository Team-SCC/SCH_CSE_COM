from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'cloud'

urlpatterns = [
    path('', views.cloud_main, name='cloud_main'),
    path('create/', views.content_create, name='content_create'),
    path('create/upload', views.content_create, name='content_create'),
    path('delete/<int:content_id>/', views.content_delete, name='content_delete'),
    path('download/', views.file_download, name='file_download')
]
