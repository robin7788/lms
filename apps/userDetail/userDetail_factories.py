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
from .models import UserDetail, IssueBookDetail
from .user_factories import UserFactory
from apps.Book.book_factories import BookFactory

faker = FakerFactory.create()

class UserDetailFactory(DjangoModelFactory):
    class Meta:
        model = UserDetail

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    #email = EmailField We do not support this field type
    phone = LazyAttribute(lambda x: faker.text(max_nb_chars=30))
    address = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    status = Iterator([True, False])
    created_by = SubFactory(UserFactory)
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))

class IssueBookDetailFactory(DjangoModelFactory):
    class Meta:
        model = IssueBookDetail

    book = SubFactory(BookFactory)
    issue_date = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    return_date = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    return_status = Iterator([True, False])
    user = SubFactory(UserDetailFactory)
    #sent_email = PositiveIntegerField We do not support this field type
    fine = LazyAttribute(lambda x: faker.pydecimal(left_digits=8, right_digits=2, positive=True))
    fine_note = LazyAttribute(lambda x: faker.paragraph(nb_sentences=3, variable_nb_sentences=True))
    created_by = SubFactory(UserFactory)
    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    updated_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))