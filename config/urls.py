from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/',include('accounts.urls')),
    path('home/', include('home.urls')),
    path('room/', include('room.urls')),
    path('product/', include('product.urls')),
    path('service/', include('service.urls')),
    path('blog/', include('blog.urls')),
    path('admin_dashboard/', include('creatoradmin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
