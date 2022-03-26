from rest_framework import serializers
from .models import Timetable


class TimetableSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Timetable
        fields = ('para', 'visit', 'type', 'id', 'date', 'discipline',
                  'teacher', 'department', 'group', 'session')
