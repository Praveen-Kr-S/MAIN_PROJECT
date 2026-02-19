from django import forms
from .models import Customer, Orders


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_since']

        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'customer_since': forms.DateInput(attrs={'class':'form-control'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_reference', 'product_reference', 'order_number', 'order_date', 'quantity']
        
        widgets = {
            'customer_reference': forms.Select(attrs={'class':'form-control mb-3'}),
            'product_reference': forms.Select(attrs={'class':'form-control mb-3'}),
            'order_number': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'order_date': forms.DateInput(attrs={'class':'form-control mb-3'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control mb-3'}),
        }