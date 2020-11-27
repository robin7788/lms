from django.shortcuts import render
from apps.Book.models import Book, Category, Publication

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

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
    return  render(request, "index.html", {
        'books': books,
        'bookCategories': book_categories,
        'bookPublications': book_publications
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