from django.urls import path

from . import views

urlpatterns = [
    path('', views.si_checker, name='si_checker'),
]
