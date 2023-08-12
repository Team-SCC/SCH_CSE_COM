from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import Calendar, ScheduleForm
from django.views import generic
from datetime import datetime, timedelta
from django.utils.safestring import mark_safe
from django.urls import reverse
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def info_main(request):
    return render(request, 'info_main.html')

def m1(request):
    if 'cont1' not in request.session:
        request.session['cont1'] = False
    if request.method == "POST":
        request.session['cont1'] = not request.session['cont1']
        return redirect('info:m1')
    if request.session['cont1'] == False:
        return redirect('info:main')

    return render(request, 'info_main.html', {'cont1': request.session['cont1']})


def m2(request):
    if 'cont2' not in request.session:
        request.session['cont2'] = False
    if request.method == "POST":
        request.session['cont2'] = not request.session['cont2']
        return redirect('info:m2')
    if request.session['cont2'] == False:
        return redirect('info:main')
    return render(request, 'info_main.html', {'cont2': request.session['cont2']})


def get_date(req):
    if req: 
        year, month = (int(x) for x in req.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()

class CalendarView(generic.ListView):
    model = schedule
    template_name = 'info_main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context
    
def schedule_view(request, schedule_id):
    content = get_object_or_404(schedule, pk=schedule_id)
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.content = content
            res.start_time = timezone.now()
            res.save()
            return redirect('info:main')
    else:
        form = ScheduleForm()
    context = {'form': form}
    return render(request, 'info:main', context)
