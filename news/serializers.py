from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        depth = 1
        fields = ('id', 'name', 'description', 'department', 'photo', 'photos', 'date', 'is_active')

class NewsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'name', 'description', 'department', 'photo', 'photos', 'date', 'is_active')