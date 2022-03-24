from rest_framework import serializers

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
