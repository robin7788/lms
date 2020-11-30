from django.test import TestCase
from django.contrib.auth.models import User
from apps.Book.models import Book, Author, Category, Type, Genre, Publication, Shelf

"""
------------------------------------------------------------------------------------------------
Test case for Book app
------------------------------------------------------------------------------------------------
"""
class BookTestCase(TestCase):

    def setUp(self):
        self.test_author_add()
        self.test_category_add()
        self.test_type_add()
        self.test_genre_add()
        self.test_publication_add()
        self.test_shelf_add()

    """
    Add two Authors; Author 1 and Author 2
    """
    def test_author_add(self):
        Author.objects.create(
            name='Author 1',
            desc='Desc 1'
        )
        Author.objects.create(
            name='Author 2',
            desc='Desc 2'
        )
    """
    Add two Categories; Category 1 and Category 2
    """
    def test_category_add(self):
        Category.objects.create(
            name='Category 1',
            desc='Desc 1'
        )
        Category.objects.create(
            name='Category 2',
            desc='Desc 2'
        )
    """
    Add two Types; Type 1 and Type 2
    """
    def test_type_add(self):
        Type.objects.create(
            name='Type 1',
            desc='Desc 1'
        )
        Type.objects.create(
            name='Type 2',
            desc='Desc 2'
        )
    """
    Add two Genres; Genre 1 and Genre 2
    """
    def test_genre_add(self):
        Genre.objects.create(
            name='Genre 1',
            desc='Desc 1'
        )
        Genre.objects.create(
            name='Genre 2',
            desc='Desc 2'
        )
    """
    Add two Publications; Publication 1 and Publication 2
    """
    def test_publication_add(self):
        Publication.objects.create(
            name='Publication 1',
            address='Publication 1 Address',
            desc='Desc 1'
        )
        Publication.objects.create(
            name='Publication 2',
            address='Publication 2 Address',
            desc='Desc 2'
        )

    """
    Add two Shelfs; Shelf 1 and Shelf 2
    """
    def test_shelf_add(self):
        Shelf.objects.create(
            name='Shelf 1',
            storey='1A',
            desc='Desc 1'
        )
        Shelf.objects.create(
            name='Shelf 2',
            storey='2A',
            desc='Desc 2'
        )


    """
    Add two books; Book 1 and book 2
    """
    def test_book_add(self):
        try:
            author = Author.objects.first()
            category = Category.objects.first()
            type = Type.objects.first()
            genre = Genre.objects.first()
            publication = Publication.objects.first()
            shelf = Shelf.objects.first()
            Book.objects.create(
                name='Book 1',
                author=author,
                category=category,
                type=type,
                genre=genre,
                publication=publication,
                shelf=shelf,
                isbn_number='ISBN1',
                published_year='2020-01-01'
            )
            Book.objects.create(
                name='Book 2',
                author=author,
                category=category,
                type=type,
                genre=genre,
                publication=publication,
                shelf=shelf,
                isbn_number='ISBN2',
                published_year='2019-01-01'
            )
        except Author.DoesNotExist:
            print('Author not found.')
        except Category.DoesNotExist:
            print('Category not found.')
        except Type.DoesNotExist:
            print('Type not found.')
        except Genre.DoesNotExist:
            print('Genre not found.')
        except Publication.DoesNotExist:
            print('Publication not found.')
        except Shelf.DoesNotExist:
            print('Shelf not found.')

    """
    Check whether added users are correctly identified
    """
    def test_book_exists(self):
        try:
            self.test_book_add()
            book1 = Book.objects.filter(isbn_number='ISBN1').first()
            book2 = Book.objects.filter(isbn_number='ISBN2').first()
            self.assertEqual(book1.name, "Book 1")
            self.assertEqual(book2.name, "Book 2")

        except Book.DoesNotExist:
            print('Book not found.')
