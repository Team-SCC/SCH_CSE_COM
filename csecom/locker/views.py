import os
import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.models import User

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

@login_required(login_url='common:login')
def locker_return(request):
    '''사물함 반납 함수
    url: localhost:port/locker/return/
    '''

    if request.method == 'POST':

        # 사용 중인 사물함이 있을 경우 request한 user의 locker_id 속성을 0으로 지정
        if request.user.locker_id != 0: 
            user = request.user
            user.locker_id = 0
            user.save()

        # 없을 경우 터미널에 출력, 만약 부가 기능 추가를 원하면 else문 밑에 구현하면 됨            
        else:
            print('사용 중인 사물함이 없습니다')

        return redirect('locker:locker')

    return render(request, 'locker_return.html')