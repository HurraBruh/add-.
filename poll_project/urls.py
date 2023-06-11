from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from poll import views as poll_views

urlpatterns = [
    path('bebramen/', admin.site.urls),
    path('', poll_views.home, name='home'),
    path('about/', poll_views.about, name='about'),
    path('garanties/', poll_views.garanties, name='garanties'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)