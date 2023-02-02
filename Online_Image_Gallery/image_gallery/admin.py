from django.contrib import admin
from .models import Image


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'date', 'owner')


admin.site.register(Image, GalleryAdmin)