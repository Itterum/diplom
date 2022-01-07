from django.contrib import admin

# Register your models here.
from .models import Students, Teachers, Department, Groups


admin.site.register(Students)
admin.site.register(Department)
admin.site.register(Teachers)
admin.site.register(Groups)
