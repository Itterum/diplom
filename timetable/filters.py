from django_filters import rest_framework as filters

from .models import Timetable
from groups.models import Group


class TimetableFilter(filters.FilterSet):
    class Meta:
        model = Timetable
        fields = ('teacher', 'session', 'group')

    def group_filter(self, queryset, name, value):
        group_queryset = Group.objects.filter(gruop=value)
        return queryset.filter(spec__in=group_queryset)