from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('',views.info_main, name='main'),
    path('m1/', views.m1, name='m1'),
    path('m2/', views.m2, name='m2'),
    path('curri/',views.curri, name='curri'),
]