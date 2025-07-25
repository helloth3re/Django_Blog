
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


from user_auth.views import CustomLoginView

urlpatterns = [
    path('admin/login/', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('api-app/', include('api.urls')),
    path('authenticate/', include('user_auth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

