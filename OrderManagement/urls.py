from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [  
    path('customers/', All_Customers, name='all_customers'),
    path('customers/add/', Add_Customers, name='add_customers'),
    path('customers/edit/<int:sp>/', Edit_Customers, name='edit_customers'),
    path('customers/delete/<int:sp>/', Delete_Customers, name='delete_customers'),

    path('order/add/', Add_Orders, name='add_orders'),
    path('orderlist/', All_Orders, name='all_orders'),
    path('order/edit/<int:sp>/', Edit_Orders, name='edit_orders'),
    path('order/delete/<int:sp>/', Delete_Orders, name='delete_orders'),
]