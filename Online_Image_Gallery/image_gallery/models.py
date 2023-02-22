from django.db import models
from django.conf import settings
from exiffield.fields import ExifField
from exiffield.getters import exifgetter
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import os
import shutil


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


# This code is used to delete cache and media folders for a particular user when that user is deleted
User = get_user_model()
@receiver(pre_delete, sender=User)
def delete_user_images(sender, instance, **kwargs):
    folder_path = f"{settings.MEDIA_ROOT}/{instance.id}"
    cache_folder_path = f"{settings.MEDIA_ROOT}/CACHE/images/{instance.id}"

    # permanently delete the media folder for that particular user and all its content 
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)

    # permanently delete the cache media folder for that particular user and all its content 
    if os.path.isdir(cache_folder_path):
        shutil.rmtree(cache_folder_path)

    # ** permanently delete only the media images and cache images but folder is not deleted **
    # user_images = Image.objects.filter(owner=instance)
    # for image in user_images:
    #     if os.path.isfile(image.image.path):
    #         os.remove(image.image.path)
    #     if os.path.isfile(image.thumbnail.path):
    #         os.remove(image.thumbnail.path)
    #     image.delete()