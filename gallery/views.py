from rest_framework import status

from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from management.permissions import IsManagerOrReadOnly

from .models import Photo
from .serializers import GalleryCreateSerializer, GallerySerializer, PhotoCreateSerializer

from .filters import GalleryFilter


class GalleryViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    filterset_class = GalleryFilter

    serializer_classes = {
        'partial_update': GalleryCreateSerializer,
        'update': GalleryCreateSerializer,
        'create': GalleryCreateSerializer
    }

    default_serializer_class = GallerySerializer

    permission_classes = [IsManagerOrReadOnly]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)

    def create(self, request, *args, **kwargs):
        photos = request.data.pop('photos')

        gallery = GalleryCreateSerializer(data=request.data)
        gallery.is_valid(raise_exception=True)
        object_gallery = gallery.save()

        # TODO: delete hardcode
        for photo in photos:
            object_photo = PhotoCreateSerializer(data={'image': photo,
                                                 'gallery': object_gallery.id})
            object_photo.is_valid(raise_exception=True)
            object_photo.save()

        return Response(GallerySerializer(object_gallery).data, status=status.HTTP_201_CREATED)
