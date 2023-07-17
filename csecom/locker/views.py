import os
import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.models import User
from common.forms import UserChangeLockerForm

@login_required(login_url='common:login')
def locker_main(request):
    locker_list = []
    
    for i in User.objects.all():
        locker_list.append(i.locker_id)

    context = {'locker_list': locker_list}
    
    return render(request, 'locker.html', context)

@login_required(login_url='common:login')
def locker_create(request):
    '''사물함 신청 함수
    url: localhost:port/locker/create/
    '''
    
    if request.method == 'POST':
        if request.POST['number'] != '':
            
            if request.user.locker_id == 0:
                locker_number = int(request.POST['number'][:-1])
                user = request.user
                user.locker_id = locker_number
                user.save()
                
            else:
                print('이미 사물함 사용중')
            
        else:
            return redirect('locker:locker')

        return redirect('locker:locker')

    return render(request, 'locker_create.html')
