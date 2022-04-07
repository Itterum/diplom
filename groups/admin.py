from django.contrib import admin

from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

from .models import Group


@admin.register(Group)
class GroupAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Group, {
        'headmen': 'profile',
        'curator': 'profile',
        'spec': 'speciality'
    })

    readonly_fields = ('id',)
