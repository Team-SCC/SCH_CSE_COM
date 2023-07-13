from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def si_checker(request):
    return render(request, 'si_checker.html')
