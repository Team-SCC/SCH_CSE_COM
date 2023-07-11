from django.urls import path
from . import views

urlpatterns = [
    path('', views.qanda_views, name='qanda'),
    path('qandalist/', views.QandalistView, name='qandalist'),

]