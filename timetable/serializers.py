from rest_framework import serializers
from .models import Timetable
from disciplines.serializers import DisciplinesListSerializer
from profiles.serializers import ProfileSerializer
from departments.serializers import DepartmentsListSerializer
from groups.serializers import GroupsListSerializer



class TimetableListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""
    discipline = DisciplinesListSerializer()
    teacher = ProfileSerializer()
    department = DepartmentsListSerializer()
    group = GroupsListSerializer()

    class Meta:
        model = Timetable
        fields = "__all__"