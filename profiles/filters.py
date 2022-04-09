from django_filters import rest_framework as filters

from .models import Profile


class ProfileFilter(filters.FilterSet):

    unattached_students = filters.CharFilter(method='unattached_students_filter')

    class Meta:
        model = Profile
        fields = ('department', 'unattached_students')

    def unattached_students_filter(self, queryset, name, value):
        queryset = Profile.objects.filter(user_type=Profile.USER_TYPE[0][0],
                                          group=None, department=value)
        return queryset
