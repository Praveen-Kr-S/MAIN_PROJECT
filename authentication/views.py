from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout

def LoginForm(request):
    context = {'error': ''}
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all_products')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)   
    return render(request,'login.html',context)

def Logout(request):
    logout(request)
    return redirect('/')
