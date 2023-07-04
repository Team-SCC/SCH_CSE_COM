from django.shortcuts import render, redirect

def si_checker(request):
    return render(request, 'si_checker.html')
