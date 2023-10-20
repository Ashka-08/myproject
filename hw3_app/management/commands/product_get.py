from django.core.management.base import BaseCommand

from hw3_app.models import Product


class Command(BaseCommand):
    help = "Get product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Product id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(id=pk).first()
        self.stdout.write(f'{product}')