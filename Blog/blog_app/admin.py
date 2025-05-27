from django.contrib import admin

from blog_app.models import Category, Tag, Author, Post, Gallery, Banner

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Gallery)
admin.site.register(Banner)