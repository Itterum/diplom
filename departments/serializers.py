from rest_framework import serializers

from .models import Department

from news.models import News
from news.serializers import NewsListSerializer

from groups.models import Group
from speciality.models import Speciality


class DepartmentsListSerializer(serializers.ModelSerializer):
    """Вывод кафедры"""

    news = serializers.SerializerMethodField()

    # TODO:
    # count_news = serializers.SerializerMethodField()
    # count_groups = serializers.SerializerMethodField()
    # count_specialty = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'news', 'name', 'email', 'phone_number', 'address',
                  'description', 'photo', 'photos', 'manager_department')

    def get_news(self, obj):
        return NewsListSerializer(News.objects.filter(department=obj), many=True).data
