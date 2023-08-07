from django.shortcuts import render, redirect
from .models import *

def info_main(request):
    return render(request, 'info_main.html')

def m1(request):
    if 'content1' not in request.session:
        request.session['content1'] = False

    if request.method == "POST":
        request.session['content1'] = not request.session['content1']
        return redirect('info:m1')  # 리디렉션 추가

    return render(request, 'info_main.html', {'content1': request.session['content1']})


def m2(request):
    if 'content2' not in request.session:
        request.session['content2'] = False

    if request.method == "POST":
        request.session['content2'] = not request.session['content2']
        return redirect('info:m2')  # 리디렉션 추가

    return render(request, 'info_main.html', {'content2': request.session['content2']})