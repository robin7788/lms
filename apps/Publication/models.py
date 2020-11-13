from django.db import models

# Create your models here.
class Publication(models.Model):

    name    = models.CharField(max_length=100)
    logo    = models.ImageField(upload_to='images/publication', blank=True)
    address = models.TextField(blank=True)
    phone   = models.CharField(max_length=25, blank=True)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)