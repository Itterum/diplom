from rest_framework import serializers
from .models import News


class NewsListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = News
        fields = ("id", "name", "description", "department", "photo", "photos")
