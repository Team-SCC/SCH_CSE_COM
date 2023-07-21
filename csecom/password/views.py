from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView


class MyPasswordChangeView(PasswordChangeView):
    template_name = "password_change.html"
    success_url = "done"

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"