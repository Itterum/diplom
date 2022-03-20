from rest_framework import serializers

from .models import Department

from news.models import News
from news.serializers import NewsListSerializer

from groups.models import Group


class DepartmentsListSerializer(serializers.ModelSerializer):
    """Вывод кафедры"""

    news = serializers.SerializerMethodField()

    count_news = serializers.IntegerField(source='news_set.count')
    count_specialty = serializers.IntegerField(
        source='speciality_set.count'
    )
    count_groups = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'news', 'name', 'email', 'phone_number', 'address',
                  'description', 'photo', 'photos', 'manager_department',
                  'count_news', 'count_specialty', 'count_groups')

    def get_news(self, obj):
        return NewsListSerializer(News.objects.filter(department=obj),
                                  many=True).data

    def get_count_groups(self, obj):
        speciality = obj.speciality_set.all()
        groups = Group.objects.filter(spec__in=speciality).count()
        return groups
