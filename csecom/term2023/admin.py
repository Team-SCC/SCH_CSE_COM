from django.contrib import admin

from .models import *


class Term2023QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Term2023Question, Term2023QuestionAdmin)
