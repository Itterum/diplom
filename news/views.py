from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News
from .serializers import (
    NewsListSerializer,
)


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга фильму"""
    serializer_class = NewsListSerializer
    queryset = News.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]  # проверка на авторизированого юзера

    filter_fields = ['department']  # фильтрация по полям ?department="значение"
    search_fields = ['name']  # поиск по полям ?search="значение"
    ordering_fields = ['name']  # сортировка по полям ?ordering="значение"

    # пример совместного использования ?department="значение"&search="значение"&?ordering="значение"
