from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Content

class ContentAdmin(admin.ModelAdmin):
    search_fields = ['title']
    
admin.site.register(Content, ContentAdmin)
