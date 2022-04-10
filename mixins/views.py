from rest_framework import request

from rest_framework.response import Response


class DeleteSetMixin(object):
    def delete(self, request: request, *args, **kwargs):
        objects = request.data.get('objects', None)
        if objects is None:
            return Response({'error': 'pass field objects'})

        self.get_queryset().filter(id__in=objects).delete()

        return Response({'status': 'ok'})
