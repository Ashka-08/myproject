from django.core.management.base import BaseCommand

from hw3_app.models import User, Order


class Command(BaseCommand):
    help = "Update order customer by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Order id')
        parser.add_argument('date_ordered', type=str, help='Order date_ordered')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        date_ordered = kwargs.get('date_ordered')
        order = Order.objects.filter(pk=pk).first() 
        order.date_ordered = date_ordered
        order.save()
        self.stdout.write(f'{order}')