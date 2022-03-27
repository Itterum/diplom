from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = News
        depth = 1
        fields = ('id', 'name', 'description', 'department', 'photo', 'photos', 'date')
