from rest_framework import viewsets
from .models import Group
from .serializers import GroupsSerializer, GroupDetailSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Листинг групп"""
    queryset = Group.objects.all()

    serializer_classes = {
        'list': GroupsSerializer,
        'retrieve': GroupDetailSerializer,
    }

    default_serializer_class = GroupsSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)
