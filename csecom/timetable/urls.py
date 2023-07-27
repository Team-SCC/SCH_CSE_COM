from django.urls import path

from . import views

app_name = "timetable"

urlpatterns = [
    path('1/', views.timetable_view_grade1, name='timetable_view1'),
    path('2/', views.timetable_view_grade2, name='timetable_view2'),
    path('3/', views.timetable_view_grade3, name='timetable_view3'),
    path('4/', views.timetable_view_grade4, name='timetable_view4'),

    path('m610/', views.timetable_view_m610, name='timetable_view_m610'),
    path('m615/', views.timetable_view_m615, name='timetable_view_m615'),
    path('m618/', views.timetable_view_m618, name='timetable_view_m618'),
    path('m619/', views.timetable_view_m619, name='timetable_view_m619'),
    path('m620/', views.timetable_view_m620, name='timetable_view_m620'),
]
