from rest_framework import status

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from profiles.serializers import ProfileSerializer

from .models import Profile


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
