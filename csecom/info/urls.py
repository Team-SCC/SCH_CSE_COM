from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('',views.CalendarView.as_view(), name='main'),
    path('m1/', views.m1, name='m1'),
    path('m2/', views.m2, name='m2'),
    path('<int:schedule_id>/', views.schedule_view, name='schedule'),
    
]

