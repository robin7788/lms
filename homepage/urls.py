from django.urls import path
from django.conf.urls import url

from . import views
from .views import BookNameListJson

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('book_detail/<book_id>', views.book_detail, name='book_detail'),
    url(r'^name_data/$', BookNameListJson.as_view(), name="name_list_json"),
]