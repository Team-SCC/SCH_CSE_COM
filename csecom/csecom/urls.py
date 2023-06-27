from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'csecom'

urlpatterns = [
    path('', views.empty_page),
    path('admin/', admin.site.urls),
    path('main/', views.main, name='main'),
    path('locker/', include('locker.urls')),
    path('common/', include('common.urls')),
]
