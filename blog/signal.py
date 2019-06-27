from django.db.models.signals import post_save
from django.dispatch import receiver
from mysite.blog.models import Author


@receiver(post_save, sender=Author)
def display_welcome_message(sender, instance, first_name, **kwargs):
    if first_name:
        return "Welcome to this blog {0}".format(first_name)

