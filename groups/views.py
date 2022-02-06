from rest_framework import viewsets
from .models import Group
from .serializers import GroupsListSerializer


# Create your views here.
class GroupsViewSet(viewsets.ModelViewSet):
    """Листинг групп"""
    serializer_class = GroupsListSerializer
    queryset = Group.objects.all()
