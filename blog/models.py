from django.db import models
from django.conf import settings
from django.utils import timezone
from filer.fields.image import FilerImageField
from django.db.models.signals import post_save, pre_save

class Travel(models.Model):
    destination = models.CharField(max_length=200)
    destination_title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    destination_description = models.TextField()
    type_category = models.CharField(max_length=200, null=True)
    destination_images = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    #image= FilerImageField(related_name="image_covers", on_delete=True, null=False)


def create_author(sender, instance, **kwargs):
    print("instance")
    print("Authoe is saved")

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

pre_save.connect(receiver=create_author, sender=Author)
post_save.connect(receiver=create_author, sender=Author)


class Food(models.Model):
    food_title = models.CharField(max_length=200)
    food_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    type_category = models.CharField(max_length=200)
    food_picture = models.ImageField(upload_to='images/%Y/%m/%d', null=True)




class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    travel_category = models.ManyToManyField(Travel)
    food_category = models.ManyToManyField(Food)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class About(models.Model):
    full_name = models.CharField(max_length=200)
    introduction = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    def __str__(self):
        return self.full_name




