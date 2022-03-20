from rest_framework import serializers
# from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'username', 'department', 'full_name', 'first_name', 'last_name',
            'gender', 'email', 'birth_date', 'phone_number', 'user_type',
            'address', 'photo', 'group',
            'phone_number_parents', 'educ_type', 'position', 'qualification',
        )
