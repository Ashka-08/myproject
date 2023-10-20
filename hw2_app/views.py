from django.shortcuts import render
from django.http import HttpResponse
from hw2_app.models import User, Product, Order
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = """
        <h1>2 домашнее задание</h1>
        <p>
            Создайте три модели Django: клиент, товар и заказ.<br>
            Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.<br>
            <ul>
                <li>
                    Поля модели «Клиент»:
                    — имя клиента
                    — электронная почта клиента
                    — номер телефона клиента
                    — адрес клиента
                    — дата регистрации клиента
                </li>
                <li>
                    Поля модели «Товар»:
                    — название товара
                    — описание товара
                    — цена товара
                    — количество товара
                    — дата добавления товара
                </li>
                <li>
                    Поля модели «Заказ»:
                    — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
                    — связь с моделью «Товар», указывает на товары, входящие в заказ
                    — общая сумма заказа
                    — дата оформления заказа
                </li>
            </ul>
            Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой БД<br>
        </p>
        <p> 
            Ссылки на страницы:
            <ul>
                <li>
                    <a href="http://127.0.0.1:8000/hw2/users/">users</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:8000/hw2/orders/">orders</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:8000/hw2/products/">products</a>
                </li>
            </ul>
        </p> 
    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def users(request):
    logger.info(f'{request} request received')
    users = User.objects.all()
    return HttpResponse(users)


def orders(request):
    logger.info(f'{request} request received')
    orders = Order.objects.all()
    return HttpResponse(orders)


def products(request):
    logger.info(f'{request} request received')
    products = Product.objects.all()
    return HttpResponse(products)