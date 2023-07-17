from django.contrib import admin

from .models import Locker

class LockerAdmin(admin.ModelAdmin):
    list_display = ('student_id','locker_id')
    ordering = ('locker_id',)
    
admin.site.register(Locker, LockerAdmin)
