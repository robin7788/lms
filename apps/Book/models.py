from django.db import models
from django.contrib.auth.models import User
# from apps.userDetail.current_user import get_current_user
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

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


class Book(models.Model):
    name            = models.CharField(max_length=100)
    isbn_number     = models.CharField(max_length=100, blank=True, unique=True)
    published_year  = models.DateField(auto_now_add=True)
    volume          = models.CharField(max_length=100, blank=True)
    author          = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    publication     = models.ForeignKey(Publication, null=True, on_delete=models.SET_NULL)
    genre           = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.SET_NULL)
    type            = models.ForeignKey(Type, blank=True, null=True, on_delete=models.SET_NULL)
    category        = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    shelf           = models.ForeignKey(Shelf, blank=True, null=True, on_delete=models.SET_NULL)
    img             = models.ImageField(upload_to='images/author', blank=True)
    # Creating thumb image using imagekit
    img_thumb       = ImageSpecField(source='img',
                                      processors=[ResizeToFill(250, 250)],
                                      format='JPEG',
                                      options={'quality': 60})
    desc            = models.TextField(blank=True)
    quantity        = models.PositiveIntegerField(default=0)
    price           = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    purchase_date   = models.DateField(auto_now_add=True)
    status          = models.BooleanField(default=True)
    # created_by      = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, editable=False, default=get_current_user)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # change app name object to actual data name
    def __str__(self):
        return self.name

    """
    ---------------------------------------------------------------------
    Calculates the available books in the library and returns "Yes" 
    if book is available else "No" 
    ---------------------------------------------------------------------
    """
    @property
    def available_quantity(self):
        from apps.userDetail.models import IssueBookDetail
        count_value = self.quantity - IssueBookDetail.objects.filter(return_status= 0).filter(book_id=self.id).count()
        if count_value > 0:
            return 'Yes'
        return 'No'