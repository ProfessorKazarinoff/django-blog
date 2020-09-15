# posts/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "image", "summary", "body")
    template_name = "post_edit.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")


class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ("title", "image", "summary", "body", "author")


# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post_new.html'
#     success_url = reverse_lazy('home')
