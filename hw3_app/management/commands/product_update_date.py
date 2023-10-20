from django.core.management.base import BaseCommand

from hw3_app.models import Product


class Command(BaseCommand):
    help = "Update product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Product id')
        parser.add_argument('reg_date', type=str, help='Product reg_date')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        reg_date = kwargs.get('reg_date')
        product = Product.objects.filter(id=pk).first()
        product.reg_date = reg_date
        product.save()
        self.stdout.write(f'{product}')