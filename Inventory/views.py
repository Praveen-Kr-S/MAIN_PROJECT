from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm 

def AllProducts(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def AddProduct(request):
    context = {
        'product_form': ProductForm()
    }
    if request.method == 'POST':
        product_form = ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('all_products')
    return render(request,'add_products.html',context)


    