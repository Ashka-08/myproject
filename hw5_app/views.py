from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    html = """
        <h1>5 домашнее задание</h1>
        <p>
            Настройте под свои нужды вывод информации о клиентах, товарах и заказах <br>
            на страницах вывода информации об объекте и вывода списка объектов.
        </p>
    """
    logger.info('Index page accessed')
    return HttpResponse(html)