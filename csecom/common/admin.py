from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('student_id', 'name', 'is_admin','is_student_pay','locker_id')
    list_filter = ('is_admin','is_student_pay')
    fieldsets = (
        (None, {'fields': ('student_id', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin','is_student_pay','locker_id')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_id', 'name', 'password1', 'password2')}
        ),
    )
    search_fields = ('student_id',)
    ordering = ('student_id',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
