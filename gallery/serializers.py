from rest_framework import serializers

from mixins.serializers import Base64ImageField

from .models import Gallery, Photo


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        depth = 1
        fields = ['id', 'title', 'description', 'photo_set']


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['image']


class GalleryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'description']


class PhotoCreateSerializer(serializers.ModelSerializer):

    image = Base64ImageField()

    class Meta:
        model = Photo
        fields = ['image', 'gallery']
