from django.contrib import admin

from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

from .models import Department


@admin.register(Department)
class DepartmentAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Department, {
        'manager_department': 'profile',
    })

    readonly_fields=('id',)
