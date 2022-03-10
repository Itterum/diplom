from django.contrib import admin
from .models import Discipline


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

