from django.db import models

# Create your models here.

class Shelf(models.Model):

    name    = models.CharField(max_length=100)
    storey  = models.CharField(max_length=100, blank=True)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name + " / " + self.storey