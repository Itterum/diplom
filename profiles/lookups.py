from ajax_select import register, LookupChannel
from .models import Profile


@register('profile')
class UserLookup(LookupChannel):

    model = Profile

    def get_query(self, q, request):
        return self.model.objects.filter(full_name__icontains=q).order_by('full_name')