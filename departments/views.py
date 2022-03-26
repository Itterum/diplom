from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Department
from .serializers import (
    DepartmentsSerializer,
)


class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentsSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated]
