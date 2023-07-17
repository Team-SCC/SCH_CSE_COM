from django.contrib import admin

from .models import Content

class ContentAdmin(admin.ModelAdmin):
    search_fields = ['title']
    
admin.site.register(Content, ContentAdmin)
