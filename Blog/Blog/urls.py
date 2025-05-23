
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views #new

from django.conf.urls.static import static
from django.conf import settings


from user_auth.views import CustomLoginView

urlpatterns = [
    path('admin/login/', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('authenticate/', include('user_auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

