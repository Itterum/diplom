from rest_framework import status
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from profiles.filters import ProfileFilter

from profiles.serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer
)

from .models import Profile
from .permissions import IsOwnerOrReadOnly
from mixins.views import DeleteSetMixin
from management.permissions import IsManagerOrReadOnly


class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if user_id := request.query_params.get('id'):
            user = Profile.objects.filter(id=user_id).first()
            if not user:
                return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(instance=user)
        else:
            serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)


class ProfileUpdateAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user


class PeoplesViewSet(DeleteSetMixin, viewsets.ModelViewSet):
    queryset = Profile.objects.all()

    serializer_classes = {
        'list': ProfileSerializer,
        'partial_update': ProfileUpdateSerializer,
        'update': ProfileUpdateSerializer,
    }

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsManagerOrReadOnly]

    default_serializer_class = ProfileSerializer

    filterset_class = ProfileFilter
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)
