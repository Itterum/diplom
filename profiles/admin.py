# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile


class CustomUserAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile

    fieldsets = add_form.fieldsets
    add_fieldsets = add_form.add_fieldsets

    list_display = (
        'username', 'full_name', 'user_type'
    )
    list_filter = (
        'user_type', 'gender'
    )
    search_fields = (
        'full_name', 'email', 'phone_number', 'address'
    )

    # ordering = ('email',)


admin.site.register(Profile, CustomUserAdmin)
# don't show groups
# admin.site.register(TeacherGroup)
# admin.site.register(Student)
admin.site.unregister(Group)
