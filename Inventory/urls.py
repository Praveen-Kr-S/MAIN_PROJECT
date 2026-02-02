from django.urls import path
from .views import *
from django.shortcuts import render



urlpatterns = [
    path('products/', AllProducts, name='all_products'),
    path('products/add/', AddProduct, name='add_product')
]

