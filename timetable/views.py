from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Timetable
from .serializers import TimetableSerializer

from .filters import TimetableFilter


class TimetableViewSet(viewsets.ModelViewSet):
    serializer_class = TimetableSerializer
    queryset = Timetable.objects.all()

    filterset_class = TimetableFilter

    def list(self, request, *args, **kwargs):
        # TODO: improve the check for parameters
        if not request.query_params:
            return Response({'error': 'pass at least one parameter'},
                            status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)
