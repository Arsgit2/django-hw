
from django.core.management.base import BaseCommand
from password_reset_app.models import send_mass_password_reset_emails

class Command(BaseCommand):
    help = '�������� ����� � ��������������� ������ ���� �������������'

    def handle(self, *args, **kwargs):
        send_mass_password_reset_emails()
        self.stdout.write(self.style.SUCCESS('��� ������ ����������!'))
    