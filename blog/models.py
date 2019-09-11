from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class BlogManager(models.Manager):
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(author=True)


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    blog_title = models.CharField(max_length=200)
    blog_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    blog_picture = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    #all_blogs = models.Manager()
    #varsha_blog = BlogManager()


class About(models.Model):
    full_name = models.CharField(max_length=200)
    introduction = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    def __str__(self):
        return self.full_name


class Contribute(models.Model):
    blog_title = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    blog_content = models.TextField(blank=True, null=True)
    your_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    about_yourself = models.TextField(blank=True, null=True)
    facebook_profile_link = models.URLField(max_length=150, unique=True, blank=True)


class UserComment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]


class User(AbstractUser):
    is_intern = models.BooleanField(default=True)





