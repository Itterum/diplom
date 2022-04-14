from django.http import QueryDict

from rest_framework import status
from rest_framework import viewsets

from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from djoser.views import UserViewSet

from profiles.managers import CustomUserManager
from profiles.serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer,
    ProfileCreateSerializer
)
from profiles.filters import ProfileFilter

from utils.model_utils import generate_short_id
from mixins.views import DeleteSetMixin
from management.permissions import IsManagerOrReadOnly

from .models import Profile
from .permissions import IsOwnerOrReadOnly
from .email import send_login_details_to_email


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


class CustomUserViewSet(UserViewSet):
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True

        serializer = ProfileCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        username_email = email.split('@')[0]
        new_username = f'{username_email}{generate_short_id()}'
        password = CustomUserManager().make_random_password()

        request.data.update({'username': new_username})
        request.data.update({'password': password})

        response = super().create(request, *args, **kwargs)

        send_login_details_to_email(new_username, password, email)

        return response
