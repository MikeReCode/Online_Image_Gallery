from django.contrib import admin
from .models import Image
# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('image', 'date', 'owner')


admin.site.register(Image, MeetupAdmin)