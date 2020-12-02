from django.shortcuts import render
from django.core.mail import send_mail

def sendmail(request):
    send_mail(
        'Hello from lms',
        'This is an automated message. Please ignore as soon as you see this message.',
        'info@lms.merobin.com',
        ['robinme7@gmail.com'],
        fail_silently=False
    )
    return  render(request, 'admin/send_mail.html')
