from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Department
from .serializers import (
    DepartmentsListSerializer,
)

# Create your views here.
class DepartmentsViewSet(viewsets.ModelViewSet):

    serializer_class = DepartmentsListSerializer
    queryset = Department.objects.all()


