
from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT
from accounts import views
import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    url(r'', include('accounts.urls')),
    url(r'^accounts/', include('userprofile.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
