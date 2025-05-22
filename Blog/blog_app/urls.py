
from django.contrib import admin
from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('gallery/', views.gallery_view, name="gallery"),
    path('blog/', views.blog_view, name="blog"),
    path('blog/category/<str:slug>', views.blog_view, name="blog_by_category"),
    path('contact/', views.contact_view, name="contact"),
    path('single/<str:slug>', views.single_view, name="single"),
]