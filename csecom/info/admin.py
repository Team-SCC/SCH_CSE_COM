from django.contrib import admin
from .models import schedule

admin.site.register(schedule)

class InfoAdmin(admin.ModelAdmin):

    list_display = ('content', 'start_time')
# Register your models here.
