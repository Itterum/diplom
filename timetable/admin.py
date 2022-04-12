from django.contrib import admin
from .models import Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

    list_filter = ('session', 'visit')
