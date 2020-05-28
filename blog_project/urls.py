#blog_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('pages/', include('pages.urls')),
    path('', include('blog.urls')),
]
