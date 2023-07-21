from django.urls import path
from . import views
from .views import MyPasswordChangeView, MyPasswordResetDoneView
from django.contrib.auth.decorators import login_required
app_name = 'password'

urlpatterns = [
    path('change/', login_required(MyPasswordChangeView.as_view()), name='password-change-view'),
    path('change/done', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),
]

