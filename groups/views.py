from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from profiles.models import Profile

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

    @action(detail=False, methods=['PATH', 'PUT'], url_path='change-session')
    def change_session(self, request):
        groups = Group.objects.filter(id__in=request.data['groups'])
        session = request.data['session']

        groups.update(is_session=session)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['PUT', 'PATCH'], url_path='user-binding')
    def user_binding(self, request):
        users = Profile.objects.filter(id__in=request.data['users'])
        group = request.data['group']

        users.update(group=group)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
