from django.urls import path
from django.conf.urls import url

from apps.userDetail import views

urlpatterns = [
    path('sendmail/', views.sendmail, name='sendmail'),
]