from django_filters import rest_framework as filters

from .models import Timetable


class TimetableFilter(filters.FilterSet):
    class Meta:
        model = Timetable
        fields = ('teacher', 'session', 'group')
