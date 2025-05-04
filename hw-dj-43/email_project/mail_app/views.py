
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText

def send_bulk_mail(request):
    recipients = ['example1@mail.com', 'example2@mail.com']
    sender = 'your_email@gmail.com'
    password = 'your_app_password'

    subject = 'Восстановление пароля'
    body = 'Ссылка на восстановление: https://example.com/reset-password'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)

        for recipient in recipients:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = recipient
            server.sendmail(sender, recipient, msg.as_string())

        server.quit()
        return HttpResponse('Письма отправлены')
    except Exception as e:
        return HttpResponse(f'Ошибка: {{e}}')
