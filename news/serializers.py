from rest_framework import serializers

from mixins.serializers import Base64ImageField

from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        depth = 1
        fields = ('id', 'name', 'description', 'department', 'photo', 'photos', 'date', 'is_active')


class NewsCreateSerializer(serializers.ModelSerializer):

    photo = Base64ImageField()

    class Meta:
        model = News
        fields = ('id', 'name', 'description', 'department', 'photo', 'photos', 'date', 'is_active')
