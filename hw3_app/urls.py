from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('orders/', views.orders, name='orders'),
    path('products/', views.products, name='products'),
    path('purchases/<int:user_id>/', views.purchases, name='purchases'),
    path('purchases/<int:user_id>/<int:days>/', views.purchases_of_days, name='purchases_of_days'),
]