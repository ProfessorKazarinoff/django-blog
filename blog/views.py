# blog/views.py

from django.views.generic import ListView

from posts.models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
