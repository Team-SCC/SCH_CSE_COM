from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy

def main(request):
    return render(request, 'main.html')

def empty_page(request):
    return redirect('main')

@login_required(login_url='common:login')
def test_page(request):
    return render(request, 'test.html')

class MyPasswordChangeView(PasswordChangeView):
    template_name = "password_change.html"
    success_url = reverse_lazy('password-change-done-view')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"