from django.shortcuts import render

def locker_main(request):
    return render(request, 'locker.html')
