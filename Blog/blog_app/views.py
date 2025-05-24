from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import *

from .forms import PostForm

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
@login_required
def user_dashboard(request):
    user = request.user

    articles = Post.objects.filter(author=user)

    context = {
        "articles": articles
    }

    return render(request, 'user-dash/my-article.html', context)
@login_required
def article_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            form.save_m2m()  # Save tags (many-to-many)
            return redirect('dashboard')  # Redirect after successful save
    else:
        form = PostForm()
    return render(request, 'user-dash/add-article.html', {'form': form})
@login_required
def article_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)  # ensure ownership

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # pre-filled with data
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)  # pre-fill with existing data

    return render(request, 'user-dash/edit-article.html', { "form": form })
@login_required
def article_delete(request, slug):
    article = get_object_or_404(Post, slug=slug, author=request.user)
    article.delete()
    return redirect('dashboard')
