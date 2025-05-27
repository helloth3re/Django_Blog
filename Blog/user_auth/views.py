from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from pyexpat.errors import messages


# Create your views here.
from user_auth.form import EmailLoginForm

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'Auth/login.html'  # your custom template
    authentication_form = EmailLoginForm

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return '/dashboard/'  # Django admin dashboard
        else:
            return '/dashboard/'  # Your custom dashboard


def logout_view(request):
    logout(request)
    return redirect('home')
