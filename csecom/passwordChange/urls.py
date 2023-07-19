from django.urls import path
from . import views
from .views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'passwordChange'

urlpatterns = [
    path('change-password/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('change-password/done', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),
]