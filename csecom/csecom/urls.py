from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



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
    path('password/', include('password.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
