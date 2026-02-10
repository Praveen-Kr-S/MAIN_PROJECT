from django.forms import ModelForm
from .models import Customer, Orders


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_since']


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_reference', 'product_reference', 'order_number', 'order_date', 'quantity']
        