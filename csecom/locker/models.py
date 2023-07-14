from django.db import models
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.models import User

class Locker(models.Model):
    '''사물함 모델
    locker_id: 사물함 번호
    student_id: 학번
    '''
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    locker_id = models.IntegerField(null=0)

    def __str__(self):
        return f'{self.student_id} {self.locker_id}'

    @property
    def locker_numbers(self):
        return f'{self.locker_id}'