from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView

# Create your views here.
class MyPasswordChangeView(PasswordChangeView):
    template_name = "password_change.html"
    success_url = reverse_lazy('password-change-done-view')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"