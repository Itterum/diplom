from rest_framework import viewsets
from .models import Group
from .serializers import GroupsListSerializer, GroupDetailSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Листинг групп"""
    queryset = Group.objects.all()
    serializer_class = GroupsListSerializer
