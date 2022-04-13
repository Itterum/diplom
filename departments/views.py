from rest_framework import viewsets
from mixins.views import DeleteSetMixin
from management.permissions import IsManagerOrReadOnly

from .models import Department
from .serializers import (
    DepartmentsSerializer,
    DepartmentsUpdateSerializer,
)


class DepartmentsViewSet(DeleteSetMixin, viewsets.ModelViewSet):
    queryset = Department.objects.filter(is_active=True)

    serializer_classes = {
        'list': DepartmentsSerializer,
        'partial_update': DepartmentsUpdateSerializer,
        'update': DepartmentsUpdateSerializer,
    }
    permission_classes = [IsManagerOrReadOnly]

    default_serializer_class = DepartmentsSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)
