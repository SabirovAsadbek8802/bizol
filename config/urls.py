from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('blog/', include('apps.blogs_app.urls')),
    path('', include('apps.main_app.urls')),
    path('shop/', include('apps.payments_app.urls')),
    path('store/', include('apps.store_app.urls')),
    path('users/', include('apps.users_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)