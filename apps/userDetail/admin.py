from django.contrib import admin
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form
from .models import UserDetail, IssueBookDetail

# make status active
def make_active(modeladmin, request, queryset):
    queryset.update(status=1)

# make status active
def make_deactive(modeladmin, request, queryset):
    queryset.update(status=0)

# make status active
def make_return_active(modeladmin, request, queryset):
    queryset.update(return_status=1)

# make status active
def make_return_deactive(modeladmin, request, queryset):
    queryset.update(return_status=0)


@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'phone', "created_by", "status")
    search_fields = ("name", 'email', 'phone', 'address')
    actions = [make_active, make_deactive]
    exclude = ['created_by',]
    actions_on_top = False
    actions_on_bottom = True

@admin.register(IssueBookDetail)
class IssueBookDetailAdmin(AjaxSelectAdmin):

    fields = (
        "book",
        "user",
        "issue_date",
        "return_date",
        "return_status"
    )
    list_display = ("user", "book", 'issue_date', 'return_date', "return_status")
    search_fields = ("book",)
    exclude = ['issued_by',]
    actions = [make_return_active, make_return_deactive]
    actions_on_top = False
    actions_on_bottom = True

    form = make_ajax_form(IssueBookDetail, {
        'book' : 'book',
        'user'  : 'user'
    })

# SELECT id,
# 	CASE
#         WHEN quantity >= (SELECT COUNT(book_id) as quantity
#                           FROM userdetail_issuebookdetail
#                           WHERE return_status=0 GROUP BY book_id)
#         THEN 1 ELSE 0
#         END as qty
# FROM `book_book`