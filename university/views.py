from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Students, Teachers, Department, Groups
from .serializers import (
    StudentListSerializer,
    StudentDetailSerializer,
    DepartmentListSerializer,
    DepartmentDetailSerializer,
    TeacherListSerializer,
    TeacherDetailSerializer,
    GroupListSerializer,
    GroupDetailSerializer,
)
from .service import StudentFilter, DepartmentFilter, TeachersFilter, GroupsFilter


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        students = Students.objects.all()
        return students

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentListSerializer
        elif self.action == 'retrieve':
            return StudentDetailSerializer


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DepartmentFilter

    def get_queryset(self):
        department = Department.objects.all()
        return department

    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentListSerializer
        elif self.action == 'retrieve':
            return DepartmentDetailSerializer


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TeachersFilter

    def get_queryset(self):
        teachers = Teachers.objects.all()
        return teachers

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherListSerializer
        elif self.action == 'retrieve':
            return TeacherDetailSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GroupsFilter

    def get_queryset(self):
        groups = Groups.objects.all()
        return groups

    def get_serializer_class(self):
        if self.action == 'list':
            return GroupListSerializer
        elif self.action == 'retrieve':
            return GroupDetailSerializer
