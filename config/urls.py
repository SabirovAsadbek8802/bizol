from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main_app.urls')),
    path('store/', include('apps.store_app.urls')),
    path('blog/', include('apps.blogs_app.urls')),
    # path('', include('apps.store_app.urls')),
]
