from rest_framework import viewsets
from .models import Group
from .serializers import GroupsListSerializer, GroupDetailSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Листинг групп"""
    queryset = Group.objects.all()

    serializer_classes = {
        'list': GroupsListSerializer,
        'retrieve': GroupDetailSerializer,
    }

    default_serializer_class = GroupsListSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)
