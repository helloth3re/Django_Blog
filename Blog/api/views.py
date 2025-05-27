from django.core.serializers import serialize
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework import permissions, status

from blog_app.models import Post

from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


