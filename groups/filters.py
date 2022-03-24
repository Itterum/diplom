from django_filters import rest_framework as filters

from speciality.models import Speciality

from .models import Group


class GroupFilter(filters.FilterSet):

    department = filters.CharFilter(method='department_filter')

    class Meta:
        model = Group
        fields = ('department',)

    def department_filter(self, queryset, name, value):
        speciality_queryset = Speciality.objects.filter(department=value)
        return queryset.filter(spec__in=speciality_queryset)
