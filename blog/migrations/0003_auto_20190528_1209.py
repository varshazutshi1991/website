# Generated by Django 2.2.1 on 2019-05-28 12:09

from django.conf import settings
from django.db import migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('blog', '0002_travel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='file',
        ),
        migrations.AddField(
            model_name='travel',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=True, related_name='image_covers', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
