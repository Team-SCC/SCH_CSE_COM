from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import Calendar, ScheduleForm
from django.views import generic
from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
import calendar
from datetime import datetime, timedelta, date

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

def prev_month(d):
    mon = d.replace(day=1)
    prev_month = mon - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req):
    if req: 
        year, month = (int(x) for x in req.split('-'))
        return date(year, month, day=1)
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
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
    
# generic.ListView의 get_context_data메서드를 오버라이드함 
# 현재 몇 월인지에 대한 월 정보를 가져옴
# 생성한 달력을 HTML형식으로 생성
# mark_safe함수를 이용해 html 안전하게 렌더링 되도록 함


def schedule_view(request, schedule_id):
    sch = get_object_or_404(schedule, pk=schedule_id)
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.content = sch
            res.save()
            return redirect('info:main')
    else:
        form = ScheduleForm()
    context = {'form': form}
    return render(request, 'info_form.html', context)