from django.shortcuts import render
from apps.Book.models import Book, Category, Publication
from apps.notice.models import Notice

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from django.utils.html import format_html
from datetime import datetime



"""
---------------------------------------------------------------------
 Display Home page with some book details and search features
 Index page is displayed by passing book categories and publications
---------------------------------------------------------------------
"""
def index(request):
    books = Book.objects.filter(status=1).order_by("?")[:6]
    book_categories = Category.objects.filter(status=1)
    book_publications = Publication.objects.filter(status=1)
    notices = Notice.objects.filter(expired_on__gte=datetime.now()).\
        filter(status=True).\
        order_by('-expired_on').\
        all()[:12]
    return  render(request, "index.html", {
        'books': books,
        'bookCategories': book_categories,
        'bookPublications': book_publications,
        'notices': notices,
    })


"""
---------------------------------------------------------------------
Display book list page with some basic parameters
---------------------------------------------------------------------
"""
def about(request):
    return render(request, 'about.html')


"""
---------------------------------------------------------------------
Display book list page with some basic parameters
---------------------------------------------------------------------
"""
def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id, status=1)
    except Book.DoesNotExist:
        book = None
    return render(request, 'book_detail.html', {
        'book': book
    })


"""
---------------------------------------------------------------------
Code to show book list for ajax search in datatables
---------------------------------------------------------------------
"""

class BookNameListJson(BaseDatatableView):
    model = Book
    columns = ['name', 'available_quantity', 'author', 'category', 'publication']
    order_columns = ['name', '', '', '', '']


    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'name':
            name = format_html('<a href="/book_detail/'+ str(row.pk) + '">' + row.name + '</a>')
            # name = format_html('<a href="/book_detail/' + str(row.pk) + '">' + row.name + '</a>')
            # escape HTML for security reasons
            return name
        else:
            return super(BookNameListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)
        category = self.request.GET.get('sSearch_1', None)
        publication = self.request.GET.get('sSearch_2', None)

        if sSearch:
            qs = qs.filter(Q(name__istartswith=sSearch) | Q(author__name__istartswith=sSearch))
        if category:
            qs = qs.filter(category__in=category)

        if publication:
            qs = qs.filter(publication__in=publication)

        return qs


"""
---------------------------------------------------------------------
Display book list page with some basic parameters
---------------------------------------------------------------------
"""
def search(request):
    search_data = Book()
    search_data.name = request.GET["name"]
    search_data.category_id = request.GET["category"]
    search_data.publication_id = request.GET["publication"]
    book_categories = Category.objects.filter(status=1)
    book_publications = Publication.objects.filter(status=1)

    return render(request, 'search_book.html', {
        'search_data': search_data,
        'bookCategories': book_categories,
        'bookPublications': book_publications
    })


