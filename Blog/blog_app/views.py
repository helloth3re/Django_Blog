from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404

from .models import *

from random import shuffle

from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    posts = list(Post.objects.all()) #retrieves all post

    shuffle(posts) #shuffles posts

    posts = posts[:10] #splits 10 posts

    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def gallery_view(request):
    pictures = Gallery.objects.all()
    categories = Category.objects.all()

    context = {
        "pictures": pictures,
        "categories": categories,
    }

    return render(request, 'gallery.html', context)

def blog_view(request, slug=None):
    categories = Category.objects.all()
    recents = Post.objects.order_by('created_at')[:5]
    if slug:
        category = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(categories=category)
    else:
        posts = Post.objects.all()

    p = Paginator(posts, 5) #4post per page
    page_num = request.GET.get('page')
    page_obj = p.get_page(page_num)
    context = {
        "page_obj": page_obj,
        "categories": categories,
        "recents": recents,
    }
    return render(request, 'blog.html', context)

def single_view(request, slug):
    single_post = get_object_or_404(Post, slug=slug)

    context = {
        "single_post": single_post,
    }

    return render(request, 'single.html', context)

def contact_view(request):
    return render(request, 'contact.html')

