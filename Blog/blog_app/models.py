from tkinter.constants import CASCADE

from django.db import models
from user_auth.models import CustomUser

from django.utils.text import slugify

from ckeditor.fields import RichTextField

from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_profile')
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField()

    slug = models.SlugField(max_length=120, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    title = models.CharField(max_length=255)
    summary = RichTextField(blank=True, null=True)
    content = RichTextField()
    post_display = models.ImageField(upload_to='post_image/img')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post_author')

    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category', blank=False)
    tags = models.ManyToManyField(Tag, related_name='post_tag', blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=270, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery_image/img")
    name = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='gallery_author')
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='gallery_category')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=50, blank=False)
    banner_image = models.ImageField(upload_to='banner_images/img')
    slug = models.SlugField(max_length=270, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
