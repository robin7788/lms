from django.contrib import admin
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile

# Register your models here.

from .models import Author, Publication, Category, Type, Genre, Shelf

# admin.site.register(Author)
# admin.site.register(Publication)
# admin.site.register(Category)
# admin.site.register(Type)
# admin.site.register(Genre)
# admin.site.register(Shelf)

class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60 }
def cached_admin_thumb(instance):
    if instance.img:
        # `image` is the name of the image field on the model
        cached = ImageCacheFile(AdminThumbnailSpec(instance.img))
        # only generates the first time, subsequent calls use cache
        cached.generate()
        return cached
    return "";


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "image_display", "status", "created_at")
    image_display = AdminThumbnail(image_field=cached_admin_thumb)
    image_display.short_description = 'Image'

    readonly_fields = ['image_display']  # this is for the change form

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("name", 'image_display', "phone", "status", "created_at")
    image_display = AdminThumbnail(image_field=cached_admin_thumb)
    image_display.short_description = 'Image'

    readonly_fields = ['image_display']  # this is for the change form


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")

@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ("name", 'storey', "status", "created_at")