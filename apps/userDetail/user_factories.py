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
from django.contrib.auth.models import User

faker = FakerFactory.create()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    password = LazyAttribute(lambda x: faker.text(max_nb_chars=128))
    last_login = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    is_superuser = Iterator([True, False])
    username = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    first_name = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    last_name = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    #email = EmailField We do not support this field type
    is_staff = Iterator([True, False])
    is_active = Iterator([True, False])
    date_joined = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))