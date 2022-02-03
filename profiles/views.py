from .models import Profile

from django.http import JsonResponse
from rest_framework import mixins, viewsets, permissions

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from profiles.permissions import (
    IsOwnerOrReadOnly, IsAdminUserOrReadOnly, IsSameUserAllowEditionOrReadOnly
)

from profiles.serializers import ProfileSerializer
# from .models import Student


class TokenObtainView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        custom_response = {
            'token': token.key,
            'user': {
                'id': user.id,
                'full_name': user.full_name,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'gender': user.gender,
                'birth_date': user.birth_date,
                'phone_number': user.phone_number,
                'address': user.address,
                'photo': f'/media/{str(user.photo)}',
                'email': user.email,
                'is_active': user.is_active,
                'user_type': user.user_type,
                'is_superuser': user.is_superuser,
                'phone_number_parents': user.phone_number_parents,
                'educ_type': user.educ_type,
                'position': user.position,
                'qualification': user.qualification,
                'department': user.department,
                'group': user.group
            }
        }
        return JsonResponse(custom_response)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
