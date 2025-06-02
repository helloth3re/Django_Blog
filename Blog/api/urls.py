
from django.urls import path, include
from .views import PostListCreate, PostDetail

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail')
]