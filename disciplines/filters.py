from django_filters import rest_framework as filters

from departments.models import Department

from .models import Discipline


class DisciplineFilter(filters.FilterSet):

    department = filters.CharFilter(method='department_filter')

    class Meta:
        model = Discipline
        fields = ('department',)

    def department_filter(self, queryset, name, value):
        departments_queryset = Department.objects.filter(department=value)
        return queryset.filter(spec__in=departments_queryset)
