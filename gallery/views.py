from rest_framework.viewsets import ModelViewSet

from .models import Photo
from .serializers import PhotoSerializer

from .filters import GalleryFilter


class GalleryViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    filterset_class = GalleryFilter
    serializer_class = PhotoSerializer
