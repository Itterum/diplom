from rest_framework import viewsets
from .models import Department
from .serializers import (
    DepartmentsListSerializer,
)


# Create your views here.
class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentsListSerializer
    queryset = Department.objects.all()

