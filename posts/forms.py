# posts/forms.py

from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "summary", "body", "author"]
