from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Students, Department, Teachers, Groups


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class StudentFilter(filters.FilterSet):
    full_name = CharFilterInFilter(field_name='full__name', lookup_expr='in')
    email = filters.RangeFilter()
    address = filters.RangeFilter()

    class Meta:
        model = Students
        fields = ['full_name', 'email', 'address', 'phone_number']


class DepartmentFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    email = filters.RangeFilter()
    address = filters.RangeFilter()

    class Meta:
        model = Department
        fields = ['name', 'email', 'address', 'phone_number']


class TeachersFilter(filters.FilterSet):
    full_name = CharFilterInFilter(field_name='full__name', lookup_expr='in')
    email = filters.RangeFilter()
    address = filters.RangeFilter()

    class Meta:
        model = Teachers
        fields = ['full_name', 'email', 'address', 'phone_number']


class GroupsFilter(filters.FilterSet):
    group_number = CharFilterInFilter(field_name='group_number', lookup_expr='in')
    headman = filters.RangeFilter()
    name_of_specialty = filters.RangeFilter()

    class Meta:
        model = Groups
        fields = ['group_number', 'headman', 'name_of_specialty']
