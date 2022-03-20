from rest_framework import viewsets
from .models import Group
from .serializers import GroupsListSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Листинг групп"""
    serializer_class = GroupsListSerializer
    queryset = Group.objects.all()
