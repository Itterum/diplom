from rest_framework import serializers
from .models import Department
from news.models import News
from news.serializers import NewsListSerializer
from profiles.serializers import ProfileSerializer


class DepartmentsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    news = serializers.SerializerMethodField()
    manager_department = ProfileSerializer()

    class Meta:
        model = Department
        fields = "__all__"

    def get_news(self, obj):
        return NewsListSerializer(News.objects.filter(department=obj), many=True).data
