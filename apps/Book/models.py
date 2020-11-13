from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name    = models.CharField(max_length=100)
    img     = models.ImageField(upload_to='images/author', blank=True)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name

    def image_tag(self):
        return '<img src="' + self.img +'" />'

    class Meta:
        verbose_name_plural = "Author"

class Category(models.Model):

    name    = models.CharField(max_length=100)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name

class Type(models.Model):

    name    = models.CharField(max_length=100)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name

class Genre(models.Model):

    name    = models.CharField(max_length=100)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name

class Publication(models.Model):

    name    = models.CharField(max_length=100)
    img    = models.ImageField(upload_to='images/publication', blank=True)
    address = models.TextField(blank=True)
    phone   = models.CharField(max_length=25, blank=True)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name

class Shelf(models.Model):

    name    = models.CharField(max_length=100)
    storey  = models.CharField(max_length=100, blank=True)
    desc    = models.TextField(blank=True)
    status  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name + " / " + self.storey
