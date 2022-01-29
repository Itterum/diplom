# from django.db import models
# from rest_framework import generics, permissions, viewsets, mixins
# from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth.models import User
#
# from .models import StudentGroup, TeacherGroup, DepartmentDuplicate, GroupsDuplicate, Profile
# from .serializers import (
#     StudentGroupListSerializer,
#     StudentGroupDetailSerializer,
#     DepartmentDuplicateListSerializer,
#     DepartmentDuplicateDetailSerializer,
#     TeacherGroupListSerializer,
#     TeacherGroupDetailSerializer,
#     GroupDuplicateListSerializer,
#     GroupDuplicateDetailSerializer,
#
#     UserSerializer,
#     ProfileSerializer,
#     ProfileDetailSerializer
# )
# from .service import StudentFilter, DepartmentFilter, TeachersFilter, GroupsFilter
# from unit_group.permissions import (
#     IsOwnerOrReadOnly, IsAdminUserOrReadOnly, IsSameUserAllowEditionOrReadOnly
# )
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsSameUserAllowEditionOrReadOnly,)
#
#
# class ProfileViewSet(mixins.ListModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      viewsets.GenericViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#     """
#     # queryset = Profile.objects.all()
#     # serializer_class = ProfileSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#
#     def get_queryset(self):
#         profiles = Profile.objects.all()
#         return profiles
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ProfileSerializer
#         elif self.action == 'retrieve':
#             return ProfileDetailSerializer
#
#
# class StudentGroupViewSet(viewsets.ReadOnlyModelViewSet):
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = StudentFilter
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         students = StudentGroup.objects.all()
#         return students
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return StudentGroupListSerializer
#         elif self.action == 'retrieve':
#             return StudentGroupDetailSerializer
#
#
# class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = DepartmentFilter
#
#     def get_queryset(self):
#         department = DepartmentDuplicate.objects.all()
#         return department
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return DepartmentDuplicateListSerializer
#         elif self.action == 'retrieve':
#             return DepartmentDuplicateDetailSerializer
#
#
# class TeacherGroupViewSet(viewsets.ReadOnlyModelViewSet):
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = TeachersFilter
#
#     def get_queryset(self):
#         teachers = TeacherGroup.objects.all()
#         return teachers
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return TeacherGroupListSerializer
#         elif self.action == 'retrieve':
#             return TeacherGroupDetailSerializer
#
#
# class GroupViewSet(viewsets.ReadOnlyModelViewSet):
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = GroupsFilter
#
#     def get_queryset(self):
#         groups = GroupsDuplicate.objects.all()
#         return groups
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return GroupDuplicateListSerializer
#         elif self.action == 'retrieve':
#             return GroupDuplicateDetailSerializer
