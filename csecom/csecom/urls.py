from django.contrib import admin
from django.urls import path, include
from . import views
from .views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'csecom'

urlpatterns = [
    path('', views.empty_page),
    path('main/', views.main, name='main'),
    path('test/', views.test_page, name='test'),
    path('admin/', admin.site.urls),
    path('locker/', include('locker.urls')),
    path('common/', include('common.urls')),
    path('si_checker/', include('si_checker.urls')),
    path('cloud/', include('cloud.urls')),
    path('qanda/', include('qanda.urls')),
    path('change-password/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('change-password/done', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),
]
