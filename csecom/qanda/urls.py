from django.urls import path
from . import views

app_name = 'qanda'

urlpatterns = [
    path('', views.qanda_view, name='qanda'),
    path('writing/', views.qandawriting_view, name='writing'),
    path('list/', views.qandalist_view, name='list'),
]