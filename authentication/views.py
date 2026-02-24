from django.shortcuts import render


def LoginForm(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST.get('password')
        print(username,password)
    return render(request,'login.html')
