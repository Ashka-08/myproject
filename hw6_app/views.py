from django.shortcuts import render
from django.template.response import TemplateResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    context = {'title': 'Домашние задания по курсу Django'}
    return TemplateResponse(request, 'hw6_app/index.html', context)
