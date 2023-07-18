from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def qanda_view(request):
    if request.method =='POST':
        form = QandaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QandaForm()
    return render(request, 'qanda.html', {'form':form})

def qandalist_view(request):
    qandaList = Qanda.objects.all()
    return render(request, 'qandalist.html', {'qandaList':qandaList})