from rest_framework import serializers
from .models import Speciality


class SpecialityListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Speciality
        fields = "__all__"
