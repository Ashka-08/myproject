from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_add/', views.product_add, name='product_add'),
    path('products_update/', views.products_update, name='products_update'),
]