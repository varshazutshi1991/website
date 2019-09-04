# Generated by Django 2.2.4 on 2019-09-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_nluuseranalyticstesting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(blank=True, max_length=100, null=True)),
                ('short_description', models.CharField(blank=True, max_length=200, null=True)),
                ('blog_content', models.TextField(blank=True, null=True)),
                ('your_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('about_yourself', models.TextField(blank=True, null=True)),
                ('facebook_profile_link', models.URLField(blank=True, max_length=150, unique=True)),
            ],
        ),
    ]