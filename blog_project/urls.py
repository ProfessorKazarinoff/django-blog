# blog_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("posts/", include("posts.urls")),
    path("pages/", include("pages.urls")),
    path("", include("pages.urls")),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
