from rest_framework import viewsets
from .models import Discipline
from .serializers import (
    DisciplinesSerializer,
    DisciplinesUpdateSerializer,
)

from mixins.views import DeleteSetMixin
from management.permissions import IsManagerOrReadOnly


class DisciplinesViewSet(DeleteSetMixin, viewsets.ModelViewSet):
    """Листинг дисциплин"""
    queryset = Discipline.objects.filter(is_active=True)
    filter_fields = ['department']

    serializer_class = {
        'list': DisciplinesSerializer,
        'update': DisciplinesUpdateSerializer,
    }

    permission_classes = [IsManagerOrReadOnly]

    default_serializer_class = DisciplinesSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)
