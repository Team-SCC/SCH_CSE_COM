from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Locker

@login_required(login_url='common:login')
def locker_main(request):
    return render(request, 'locker.html')

def locker_create(request):
    '''사물함 신청 함수
    url: localhost:port/locker/create/
    '''
    
    if request.method == 'POST':
        if request.POST['number'] != '':
            form = Locker()
            form.student_id = request.user
            form.locker_id = int(request.POST['number'][:-1])
            form.save()

        return redirect('locker:locker')

    return render(request, 'locker.html')
