from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
