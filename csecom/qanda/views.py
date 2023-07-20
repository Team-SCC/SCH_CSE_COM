from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def qandawriting_view(request):
    if request.method =='POST':
        form = QandaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QandaForm()
    return render(request, 'qandawriting.html', {'form':form})

def qanda_view(request):
    qanda = Qanda.objects.all()
    return render(request, 'qanda.html', {'qanda':qanda})

def qandalist_view(request, pk):
    list = get_object_or_404(Qanda, id=pk)
    return render(request, 'qandalist.html', {'list':list})