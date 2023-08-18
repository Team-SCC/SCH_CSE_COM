from django.db import models
from django.urls import reverse
from calendar import HTMLCalendar

class schedule(models.Model):
    content = models.TextField(max_length=15)
    start_time = models.DateTimeField()
    
    
    @property
    def get_url(self):
        url = reverse('info:schedule', args=(self.id,))
        for week in self.monthdays2calendar(self.year, self.month):
            for d, weekday in week:
                #day = self.start_time.day 
                return f'<a href="{url}"> {d} </a>' 