import string

from random import randint
from pytz import timezone

from django.conf import settings

from factory import Iterator
from factory import LazyAttribute
from factory import SubFactory
from factory import lazy_attribute
from factory.django import DjangoModelFactory, FileField
from factory.fuzzy import FuzzyText, FuzzyInteger
from faker import Factory as FakerFactory
from .models import Author, Publication, Genre, Category, Type, Shelf, Book

faker = FakerFactory.create()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    #img = ImageField We do not support this field type
    desc = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    status = Iterator([True, False])
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    desc = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    status = Iterator([True, False])
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))

class TypeFactory(DjangoModelFactory):
    class Meta:
        model = Type

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    desc = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    status = Iterator([True, False])
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))

class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    desc = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    status = Iterator([True, False])
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))

class PublicationFactory(DjangoModelFactory):
    class Meta:
        model = Publication

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    #img = ImageField We do not support this field type
    address = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    phone = LazyAttribute(lambda x: faker.text(max_nb_chars=25))
    desc = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    status = Iterator([True, False])
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))

class ShelfFactory(DjangoModelFactory):
    class Meta:
        model = Shelf

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    storey = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    desc = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    status = Iterator([True, False])
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))

class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    isbn_number = LazyAttribute(lambda x: FuzzyText(length=100, chars=string.digits).fuzz())
    published_year = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    volume = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    author = SubFactory(AuthorFactory)
    publication = SubFactory(PublicationFactory)
    genre = SubFactory(GenreFactory)
    type = SubFactory(TypeFactory)
    category = SubFactory(CategoryFactory)
    shelf = SubFactory(ShelfFactory)
    #img = ImageField We do not support this field type
    desc = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    #quantity = PositiveIntegerField We do not support this field type
    price = LazyAttribute(lambda x: faker.pydecimal(left_digits=8, right_digits=2, positive=True))
    purchase_date = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    status = Iterator([True, False])
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))