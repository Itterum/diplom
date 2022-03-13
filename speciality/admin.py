from django.contrib import admin

from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

from .models import Speciality


@admin.register(Speciality)
class AdminSpeciality(AjaxSelectAdmin):
    form = make_ajax_form(Speciality, {
        'department': 'department',
    })
