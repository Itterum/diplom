from ajax_select import register, LookupChannel
from .models import Speciality


@register('speciality')
class SpecialityLookup(LookupChannel):

    model = Speciality

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')