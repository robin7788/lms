from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.userDetail.current_user import get_current_user
from apps.Book.models import Book
from django.utils import timezone
from django.utils.html import format_html
from django.db.models.signals import pre_save
from django.dispatch import receiver


class UserDetail(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name 		    = models.CharField(max_length=150)
    email 			= models.EmailField(max_length=100, blank=True, unique=True)
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
    sent_email      = models.PositiveIntegerField(default=0)
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
            if self.return_date.date() < timezone.now().date():
                return_date_val = format_html('<span style="color: #cc0033; font-weight: bold;">{0}</span>', return_date_val)
        else:
            return_date_val = format_html('<span style="color: #70bf2b;">{0}</span>', return_date_val)

        return return_date_val

    returning_date.allow_tags = True
"""
-------------------------------------------------------------------------------------------------------------------
This receiver signal method; adds user as default student in user model and allows them to login and access his data 
This method is called after user detail is added
-------------------------------------------------------------------------------------------------------------------
"""
@receiver(pre_save, sender=UserDetail)
def create_student_when_adding_user(sender, instance, **kwargs):
    last_data = User.objects.order_by('-id')[0]
    username = instance.email.strip().split('@')[0] + str(last_data.id + 1)
    user = User.objects.filter(email=instance.email)
    if user.count() == 0:
        user = User.objects.create_user(username = username, email=instance.email, password=username)
        user.is_staff = True
        group = Group.objects.filter(name='Student')
        if group.count() > 0:
            group.first().user_set.add(user)
    else:
        user = user.first()
    first_name = instance.name.strip().split(' ')[0]
    last_name = ' '.join((instance.name + ' ').split(' ')[1:]).strip()
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    pass

