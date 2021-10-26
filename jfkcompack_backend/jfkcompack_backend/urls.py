from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index

urlpatterns = [
    path('_/', admin.site.urls),
    path('', index, name="index"),
    path('api/v1/', include('core.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
