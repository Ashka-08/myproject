from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    html = """
        <h1>1 домашнее задание</h1>
        <p>Создайте пару представлений в вашем первом приложении:<br>
        <ul>
            <li>главная</li>
            <li><a href="http://127.0.0.1:8000/about/">о себе</a></li>
        </ul>
        Внутри каждого представления должна быть переменная html — <br>
        многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.<br>
        Сохраняйте в логи данные о посещении страниц.</p> 
    """
    logger.info('Index page accessed')
    return HttpResponse(html)

def about(request):
    html = """
        <h1>О себе</h1>
        <h1>Привет</h1>
        <p>Я Марванова Любовь и уже более 3-х лет создаю сайты на разных технологиях:<br>
        <ul>
            <li>сначала был зеро-кодинг,</li>
            <li>потом изучила Webflow, разбралась в HTML, CSS, частично JS, PHP,</li>
            <li>а теперь спасибо, Python, появились навыки в разных фреймворках, <br>
            но все это пока темный лес, предстоит изучать и изучать =)</li>
        </ul>
        Вернуться на <a href="http://127.0.0.1:8000/">главную</a></p> 
    """
    logger.info('About page accessed')
    return HttpResponse(html)