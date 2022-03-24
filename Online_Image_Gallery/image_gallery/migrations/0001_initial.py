# Generated by Django 4.0.3 on 2022-03-24 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import exiffield.fields
import image_gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=image_gallery.models.getcurrentusername)),
                ('date', models.CharField(editable=False, max_length=100, null=True)),
                ('exif', exiffield.fields.ExifField(default={}, editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]