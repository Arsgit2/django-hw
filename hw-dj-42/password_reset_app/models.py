
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

def send_password_reset_email(user):
    subject = 'Восстановление пароля'
    email_template_name = 'password_reset_email.html'
    
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(str(user.pk).encode())
    
    password_reset_url = f"{settings.SITE_URL}/reset/{uid}/{token}/"
    
    context = {
        'user': user,
        'password_reset_url': password_reset_url,
    }
    
    message = render_to_string(email_template_name, context)
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

def send_mass_password_reset_emails():
    users = User.objects.all()
    for user in users:
        send_password_reset_email(user)
    