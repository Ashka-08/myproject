import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from hw3_app.models import User, Product, Order


LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicingelit. " \
"Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime " \
"nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
"tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
"tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
"quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
"consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
"ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
"quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."


class Command(BaseCommand):
    help = 'Generate fake products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        text = LOREM.split()
        # Generate fake products
        for j in range(1, count + 1):
            product = Product(name=f'{random.choice(text)}',
                              description=" ".join(random.choices(text, k=15)),
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