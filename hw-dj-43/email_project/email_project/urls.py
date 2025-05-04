
from django.urls import path
from mail_app.views import send_bulk_mail

urlpatterns = [
    path('send-mails/', send_bulk_mail),
]
