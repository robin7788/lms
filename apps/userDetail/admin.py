from django.contrib import admin
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form
from .models import UserDetail, IssueBookDetail
import datetime
from django.utils.html import format_html


from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

"""
---------------------------------------------------------------------
Make selected data status active 
---------------------------------------------------------------------
"""
def make_active(modeladmin, request, queryset):
    queryset.update(status=1)

"""
---------------------------------------------------------------------
Make selected data status not active 
---------------------------------------------------------------------
"""
def make_deactive(modeladmin, request, queryset):
    queryset.update(status=0)

"""
---------------------------------------------------------------------
Make selected data return status active 
---------------------------------------------------------------------
"""
def make_return_active(modeladmin, request, queryset):
    queryset.update(return_status=1)

"""
---------------------------------------------------------------------
Make selected data return status not active 
---------------------------------------------------------------------
"""
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
    list_filter = ("return_status", ('return_date', DateRangeFilter))
    # fields = (
    #     "book",
    #     "user",
    #     "returning_date",
    #     "return_date",
    #     "return_status",
    #     "fine",
    #     "fine_note"
    # )
    fieldsets = (
        (None, {
            'fields': ("book", "user", "issue_date", "return_date",)
        }),
        ("Check if book has been return", {
            'fields': ("return_status",),
            'classes': ("show_hidden_field",)
        }),
        ('Add fine and fine note if problem is seen in book', {
            'classes': ('show_hide_collapse',),
            'fields': ("fine", "fine_note",)
        })

    )
    list_display = ("user", "book", "get_book_isbn", 'get_date_formatted', "return_status")
    search_fields = ("user__name", "book__name", "book__isbn_number",)
    exclude = ['issued_by',]
    actions = [make_return_active, make_return_deactive]
    actions_on_top = False
    actions_on_bottom = True

    form = make_ajax_form(IssueBookDetail, {
        'book' : 'book',
        'user'  : 'user'
    })

    """
    ---------------------------------------------------------------------
    Display ISBN number of book in issue book detail
    ---------------------------------------------------------------------
    """
    def get_book_isbn(self, obj):
        return obj.book.isbn_number
    get_book_isbn.short_description = 'ISBN No'
    get_book_isbn.admin_order_field = 'book__isbn_number'

    """
    ---------------------------------------------------------------------
    Get date only from datetime timestamp
    ---------------------------------------------------------------------
    """
    def get_date_formatted(self, obj):

        if obj:
            if obj.return_date.date() < datetime.date.today():
                return format_html('<span style="color: #cc0033; font-weight: bold;">{0}</span>',
                                   obj.return_date.strftime('%b. %d, %Y'))
            else:
                return obj.return_date.date()
        return ""
    get_date_formatted.admin_order_field = 'return_date'
    get_date_formatted.short_description = 'Return date'

    class Media:
        js = ('/static/admin/js/hide_attribute.js',)
