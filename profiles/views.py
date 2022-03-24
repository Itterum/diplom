from rest_framework import status
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from profiles.serializers import ProfileSerializer

from .models import Profile
from .permissions import IsOwnerOrReadOnly


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

class PeoplesViewSet(viewsets.ModelViewSet):
    """Листинг новостей"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]  # проверка на авторизированого юзера

    filter_fields = ['department']  # фильтрация по полям ?department="значение"
    search_fields = ['name']  # поиск по полям ?search="значение"
    ordering_fields = ['name']  # сортировка по полям ?ordering="значение"

    # пример совместного использования ?department="значение"&search="значение"&?ordering="значение"
