from django.test import TestCase
from django.forms.models import model_to_dict
from .models import UserDetail, IssueBookDetail
from django.contrib.auth.models import User
from apps.Book.models import Book
from django.utils import timezone

class TestCaseUserDetail(TestCase):
    TEST_USER_USERNAME = "admin"
    TEST_USER_PASSWORD = "adminadmin"
    TEST_USER_EMAIL = "admin@test.com"

    """
    ------------------------------------------------------------------------------
    Creating user data before testing other part of userDetail
    ------------------------------------------------------------------------------
    """
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
        self.test_user_detail_create()
        self.test_issue_book_detail_create()
    """
    ------------------------------------------------------------------------------
    Test the creation of a UserDetail model
    ------------------------------------------------------------------------------
    """
    def test_user_detail_create(self):
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
    ------------------------------------------------------------------------------
    Test the creation of a UserDetail model
    ------------------------------------------------------------------------------
    """
    def test_created_user_detail(self):
        self.assertEqual(UserDetail.objects.count(), 2)


    """
    -------------------------------------------------------------------------------------------------------------------
    Test that all attributes of UserDetail server are counted. 
    It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    Note: excluded columns via admin will not get counted in model_to_dict like created_by, created_at and updated_at 

    -------------------------------------------------------------------------------------------------------------------
    """
    def test_user_detail_attribute_count(self):
        user_detail = UserDetail.objects.first()
        user_detail_dict = model_to_dict(user_detail)
        self.assertEqual(len(user_detail_dict.keys()), 6)


    """
    ------------------------------------------------------------------------------------------------------------------
    Test that all attributes of UserDetail server have content. 
    This test will break if an attributes name is changed.
    ------------------------------------------------------------------------------------------------------------------
    """
    def test_user_detail_attribute_content(self):
        user_detail = UserDetail.objects.first()
        self.assertIsNotNone(user_detail.id)
        self.assertIsNotNone(user_detail.name)
        self.assertIsNotNone(user_detail.email)
        self.assertIsNotNone(user_detail.phone)
        self.assertIsNotNone(user_detail.address)
        self.assertIsNotNone(user_detail.status)
        self.assertIsNotNone(user_detail.created_by)
        self.assertIsNotNone(user_detail.created_at)
        self.assertIsNotNone(user_detail.updated_at)

    """
    -----------------------------------------------------------------------------------------------------
    Test the creation of a IssueBookDetail model
    -----------------------------------------------------------------------------------------------------
    """
    def test_issue_book_detail_create(self):
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
    -----------------------------------------------------------------------------------------------------
    Test the creation of a IssueBookDetail model
    -----------------------------------------------------------------------------------------------------
    """
    def test_created_issue_book_detail(self):
        self.assertEqual(IssueBookDetail.objects.count(), 2)
    """
    ------------------------------------------------------------------------------------------------------------------
    Test that all attributes of IssueBookDetail server are counted.
    It will count the primary key and all editable attributes.
    This test should break if a new attribute is added.
    Note: excluded columns via admin will not get counted in model_to_dict like issued_by, created_at and updated_at 
    ------------------------------------------------------------------------------------------------------------------
    """

    def test_issue_book_detail_attribute_count(self):
        issue_book_detail = IssueBookDetail.objects.first()
        issue_book_detail_dict = model_to_dict(issue_book_detail)
        self.assertEqual(len(issue_book_detail_dict.keys()), 9)



    """
    ------------------------------------------------------------------------------------------------------------------
    Test that all attributes of IssueBookDetail server have content. 
    This test will break if an attributes name is changed.
    ------------------------------------------------------------------------------------------------------------------
    """
    def test_issue_book_detail_attribute_content(self):
        issue_book_detail = IssueBookDetail.objects.first()
        self.assertIsNotNone(issue_book_detail.id)
        self.assertIsNotNone(issue_book_detail.book)
        self.assertIsNotNone(issue_book_detail.issue_date)
        self.assertIsNotNone(issue_book_detail.return_date)
        self.assertIsNotNone(issue_book_detail.return_status)
        self.assertIsNotNone(issue_book_detail.user)
        self.assertIsNotNone(issue_book_detail.sent_email)
        self.assertIsNotNone(issue_book_detail.fine)
        self.assertIsNotNone(issue_book_detail.fine_note)
        self.assertIsNotNone(issue_book_detail.created_by)
        self.assertIsNotNone(issue_book_detail.created_at)
        self.assertIsNotNone(issue_book_detail.updated_at)