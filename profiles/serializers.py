from rest_framework import serializers

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
