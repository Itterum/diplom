from rest_framework import serializers
from .models import Department
from news.models import News
from profiles.models import Profile
from news.serializers import NewsListSerializer


def get_news(obj):
    return NewsListSerializer(News.objects.filter(department=obj), many=True).data


def get_teachers(obj):
    return NewsListSerializer(Profile.objects.filter(teacher='teacher'), many=True).data


class DepartmentsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    news = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = (
            "id", "name", "email", "phone_number", "address", "manager_department", "description", "photo", "photos",
            "news", "teachers")
