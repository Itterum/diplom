from rest_framework import serializers

from .models import Timetable


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        depth = 1
        fields = ('para', 'visit', 'type', 'id', 'date', 'discipline',
                  'teacher', 'department', 'group', 'session', 'is_active',
                  'description')


class TimetableCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ('para', 'visit', 'type', 'id', 'date', 'discipline',
                  'teacher', 'department', 'group', 'session', 'is_active',
                  'description')
