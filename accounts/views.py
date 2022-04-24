from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'error': "the username or password is wrong",
            }
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect('/')


    return render(request, "accounts/login.html", {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/logout/")

    return render(request, "accounts/logout.html", {})

def register_view(request):

    return render(request, "accounts/register.html", {})