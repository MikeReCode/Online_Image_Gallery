from django.db import models
from django.conf import settings
from exiffield.fields import ExifField
from exiffield.getters import exifgetter
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def getcurrentusername(instance, filename):

    # https://stackoverflow.com/questions/71438192/uploading-file-by-filefield-returns-bad-request-suspiciousfileoperation
    # print( f"{settings.MEDIA_ROOT}/{instance.owner.id}/{filename}", "**********************************************")
    return f"{instance.owner.id}/{filename}"


class Image(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to=getcurrentusername, max_length=500)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(210, 210)], format='JPEG', options={'quality': 60})
    date = models.CharField(editable=False, max_length=100, null=True)
    exif = ExifField(source='image', denormalized_fields={'date': exifgetter('CreateDate'), }, )

    def __str__(self):
        return "image**"

    def delete(self, *args, **kwargs):

        self.image.delete()
        super().delete(*args, **kwargs)
