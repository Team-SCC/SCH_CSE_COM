from django.urls import path

from . import views

app_name = "locker"

urlpatterns = [
    path('', views.locker_main, name='locker'),
    path('create', views.locker_create, name='locker_create'),
]
