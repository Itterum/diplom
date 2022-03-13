from django.contrib import admin

from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

from .models import Discipline


@admin.register(Discipline)
class DisciplineAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Discipline, {
        'department': 'department',
    })

    readonly_fields=('id',)
