from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
    context = {'list': list}
    return render(request, 'qandalist.html', context)

def qanda_answer(request, pk):
    question = get_object_or_404(Qanda, id=pk)
    answer = Answer(question=question, contents=request.POST.get('contents'), cdate=timezone.now())
    answer.save()
    return redirect('qanda:list', pk=question.id)