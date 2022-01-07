from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Students, Department, Teachers, Groups
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


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Students.objects.all()
        serializer = StudentListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Students.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentDetailSerializer(student)
        # print(self.retrieve.u)
        return Response(serializer.data)


class StudentsReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentListSerializer


class StudentsModelViewSet(viewsets.ModelViewSet):
    serializer_class = StudentListSerializer
    queryset = Students.objects.all()

    # @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    # def my_list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'put'])  # , renderer_classes=[renderers.AdminRenderer])
    def example(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action == "example":
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]


class TeacherViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Teachers.objects.all()
        serializer = TeacherListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Teachers.objects.all()
        teacher = get_object_or_404(queryset, pk=pk)
        serializer = TeacherDetailSerializer(teacher)
        # print(self.retrieve.u)
        return Response(serializer.data)


class TeacherReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherListSerializer


class TeacherModelViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherListSerializer
    queryset = Teachers.objects.all()

    # @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    # def my_list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'put'])  # , renderer_classes=[renderers.AdminRenderer])
    def example(self, request, *args, **kwargs):
        teacher = self.get_object()
        serializer = TeacherDetailSerializer(teacher)
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action == "example":
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]


class DepartmentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Department.objects.all()
        serializer = TeacherListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentDetailSerializer(department)
        # print(self.retrieve.u)
        return Response(serializer.data)


class DepartmentReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer


class DepartmentModelViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentListSerializer
    queryset = Department.objects.all()

    # @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    # def my_list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'put'])  # , renderer_classes=[renderers.AdminRenderer])
    def example(self, request, *args, **kwargs):
        department = self.get_object()
        serializer = DepartmentDetailSerializer(department)
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action == "example":
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]
