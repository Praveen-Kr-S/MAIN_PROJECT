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

def EditProduct(request,id):
    product_form = Product.objects.get(id=id)
    context = {
        'product_form': ProductForm(instance=product_form)
    }
    if request.method == 'POST':
        edit_form = ProductForm(request.POST,request.FILES,instance=product_form)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('all_products')
    
    return render(request,'edit_product.html',context)

def DeleteProduct(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('all_products')