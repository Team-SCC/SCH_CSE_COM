from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def locker_main(request):
    return render(request, 'locker.html')
