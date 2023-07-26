from django.db import models

class TimetableTest(models.Model):
    time = models.TextField()
    MON = models.TextField()
    TUE = models.TextField()
    WED = models.TextField()
    THU = models.TextField()
    FRI = models.TextField()