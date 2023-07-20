from django.db import models

class Qanda(models.Model):
    title = models.CharField(max_length=50)
    cdate = models.DateTimeField(editable=True)
    contents = models.TextField()

    def __str__(self):
        return self.title
