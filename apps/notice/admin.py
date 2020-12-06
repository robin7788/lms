from django.contrib import admin
from .models import Notice


# make status active
def make_active(modeladmin, request, queryset):
    queryset.update(status=1)

# make status active
def make_deactive(modeladmin, request, queryset):
    queryset.update(status=0)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("name", "expired_on", "status", "created_at")
    search_fields = ("name", )
    actions = [make_active, make_deactive]
    actions_on_top = False
    actions_on_bottom = True