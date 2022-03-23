from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class ProfileCreationForm(UserCreationForm):
    fieldsets = (
        ('Personal info', {
            'fields': (
                'username', 'password', 'department','full_name', 'first_name', 'last_name',
                'gender', 'email', 'birth_date', 'phone_number', 'user_type',
                'address', 'photo', 'is_active', 'is_superuser', 'group',
                'phone_number_parents', 'educ_type', 'position', 'qualification'
            )
        }),
    )
    add_fieldsets = (
        ('Personal info', {
            'fields': (
                'username', 'password1', 'department','password2', 'full_name', 'first_name', 'last_name',
                'gender', 'email', 'birth_date', 'phone_number', 'user_type',
                'address', 'photo', 'is_active', 'is_superuser', 'group',
                'phone_number_parents', 'educ_type', 'position', 'qualification'
            )
        }),
    )

    class Meta(UserCreationForm):
        model = Profile
        fields = (
            'username', 'password', 'department','full_name', 'first_name', 'last_name',
            'gender', 'email', 'birth_date', 'phone_number', 'user_type',
            'address', 'photo', 'is_active', 'is_superuser', 'group',
            'phone_number_parents', 'educ_type', 'position', 'qualification'
        )


class ProfileChangeForm(UserChangeForm):
    fieldsets = (
        ('Personal info', {
            'fields': (
                'username', 'password', 'department','full_name', 'first_name', 'last_name',
                'gender', 'email', 'birth_date', 'phone_number', 'user_type',
                'address', 'photo', 'is_active', 'is_superuser', 'group',
                'phone_number_parents', 'educ_type', 'position', 'qualification'
            )
        }),
    )
    add_fieldsets = (
        ('Personal info', {
            'fields': (
                'username', 'password1', 'department','password2', 'full_name', 'first_name', 'last_name',
                'gender', 'email', 'birth_date', 'phone_number', 'user_type',
                'address', 'photo', 'is_active', 'is_superuser', 'group',
                'phone_number_parents', 'educ_type', 'position', 'qualification'
            )
        }),
    )

    class Meta:
        model = Profile
        fields = (
            'username', 'password', 'department','full_name', 'first_name', 'last_name',
            'gender', 'email', 'birth_date', 'phone_number',
            'address', 'photo', 'is_active', 'is_superuser', 'group',
            'phone_number_parents', 'educ_type', 'position', 'qualification'
        )
