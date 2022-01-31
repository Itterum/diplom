from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import News
from .serializers import (
    NewsListSerializer,
)

# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга фильму"""
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
