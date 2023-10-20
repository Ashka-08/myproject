from django.core.management.base import BaseCommand

from hw2_app.models import User, Order


class Command(BaseCommand):
    help = "Update order customer by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Order id')
        parser.add_argument('pk2', type=str, help='User id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user_id = kwargs.get('pk2')
        order = Order.objects.filter(pk=pk).first() 
        user = User.objects.filter(pk=user_id).first()
        order.customer = user
        order.save()
        self.stdout.write(f'{order}')