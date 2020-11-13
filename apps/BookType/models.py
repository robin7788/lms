from django.db import models

# Create your models here.

class BookType(models.Model):

    name    = models.CharField(max_length=100)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name

