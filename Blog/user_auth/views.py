from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from pyexpat.errors import messages


# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'LOGIN SUCCESS')
        else:
            messages.error(request, 'Invalid Credentials')

    return render(request, 'Auth/login.html')

