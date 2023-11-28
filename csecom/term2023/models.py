from django.db import models
import os
import sys

from .utils import file_name_creater


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.models import User

class Term2023Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='term2023_author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='term2023_voter_question')
    image = models.FileField(upload_to=file_name_creater)

    def __str__(self):
        return self.subject
    
class Term2023Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='term2023_author_answer')
    question = models.ForeignKey(Term2023Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='term2023_voter_answer')

class Term2023Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Term2023Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Term2023Answer, null=True, blank=True, on_delete=models.CASCADE)
