from rest_framework import serializers
from .models import Timetable


class TimetableListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Timetable
        fields = "__all__"
