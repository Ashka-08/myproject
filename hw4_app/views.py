from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.core.files.storage import FileSystemStorage
import logging
from hw4_app.models import Product
from hw4_app.forms import FormProductAdd, FormProductsUpdate


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    context = {'title': 'Домашнее задание № 4 по курсу Django'}
    return TemplateResponse(request, 'hw4_app/index.html', context)


def product_add(request):
    logger.info(f'{request} request received')
    context = {'title': 'Добавление товара'}
    if request.method == 'POST':
        form = FormProductAdd(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            prod_quant = form.cleaned_data['prod_quant']
            img = form.cleaned_data['img']
            fs = FileSystemStorage()
            fs.save(img.name, img)
            product = Product(
                name=name,
                description=description,
                price=price,
                prod_quant=prod_quant,
                img=img)
            product.save()
            context['answer'] = f'Товар добавлен: {product}'
            return TemplateResponse(request, 'hw4_app/form_product.html', context)
    else:
        form = FormProductAdd()
        context['form'] = form
    return TemplateResponse(request, 'hw4_app/form_product.html', context)


def products_update(request):
    logger.info(f'{request} request received')
    context = {'title': 'Редактирование товаров'}
    if request.method == 'POST':
        form = FormProductsUpdate(request.POST, request.FILES)
        if form.is_valid():
            pk = form.cleaned_data['product'].pk
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            prod_quant = form.cleaned_data['prod_quant']
            img = form.cleaned_data['img']
            if img:
                fs = FileSystemStorage()
                fs.save(img.name, img)
            product = Product.objects.filter(pk=pk).first()
            product.name=name
            product.description=description
            product.price=price
            product.prod_quant=prod_quant
            product.img=img
            product.save()
            context['answer'] = f'Товар изменен: {product}'
            return TemplateResponse(request, 'hw4_app/form_product.html', context)
    else:
        form = FormProductsUpdate()
        context['form'] = form
    return TemplateResponse(request, 'hw4_app/form_product.html', context)