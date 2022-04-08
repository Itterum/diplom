from django_filters import rest_framework as filters

from departments.models import Department

from .models import Photo


class GalleryFilter(filters.FilterSet):

    department = filters.CharFilter(method='department_filter')

    class Meta:
        model = Photo
        fields = ('department',)

    def department_filter(self, queryset, name, value):
        gallery_filter = Department.objects.get(id=value).gallery
        return queryset.filter(gallery=gallery_filter)
