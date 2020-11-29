from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.userDetail.current_user import get_current_user
from apps.Book.models import Book
import datetime
from django.utils.html import format_html


class UserDetail(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name 			= models.CharField(max_length=150)
    email 			= models.EmailField(max_length=100, blank=True)
    phone 			= models.CharField(max_length=30, blank=True)
    address 		= models.TextField(blank=True)
    status 			= models.BooleanField(default=True)
    created_by      = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, editable=False, default=get_current_user)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
	
    # change app name object to actual data name
    def __str__(self):
        return self.name
	
class IssueBookDetail(models.Model):
    book            = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date      = models.DateTimeField(auto_now_add=False)
    return_date     = models.DateTimeField(auto_now=False)
    return_status   = models.BooleanField(default=False)
    user            = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    fine            = models.DecimalField(default=0,max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    fine_note       = models.TextField(blank=True)
    created_by      = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, editable=False, default=get_current_user)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.name

    """
    ---------------------------------------------------------------------
    Change colors of returning date to red if returning date exceed 
    today's date
    ---------------------------------------------------------------------
    """
    def returning_date(self):
        return_date_val = self.return_date.strftime('%b. %d, %Y')
        if self.return_status == 0:
            if self.return_date.date() < datetime.date.today():
                return_date_val = format_html('<span style="color: #cc0033; font-weight: bold;">{0}</span>', return_date_val)
        else:
            return_date_val = format_html('<span style="color: #70bf2b;">{0}</span>', return_date_val)

        return return_date_val

    returning_date.allow_tags = True
        

