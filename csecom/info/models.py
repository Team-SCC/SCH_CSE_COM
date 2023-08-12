from django.db import models
from django.urls import reverse
from calendar import HTMLCalendar

class schedule(models.Model):
    content = models.TextField(max_length=15)
    start_time = models.DateTimeField()

    @property
    def get_url(self):
        url = reverse('info:schedule', args=(self.id,))
        day = mon()
        return f'<a href="{url}">{day}</a>'
    

def mon(self):
    for week in self.monthdays2calendar(self.start_time.year, self.start_time.month):
        for d, weekday in week:
            return d