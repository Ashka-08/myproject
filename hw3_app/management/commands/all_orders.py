from django.core.management.base import BaseCommand

from hw3_app.models import Order


class Command(BaseCommand):
    help = "Get orders with list products"

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            self.stdout.write(f'{order}')
            self.stdout.write(f'Продукты:')
            for product in order.products.all():
                self.stdout.write(f'{product}')