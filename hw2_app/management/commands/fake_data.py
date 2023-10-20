import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from hw2_app.models import User, Product, Order


class Command(BaseCommand):
    help = 'Generate fake data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count users, orders and product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        
        # Generate fake products
        for j in range(1, count + 1):
            product = Product(name=f'product{j}',
                              description=f'description{j}',
                              price=random.randint(1, 100),
                              prod_quant=random.randint(1, 10),
                              reg_date=timezone.now())
            product.save()
        
        # Generate fake users
        for i in range(1, count + 1):
            user = User(name=f'user{i}',
                        email=f'user{i}@mail.com',
                        phone=f'8{random.randint(9000000000,10000000000)}',
                        address=f'Wall {i}, house {i}',
                        reg_date=timezone.now())
            user.save()
        
        # Generate fake orders
        for i in range(1, count + 1):
            user = User.objects.filter(pk=i).first()
            for _ in range(1, random.randint(1, count)):
                total_price = 0
                order = Order(
                    customer=user,
                    date_ordered=timezone.now()
                )
                for _ in range(1, random.randint(1, count)):
                    product = Product.objects.filter(pk=random.randint(1, count)).first()
                    total_price += product.price
                    order.total_price = total_price
                    order.save()
                    order.products.add(product)