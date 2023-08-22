from django.db import models
from django.urls import reverse
from datetime import datetime
from calendar import HTMLCalendar

class schedule(models.Model):
    content = models.TextField(max_length=15)
    start_time = models.DateTimeField()
    
    
#    @property
#    def get_url(self):
#        url = reverse('info:schedule', args=(self.id,))
#        for week in self.monthdays2calendar(start_time__year=self.year, start_time__month=self.month):
#            for d, weekday in week:
#                day = d
#    
#        return f'<a href="{url}"> {self.content} </a>'
    