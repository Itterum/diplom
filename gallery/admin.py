from django.contrib import admin

from .models import Gallery, Photo


class PhotoAdmin(admin.TabularInline):
    model = Photo


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        PhotoAdmin,
    ]
