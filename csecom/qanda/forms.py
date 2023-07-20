from django import forms
from .models import *
#from common.models import *

class QandaForm(forms.ModelForm):
    class Meta:
        model = Qanda
        fields = ['title', 'cdate', 'contents']
