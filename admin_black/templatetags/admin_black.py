import re
from django import template

from admin_black.utils import get_menu_items

register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag


@register.filter
def clean_text(value):
    res = value.replace('\n', ' ')
    return res


@register.filter
def checkbox(value):
    res = re.sub(r"</?(?i:td)(.|\n)*?>", "", value)
    return res

# register tag for comparing and making menu active
@register.filter
def startswith(text, starts):
    if isinstance(text, str):
        return text.startswith(starts)
    return False

@assignment_tag(takes_context=True)
def admin_black_get_menu(context):
    return get_menu_items(context)


@assignment_tag(takes_context=True)
def get_direction(context):
    res = {
        'panel': 'text-left',
        'notify': 'right',
        'float': 'float-right',
        'reverse_panel': 'text-right',
        'nav': 'ml-auto'
    }
    if context.get('LANGUAGE_BIDI'):
        res['panel'] = 'text-right'
        res['notify'] = 'left'
        res['float'] = ''
        res['reverse_panel'] = 'text-left'
        res['nav'] = 'mr-auto'
    return res


@assignment_tag(takes_context=True)
def get_admin_black_setting(context):
    user = context.get('request').user
    admin_black_setting = user.admin_black_setting if hasattr(user, 'admin_black_setting') else None
    res = {
        'admin_black_setting': admin_black_setting,
        'sidebar_background': admin_black_setting.sidebar_background if admin_black_setting else 'primary',
        'dark_mode': admin_black_setting.dark_mode == True if admin_black_setting else False,
        'input_bg_color': '#27293c' if admin_black_setting and admin_black_setting.dark_mode else '#ffffff'
    }

    return res

from apps.Book.models import Book
from apps.Book.models import Category
from apps.userDetail.models import IssueBookDetail
from django.contrib.auth import get_user_model
from datetime import datetime


@assignment_tag(takes_context=True)
def get_admin_counted_data(context):
    users = get_user_model()
    books = Book.objects.count()
    librarians = users.objects.filter(groups__name='librarian').count()
    categories = Category.objects.count()
    recent_issued_book = IssueBookDetail.objects.filter(return_date__lt=datetime.now()).\
        filter(return_status=False).\
        order_by('-return_date').\
        all()[:10]
    res = {
        "books" : books,
        "librarians" : librarians,
        "categories" : categories,
        "recent_issued_book" : recent_issued_book,
    }

    return res
