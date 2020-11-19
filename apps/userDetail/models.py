from django.db import models
from django.contrib.auth.models import User
from apps.userDetail.current_user import get_current_user
from apps.Book.models import Book


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
    created_by      = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, editable=False, default=get_current_user)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.name
        

