# posts/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = (
        "title",
        "summary",
        "body",
    )
    template_name = "post_edit.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")


class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ("title","summary","body","author")
