from django.shortcuts import render, redirect
from .models import Customer,Orders
from .forms import CustomerForm,OrderForm
from Inventory.models import Product

def All_Customers(request):
    customers = Customer.objects.all()
    return render(request, 'All_Customers.html', {'customers': customers})

def Add_Customers(request):
    customer_form = CustomerForm()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('all_customers')
    return render(request, 'Add_Customers.html', {'customer_form': customer_form})
    
def Edit_Customers(request, sp):
    customer = Customer.objects.get(id=sp)
    edit_customer_form = CustomerForm(instance=customer)
    if request.method == 'POST':
        edit_customer_form = CustomerForm(request.POST, instance=customer)
        if edit_customer_form.is_valid():
            edit_customer_form.save()
            return redirect('all_customers')
    return render(request, 'Add_Customers.html', {'edit_customer_form': edit_customer_form})
    
def Delete_Customers(request, sp):
    customer = Customer.objects.get(id=sp)
    customer.delete()
    return redirect('all_customers')


def Add_Orders(request):
    
    context = {
        'order_form':OrderForm()
    }
    if request.method == 'POST':
        product_reference = Product.objects.get(id=request.POST.get('product_reference'))
        amount = float(product_reference.price) * float(request.POST.get('quantity'))
        gst_amount = (amount * float(product_reference.gst)) / 100
        bill_amount = amount + gst_amount   
        new_order = Orders(
            customer_reference_id = request.POST['customer_reference'],
            product_reference_id = request.POST['product_reference'],
            order_number = request.POST['order_number'],
            order_date = request.POST['order_date'],
            quantity = request.POST['quantity'],
            amount = amount,
            gst_amount = gst_amount,
            bill_amount = bill_amount
        )
        new_order.save()
        return redirect('all_orders')       
    return render(request,'add_orders.html',context)

def All_Orders(request):
    orders = Orders.objects.all()
    return render(request, 'All_Orders.html', {'orders': orders})

def Edit_Orders(request, sp):
    order = Orders.objects.get(id=sp)
    edit_order_form = OrderForm(instance=order)
    if request.method == 'POST':
        product_reference = Product.objects.get(id=request.POST.get('product_reference'))
        amount = float(product_reference.price) * float(request.POST.get('quantity'))
        gst_amount = (amount * float(product_reference.gst)) / 100
        bill_amount = amount + gst_amount   
        new_order = Orders(
            customer_reference_id = request.POST['customer_reference'],
            product_reference_id = request.POST['product_reference'],
            order_number = request.POST['order_number'],
            order_date = request.POST['order_date'],
            quantity = request.POST['quantity'],
            amount = amount,
            gst_amount = gst_amount,
            bill_amount = bill_amount
        )
        new_order.save()
        return redirect('all_orders')
    return render(request, 'Add_Orders.html', {'edit_order_form': edit_order_form})

def Delete_Orders(request, sp):
    order = Orders.objects.get(id=sp)
    order.delete()
    return redirect('all_orders')
