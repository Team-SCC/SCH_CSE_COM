from django.urls import path
from . import views

app_name = 'qanda'

urlpatterns = [
    path('', views.qanda_view, name='main'),
    path('writing/', views.qandawriting_view, name='writing'),
    path('list/<int:pk>', views.qandalist_view, name='list'),
    path('answer/<int:pk>/', views.qanda_answer, name='answer'),
]