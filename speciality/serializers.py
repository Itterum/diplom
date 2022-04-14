from rest_framework import serializers
from .models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = ('id', 'name', 'department', 'remote_education_time', 'locale_education_time', 'is_active')
