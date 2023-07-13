from django.db import models
import os
import sys

from .utils import file_name_creater

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.models import User

class Content(models.Model):
    '''클라우드 게시글 모델
    author: 작성자
    title: 제목
    file: 파일(미디어 파일, 멀티 옵션 true)
    create_date: 작성일
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    file = models.FileField(upload_to=file_name_creater)
    create_date = models.DateTimeField()

    def __str__(self):
        text = str(self.create_date)[:10]
        return f'{text} {self.title}'
