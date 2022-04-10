from rest_framework import status
from rest_framework.response import Response

from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.serializers import JSONWebTokenSerializer


class AuthManager(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = JSONWebTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            if user.is_manager is False:
                return Response({'error': 'you are not a manager'},
                                status=status.HTTP_400_BAD_REQUEST)

        return super(AuthManager, self).post(request, *args, **kwargs)
