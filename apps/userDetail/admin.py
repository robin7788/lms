from django.contrib import admin
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form
from .models import UserDetail, IssueBookDetail
import datetime
from django.utils.html import format_html
from django.core.mail import EmailMultiAlternatives
from django.urls import path
from django.urls import reverse
from django.http import JsonResponse




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
    list_display = ("user", "book", "get_book_isbn", 'get_date_formatted', "return_status", "sendmail_actions")
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
        return_date_val = ""
        if obj:
            return_date_val = obj.return_date.strftime('%b. %d, %Y')
            if obj.return_status == 0:
                if obj.return_date.date() < datetime.date.today():
                    return_date_val = format_html('<span style="color: #cc0033; font-weight: bold;">{0}</span>', return_date_val)
            else:
                return_date_val = format_html('<span style="color: #70bf2b;">{0}</span>', return_date_val)

        return return_date_val

    get_date_formatted.admin_order_field = 'return_date'
    get_date_formatted.short_description = 'Return date'


    """
    --------------------------------------------------------------------------------
    Add new url / route in system to send mail manually to user who have issued book
    --------------------------------------------------------------------------------
    """
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:user_id>/sendmail',
                self.admin_site.admin_view(self.sendmail),
                name='sendmail'
            ),
        ]
        return custom_urls + urls


    """
    ---------------------------------------------------------------------
    Display send mail button while listing user issued book.
    It also shows the number of email sent to user to notify
    ---------------------------------------------------------------------
    """
    def sendmail_actions(self, obj):
        if obj and obj.return_status == 0:
            return format_html(
                str(obj.sent_email) + ' <span> <a class="button sendmailbutton" href="{}" title="Send email"><i class="tim-icons icon-send"></i></a>&nbsp;</span>',
                reverse('admin:sendmail', args=[obj.pk]),
            )
        return ''

    sendmail_actions.short_description = 'Sent / Send mail'
    sendmail_actions.allow_tags = True


    """
    ---------------------------------------------------------------------
    It sends mail to selected user in specific html format 
    ---------------------------------------------------------------------
    """
    def sendmail(self, request, user_id, *args, **kwargs):
        message = ''
        status = 200
        email_no = 0
        try:
            issue_book = IssueBookDetail.objects.get(pk=user_id)
            if issue_book:
                message = 'Email successfully sent to ' + issue_book.user.name
                issue_book.sent_email += 1
                issue_book.save()
                email_no = issue_book.sent_email

                subject = 'UEL | LMS book returning notification'
                from_email = 'info@lms.merobin.com'
                to_email = [issue_book.user.email]
                text_content = 'This is an important message.'
                html_content = 'Dear ' + issue_book.user.name + ',' +\
                               '<br /> It shows that you have issued the book "' + issue_book.book.name + \
                               '" on '+ issue_book.issue_date.strftime('%b. %d, %Y') + \
                               ' and your returning date is on ' + \
                               issue_book.return_date.strftime('%b. %d, %Y') + \
                               '. If you failed to return on time, then you will get charged a fine as per ' + \
                               'institution rule.<br /> Yours,<br/>UEL | LMS'

                msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

        except UserDetail.DoesNotExist:
            message = 'Error while sending mail. Please try after sometime.'
            status = 404

        data = {
            'message': message,
            'status': status,
            'email_no': email_no,
            'panel': 'text-left',
            'notify': 'right',
        }
        return JsonResponse(data)
        # return JsonResponse(data, status=status)

    """
    ---------------------------------------------------------------------
    It loads a script in userDetail app in order to show or hide specific
    area. Here, show or hide fine option is toggled with this script
    ---------------------------------------------------------------------
    """
    class Media:
        js = ('/static/admin/js/hide_attribute.js',)


