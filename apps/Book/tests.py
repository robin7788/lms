from django.test import TestCase
from django.forms.models import model_to_dict
from django.db import IntegrityError
from django.conf import settings
from .models import Author, Publication, Genre, Category, Type, Shelf, Book

class TestCaseAuthor(TestCase):
    def setUp(self):
        Author.objects.create(
            name='Author 1',
            desc='Desc 1'
        )
        Author.objects.create(
            name='Author 2',
            desc='Desc 2'
        )
    """
    -------------------------------------------------------------------------------------------------------------------
    Test the creation of a Author model using a manual data
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_create(self):
        self.assertEqual(Author.objects.count(), 2)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Author server are counted. 
    It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    Note: excluded columns via admin will not get counted in model_to_dict like created_at and updated_at 
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_count(self):
        author = Author.objects.first()
        author_dict = model_to_dict(author)
        self.assertEqual(len(author_dict.keys()), 5)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Author server have content. This test will break if an attributes name is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_content(self):
        author = Author.objects.first()
        self.assertIsNotNone(author.id)
        self.assertIsNotNone(author.name)
        self.assertIsNotNone(author.img)
        self.assertIsNotNone(author.desc)
        self.assertIsNotNone(author.status)
        self.assertIsNotNone(author.created_at)
        self.assertIsNotNone(author.updated_at)


class TestCaseCategory(TestCase):
    def setUp(self):
        Category.objects.create(
            name='Category 1',
            desc='Desc 1'
        )
        Category.objects.create(
            name='Category 2',
            desc='Desc 2'
        )

    """
    -------------------------------------------------------------------------------------------------------------------
    Test the creation of a Category model using manual data
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_create(self):
        self.assertEqual(Category.objects.count(), 2)

    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Category server are counted. It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_count(self):
        category = Category.objects.first()
        category_dict = model_to_dict(category)
        self.assertEqual(len(category_dict.keys()), 4)

    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Category server have content. This test will break if an attributes name is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_content(self):
        category = Category.objects.first()
        self.assertIsNotNone(category.id)
        self.assertIsNotNone(category.name)
        self.assertIsNotNone(category.desc)
        self.assertIsNotNone(category.status)
        self.assertIsNotNone(category.created_at)
        self.assertIsNotNone(category.updated_at)


class TestCaseType(TestCase):
    def setUp(self):
        Type.objects.create(
            name='Type 1',
            desc='Desc 1'
        )
        Type.objects.create(
            name='Type 2',
            desc='Desc 2'
        )

    """
    -------------------------------------------------------------------------------------------------------------------
    Test the creation of a Type model using manual data
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_create(self):
        self.assertEqual(Type.objects.count(), 2)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Type server are counted. It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_count(self):
        type = Type.objects.first()
        type_dict = model_to_dict(type)
        self.assertEqual(len(type_dict.keys()), 4)



    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Type server have content. This test will break if an attributes name is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_content(self):
        type = Type.objects.first()
        self.assertIsNotNone(type.id)
        self.assertIsNotNone(type.name)
        self.assertIsNotNone(type.desc)
        self.assertIsNotNone(type.status)
        self.assertIsNotNone(type.created_at)
        self.assertIsNotNone(type.updated_at)


class TestCaseGenre(TestCase):
    def setUp(self):
        Genre.objects.create(
            name='Genre 1',
            desc='Desc 1'
        )
        Genre.objects.create(
            name='Genre 2',
            desc='Desc 2'
        )

    """
    -------------------------------------------------------------------------------------------------------------------
    Test the creation of a Genre model using manual data
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_create(self):
        self.assertEqual(Genre.objects.count(), 2)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Genre server are counted. It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_count(self):
        genre = Genre.objects.first()
        genre_dict = model_to_dict(genre)
        self.assertEqual(len(genre_dict.keys()), 4)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Genre server have content. This test will break if an attributes name is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_content(self):
        genre = Genre.objects.first()
        self.assertIsNotNone(genre.id)
        self.assertIsNotNone(genre.name)
        self.assertIsNotNone(genre.desc)
        self.assertIsNotNone(genre.status)
        self.assertIsNotNone(genre.created_at)
        self.assertIsNotNone(genre.updated_at)


class TestCasePublication(TestCase):
    def setUp(self):
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
    -------------------------------------------------------------------------------------------------------------------
    Test the creation of a Publication model using manual data
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_create(self):
        self.assertEqual(Publication.objects.count(), 2)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Publication server are counted. It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_count(self):
        publication = Publication.objects.first()
        publication_dict = model_to_dict(publication)
        self.assertEqual(len(publication_dict.keys()), 7)

    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Publication server have content. This test will break if an attributes name is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_content(self):
        publication = Publication.objects.first()
        self.assertIsNotNone(publication.id)
        self.assertIsNotNone(publication.name)
        self.assertIsNotNone(publication.img)
        self.assertIsNotNone(publication.address)
        self.assertIsNotNone(publication.phone)
        self.assertIsNotNone(publication.desc)
        self.assertIsNotNone(publication.status)
        self.assertIsNotNone(publication.created_at)
        self.assertIsNotNone(publication.updated_at)


class TestCaseShelf(TestCase):
    def setUp(self):
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
    -------------------------------------------------------------------------------------------------------------------
    Test the creation of a Shelf model using manual data
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_create(self):
        self.assertEqual(Shelf.objects.count(), 2)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Shelf server are counted. It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_count(self):
        shelf = Shelf.objects.first()
        shelf_dict = model_to_dict(shelf)
        self.assertEqual(len(shelf_dict.keys()), 5)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Shelf server have content. This test will break if an attributes name is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_content(self):
        shelf = Shelf.objects.first()
        self.assertIsNotNone(shelf.id)
        self.assertIsNotNone(shelf.name)
        self.assertIsNotNone(shelf.storey)
        self.assertIsNotNone(shelf.desc)
        self.assertIsNotNone(shelf.status)
        self.assertIsNotNone(shelf.created_at)
        self.assertIsNotNone(shelf.updated_at)


class TestCaseBook(TestCase):

    def setUp(self):
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
    -------------------------------------------------------------------------------------------------------------------
    Test the creation of a Book model using a manual data
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_create(self):
        self.assertEqual(Book.objects.count(), 2)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Book server are counted. It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_count(self):
        book = Book.objects.first()
        book_dict = model_to_dict(book)
        self.assertEqual(len(book_dict.keys()), 16)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of Book server have content. This test will break if an attributes name is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_attribute_content(self):
        book = Book.objects.first()
        self.assertIsNotNone(book.id)
        self.assertIsNotNone(book.name)
        self.assertIsNotNone(book.isbn_number)
        self.assertIsNotNone(book.published_year)
        self.assertIsNotNone(book.volume)
        self.assertIsNotNone(book.img)
        self.assertIsNotNone(book.desc)
        self.assertIsNotNone(book.quantity)
        self.assertIsNotNone(book.price)
        self.assertIsNotNone(book.purchase_date)
        self.assertIsNotNone(book.status)
        self.assertIsNotNone(book.created_at)
        self.assertIsNotNone(book.updated_at)

    """
    -------------------------------------------------------------------------------------------------------------------
    Tests attribute isbn_number of model Book to see if the unique constraint works.
    This test should break if the unique attribute is changed.
    -------------------------------------------------------------------------------------------------------------------
    """
    def test_isbn_number_is_unique(self):
        book = Book.objects.filter(name='Book 1').first()
        book_02 = Book.objects.filter(name='Book 2').first()
        book_02.isbn_number = book.isbn_number
        try:
            book_02.save()
            self.fail('Test should have raised and integrity error')
        except IntegrityError as e:
            self.assertEqual(str(e), '') #This line should show duplicate entry error