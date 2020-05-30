# posts/urls.py

from django.urls import path

from .views import (
    PostUpdateView,
    PostDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
)

urlpatterns = [
    path("<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("", PostListView.as_view(), name="post_list"),
]
