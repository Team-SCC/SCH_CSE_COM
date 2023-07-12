from django.shortcuts import render, redirect
from .forms import *


def qanda_views(request):
    return render(request, 'qanda.html')

def QandaView(request):
    if request.method =='POST':
        form = QandaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QandaForm()
    return render(request, 'qanda.html', {'form':form})

def QandalistView(request):
    articleList = Qanda.objects.all()
    return render(request, 'qandalist.html', {'articleList':articleList})