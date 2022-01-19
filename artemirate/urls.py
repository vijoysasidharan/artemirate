from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header  = "Artemirate Admin"
admin.site.site_title   = "Artemirate Admin Portal"
admin.site.index_title  = "Welcome to Artemirate India Portal"
