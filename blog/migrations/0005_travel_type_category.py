# Generated by Django 2.2.1 on 2019-06-04 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_travel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='type_category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
