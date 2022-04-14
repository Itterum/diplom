from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from mixins.views import DeleteSetMixin
from management.permissions import IsManagerOrReadOnly

from .models import News
from .serializers import (
    NewsSerializer, NewsCreateSerializer
)


class NewsViewSet(DeleteSetMixin, viewsets.ModelViewSet):
    """Листинг новостей"""
    serializer_classes = {
        'list': NewsSerializer,
        'partial_update': NewsCreateSerializer,
        'update': NewsCreateSerializer,
        'create': NewsCreateSerializer,
    }

    queryset = News.objects.filter(is_active=True)

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsManagerOrReadOnly]

    default_serialuzer_class = NewsSerializer

    filter_fields = ['department']  # фильтрация по полям ?department="значение"
    search_fields = ['name']  # поиск по полям ?search="значение"
    ordering_fields = ['name']  # сортировка по полям ?ordering="значение"

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serialuzer_class)

    def update(self, request, *args, **kwargs):
        photo = request.data.get('photo')

        if photo:
            news = NewsSerializer(News.objects.get(pk=kwargs['pk'])).data
            if photo.endswith(news['photo']):
                request.data.pop('photo')

        return super().update(request, *args, **kwargs)
