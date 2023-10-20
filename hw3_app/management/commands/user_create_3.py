from django.core.management.base import BaseCommand
from django.utils import timezone

from hw3_app.models import User


class Command(BaseCommand):
    help = "Create user by name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        user = User(name=name,
                    email=f'{name}@mail.ru',
                    phone='88001114567',
                    address='Some address',
                    reg_date=timezone.now())
        user.save()
        self.stdout.write(f'{user}')