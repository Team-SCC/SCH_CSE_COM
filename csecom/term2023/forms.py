from django import forms

from .models import *


class Term2023QuestionForm(forms.ModelForm):
    class Meta:
        model = Term2023Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class Term2023AnswerForm(forms.ModelForm):
    class Meta:
        model = Term2023Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class Term2023CommentForm(forms.ModelForm):
    class Meta:
        model = Term2023Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
