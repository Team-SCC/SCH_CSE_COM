from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def si_checker(request):
    
    user = request.user
    
    if user.is_check:
        return render(request, 'si_checker.html', {'is_check': True})
    
    return render(request, 'si_checker.html', {'is_check': False})
