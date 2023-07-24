# from django.db import models


# class Qanda(models.Model):
#     name = models.CharField(max_length=15, default='', null=True)
#     title = models.CharField(max_length=50)
#     cdate = models.DateTimeField(editable=True)
#     contents = models.TextField()
    
#     def __str__(self):
#         return self.title
    
# class Answer(models.Model):
#     question = models.ForeignKey(Qanda, on_delete=models.CASCADE)
#     contents = models.TextField()
#     cdate = models.DateTimeField()
