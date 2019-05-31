from django.db import models

# Create your models here.

class Blogger(models.Model):
    bid = models.CharField(max_length=20)
    bname = models .CharField(max_length=100)
    bemail = models.EmailField()
    bconatact =models.CharField(max_length=15)

    class Meta:
        db_table = 'blogger'
