from django.contrib import admin
from .models import UserDetail, IssueBookDetail

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'phone', "created_by")
    search_fields = ("name", 'email', 'phone', 'address')
    exclude = ['created_by',]

@admin.register(IssueBookDetail)
class IssueBookDetailAdmin(admin.ModelAdmin):
    list_display = ("book", 'issue_date', 'return_date', "return_status")
    search_fields = ("book",)
    exclude = ['issued_by',]
    actions_on_top = False
    actions_on_bottom = True
