from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import StudentGroup, DepartmentDuplicate, TeacherGroup, GroupsDuplicate
from .serializers import (
    StudentGroupListSerializer,
    StudentGroupDetailSerializer,
    DepartmentDuplicateListSerializer,
    DepartmentDuplicateDetailSerializer,
    TeacherGroupListSerializer,
    TeacherGroupDetailSerializer,
    GroupDuplicateListSerializer,
    GroupDuplicateDetailSerializer,
)


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = StudentGroup.objects.all()
        serializer = StudentGroupListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StudentGroup.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentGroupDetailSerializer(student)
        # print(self.retrieve.u)
        return Response(serializer.data)


class StudentsReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer


class StudentsModelViewSet(viewsets.ModelViewSet):
    serializer_class = StudentGroupListSerializer
    queryset = StudentGroup.objects.all()

    # @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    # def my_list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'put'])  # , renderer_classes=[renderers.AdminRenderer])
    def example(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = StudentGroupDetailSerializer(student)
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
        queryset = TeacherGroup.objects.all()
        serializer = TeacherGroupListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TeacherGroup.objects.all()
        teacher = get_object_or_404(queryset, pk=pk)
        serializer = TeacherGroupDetailSerializer(teacher)
        # print(self.retrieve.u)
        return Response(serializer.data)


class TeacherReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = TeacherGroup.objects.all()
    serializer_class = TeacherGroupListSerializer


class TeacherModelViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherGroupListSerializer
    queryset = TeacherGroup.objects.all()

    # @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    # def my_list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'put'])  # , renderer_classes=[renderers.AdminRenderer])
    def example(self, request, *args, **kwargs):
        teacher = self.get_object()
        serializer = TeacherGroupDetailSerializer(teacher)
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
        queryset = DepartmentDuplicate.objects.all()
        serializer = TeacherGroupListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DepartmentDuplicate.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        serializer = DepartmentDuplicateDetailSerializer(department)
        # print(self.retrieve.u)
        return Response(serializer.data)


class DepartmentReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = DepartmentDuplicate.objects.all()
    serializer_class = DepartmentDuplicateListSerializer


class DepartmentModelViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentDuplicateListSerializer
    queryset = DepartmentDuplicate.objects.all()

    # @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    # def my_list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'put'])  # , renderer_classes=[renderers.AdminRenderer])
    def example(self, request, *args, **kwargs):
        department = self.get_object()
        serializer = DepartmentDuplicateDetailSerializer(department)
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action == "example":
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]
