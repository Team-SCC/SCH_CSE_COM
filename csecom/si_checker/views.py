from django.shortcuts import render, redirect
from django.conf import settings

def si_checker(request):
    return render(request, 'si_checker.html')
