from django.db import models
from django.urls import reverse


class schedule(models.Model):
    content = models.TextField(max_length=15)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.content} / {self.start_time}"
    
    @property
    def get_url(self):
        url = reverse('info:schedule', args=(self.id,))    
        return f"{self.content}"
        
    #f"{self.content}"
    #'<a href="{url}"> {self.content} </a>'

    