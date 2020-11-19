from ajax_select import register, LookupChannel
from apps.Book.models import Book
from apps.userDetail.models import UserDetail
from django.db.models.expressions import RawSQL

@register('book')
class BookLookup(LookupChannel):

    model = Book

    def get_query(self, q, request):
        # valid_books_ids1 = Book.objects.filter(status=1).extra(
        #         select={
        #             'qty': 'CASE WHEN book_book.quantity <= (SELECT COUNT(ub.book_id) as qtt FROM userdetail_issuebookdetail as ub ' \
        #                    'WHERE ub.return_status=0 AND ub.book_id = book_book.id ' \
        #                    'GROUP BY ub.book_id) ' \
        #                    'THEN 0 ' \
        #                    'WHEN book_book.quantity = 0 THEN 0 ELSE 1 END'
        #         }
        #     ).all()

        # Code has to be optimized
        valid_books_ids = Book.\
            objects.raw("SELECT bb.id, "
                             "CASE "
                                 "WHEN "
                                    "bb.quantity <= (SELECT COUNT(ub.book_id) as qtt "
                                        "FROM userdetail_issuebookdetail as ub "
                                        "WHERE ub.return_status=0 AND ub.book_id = bb.id "
                                        "GROUP BY ub.book_id) "
                                "THEN 0 "
                                "WHEN bb.quantity = 0 THEN 0 "
                                "ELSE 1 "
                                "END as qty "
                        "FROM book_book as bb "
                        "HAVING qty = 0")
        valid_books_ids = set(ans.id for ans in valid_books_ids)
        return self.model.objects.filter(name__icontains=q). \
                filter(quantity__gte=1).filter(status=1). \
                   exclude(id__in=valid_books_ids).order_by('name')[:50]

@register('user')
class UserLookup(LookupChannel):

    model = UserDetail

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).filter(status=1).order_by('name')[:50]
