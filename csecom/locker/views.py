from django.shortcuts import render, redirect

def locker_main(request):
    return render(request, 'locker.html')
