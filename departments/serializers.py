from rest_framework import serializers
from .models import Department
from news.models import News
from news.serializers import NewsListSerializer


class DepartmentsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    news = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"

    def get_news(obj):
        return NewsListSerializer(News.objects.filter(department=obj), many=True).data
