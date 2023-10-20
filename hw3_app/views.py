from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.response import TemplateResponse
from hw3_app.models import User, Product, Order
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    context = {'title': 'Домашнее задание № 3 по курсу Django'}
    return TemplateResponse(request, 'hw3_app/index.html', context)


def users(request):
    logger.info(f'{request} request received')
    users = User.objects.all()
    context = {
        'title' : 'Пользователи',
        'users' : users
    }
    return TemplateResponse(request, 'hw3_app/users.html', context)


def orders(request):
    logger.info(f'{request} request received')
    orders = Order.objects.all()
    context = {
        'title' : 'Заказы',
        'orders' : orders,
    }
    return TemplateResponse(request, 'hw3_app/orders.html', context)


def products(request):
    logger.info(f'{request} request received')
    products = Product.objects.all()
    context = {
        'title' : 'Товары',
        'products' : products
    }
    return TemplateResponse(request, 'hw3_app/products.html', context)


def purchases(request, user_id):
    logger.info(f'{request} request received')
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user).order_by('-date_ordered')
    purchases = {}
    for order in orders:
        for product in order.products.all():
            if product not in purchases:
                purchases[product] = order.date_ordered
                logger.info(f'{product.name}: {order.date_ordered}')
    context = {
        'title' : f'Товары пользователя c ID {user_id}',
        'purchases' : purchases
    }
    return TemplateResponse(request, 'hw3_app/purchases.html', context)


def purchases_of_days(request, user_id, days):
    logger.info(f'{request} request received')
    user = get_object_or_404(User, pk=user_id)
    today = datetime.now()
    range_days = today - timedelta(days=days)

    orders = Order.objects.filter(customer=user, date_ordered__range=(range_days, today)).order_by('-date_ordered')
    purchases = {}
    for order in orders:
        for product in order.products.all():
            if product not in purchases:
                purchases[product] = order.date_ordered
                logger.info(f'{product.name}: {order.date_ordered}')
    context = {
        'title' : f'Товары пользователя c ID {user_id} за последние {days} дней',
        'purchases' : purchases
    }
    return TemplateResponse(request, 'hw3_app/purchases.html', context)