from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from mixins.views import DeleteSetMixin
from management.permissions import IsManagerOrReadOnly

from .models import News
from .serializers import (
    NewsSerializer, NewsUpdateSerializer
)


class NewsViewSet(DeleteSetMixin, viewsets.ModelViewSet):
    """Листинг новостей"""
    serializer_class = {
        'list': NewsSerializer,
        'update': NewsUpdateSerializer,
    }

    queryset = News.objects.filter(is_active=True)

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsManagerOrReadOnly]

    default_serialuzer_class = NewsSerializer

    filter_fields = ['department']  # фильтрация по полям ?department="значение"
    search_fields = ['name']  # поиск по полям ?search="значение"
    ordering_fields = ['name']  # сортировка по полям ?ordering="значение"

    def get_serializer_class(self):
            return  self.serializer_classes.get(self.action,
                                                self.default_serialuzer_class)
