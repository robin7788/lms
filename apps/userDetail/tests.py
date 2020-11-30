from django.test import TestCase
from django.contrib.auth.models import User
from apps.userDetail.models import UserDetail, IssueBookDetail
from apps.Book.models import Book
from django.utils import timezone
import datetime

"""
------------------------------------------------------------------------------------------------
Test case for UserDetail app
------------------------------------------------------------------------------------------------
"""
class UserDetailTestCase(TestCase):
    TEST_USER_USERNAME = "admin"
    TEST_USER_PASSWORD = "adminadmin"
    TEST_USER_EMAIL = "admin@test.com"

    def setUp(self):
        self.user = User.objects.create_superuser(
            username=self.TEST_USER_USERNAME,
            password=self.TEST_USER_PASSWORD,
            email=self.TEST_USER_EMAIL
        )
        self.client.login(username=self.TEST_USER_USERNAME, password=self.TEST_USER_PASSWORD)

        Book.objects.create(
            name='Book 1',
            isbn_number='ISBN123',
            published_year='2020-11-13'
        )
        self.test_user_detail_add()
        self.test_issue_book_add()

    """
    Add two users test user 1 and test user 2
    """
    def test_user_detail_add(self):
        try:
            user = User.objects.first()

            UserDetail.objects.create(
                    name="Test User 1",
                    email="testuser1@test.com",
                    phone="0987654321",
                    address="University Way, London",
                    status=True,
                    created_by=user,
                    created_at=timezone.now(),
                    updated_at=timezone.now()
                )

            UserDetail.objects.create(
                    name="Test User 2",
                    email="testuser2@test.com",
                    phone="0987654321",
                    address="Docklands Campus, London",
                    status=1,
                    created_by=user,
                    created_at=timezone.now(),
                    updated_at=timezone.now()
                )
        except User.DoesNotExist:
            print('User not found.')

    """
    Check whether added users are correctly identified
    """
    def test_check_user_exists(self):
        try:
            test1 = UserDetail.objects.filter(email="testuser1@test.com").first()
            test2 = UserDetail.objects.filter(email="testuser2@test.com").first()
            self.assertEqual(test1.name, "Test User 1")
            self.assertEqual(test2.name, "Test User 2")

        except UserDetail.DoesNotExist:
            print('User detail not found.')

    """
    Issue same book twice to first user
    """
    def test_issue_book_add(self):
        try:
            user = User.objects.first()
            book = Book.objects.filter(status=1).first()
            userDetail = UserDetail.objects.first()

            IssueBookDetail.objects.create(
                book=book,
                issue_date=timezone.now(),
                return_date=timezone.now(),
                return_status=1,
                user=userDetail,
                fine=10.21,
                fine_note="Test Fine 1",
                created_by=user,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            IssueBookDetail.objects.create(
                book=book,
                issue_date=timezone.now(),
                return_date=timezone.now(),
                return_status=0,
                user=userDetail,
                fine=30.12,
                fine_note="Test Fine 2",
                created_by=user,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
        except User.DoesNotExist:
            print('User not found.')
        except Book.DoesNotExist:
            print('Did not find any book.')
        except UserDetail.DoesNotExist:
            print('Did not find any user.')

    """
    Check whether issued book are correctly identified
    """
    def test_issue_book_exists(self):
        try:
            issued_book1 = IssueBookDetail.objects.filter(fine_note="Test Fine 1").first()
            issued_book2 = IssueBookDetail.objects.filter(fine_note="Test Fine 2").first()

            self.assertEqual(issued_book1.return_status, 1)
            self.assertEqual(issued_book2.return_status, 0)

        except IssueBookDetail.DoesNotExist:
            print('Issued book not found.')