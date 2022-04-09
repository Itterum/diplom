from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Group
from .serializers import GroupsSerializer, GroupDetailSerializer

from .filters import GroupFilter


class GroupsViewSet(viewsets.ModelViewSet):
    """Листинг групп"""
    queryset = Group.objects.all()

    serializer_classes = {
        'list': GroupsSerializer,
        'retrieve': GroupDetailSerializer,
    }

    permission_classes = {
        'update': IsAuthenticated,
    }

    default_serializer_class = GroupsSerializer
    default_permission_class = AllowAny

    filterset_class = GroupFilter

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)

    def get_permissions(self):
        permissions = [self.permission_classes.get(self.action,
                       self.default_permission_class)]
        return [permission() for permission in permissions]
