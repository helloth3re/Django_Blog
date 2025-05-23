
from django.contrib import admin
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('logout/', views.logout_view, name="logout")
]
