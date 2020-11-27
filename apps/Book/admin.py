from django.contrib import admin
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile
from apps.userDetail.models import IssueBookDetail

# Register your models here.
from admin_black.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

from .models import Book, Author, Publication, Category, Type, Genre, Shelf

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
    return ""

# make status active
def make_active(modeladmin, request, queryset):
    queryset.update(status=1)

# make status active
def make_deactive(modeladmin, request, queryset):
    queryset.update(status=0)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", 'isbn_number', "get_quantity_available", "shelf", "author", "category", "type", "status")
    search_fields = ("name", 'isbn_number', "shelf__name", "author__name", "category__name")
    list_filter = (
            ("shelf", RelatedDropdownFilter),
            ("category", RelatedDropdownFilter),
            ("author", RelatedDropdownFilter),
    )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True

    """
    ---------------------------------------------------------------------
    Get remaining book value in Library
    ---------------------------------------------------------------------
    """
    def get_quantity_available(self, obj):
        return obj.quantity - IssueBookDetail.objects.filter(return_status= 0).filter(book_id=obj.id).count()
    get_quantity_available.short_description = 'Available'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "image_display", "status", "created_at")
    search_fields = ("name", )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True

    image_display = AdminThumbnail(image_field=cached_admin_thumb)
    image_display.short_description = 'Image'

    readonly_fields = ['image_display']  # this is for the change form

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("name", 'image_display', "phone", "status", "created_at")
    search_fields = ("name", )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True

    image_display = AdminThumbnail(image_field=cached_admin_thumb)
    image_display.short_description = 'Image'

    readonly_fields = ['image_display']  # this is for the change form


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")
    search_fields = ("name", )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")
    search_fields = ("name", )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")
    search_fields = ("name", )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True

@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ("name", 'storey', "status", "created_at")
    search_fields = ("name", )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True