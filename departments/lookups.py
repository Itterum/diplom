from ajax_select import register, LookupChannel
from .models import Department


@register('department')
class SpecialityLookup(LookupChannel):

    model = Department

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')