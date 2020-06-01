# posts/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post

# view test
class PostsListViewTest(TestCase):
    def test_post_list_page_view(self):
        url = reverse("post_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class PostsNewPageTest(TestCase):
    def test_new_post_page_status(self):
        response = self.client.get("/posts/new/")
        self.assertEqual(response.status_code, 200)

    def test_new_post_page_url_by_name(self):
        response = self.client.get(reverse("post_new"))
        self.assertEqual(response.status_code, 200)

    def test_new_post_page_uses_correct_template(self):
        response = self.client.get(reverse("post_new"))
        self.assertTemplateUsed("post_new.html")


class PostsNewUpdateDeleteTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@email.com", password="secret"
        )

        self.post = Post.objects.create(
            title="A good title",
            summary="My short summary",
            body="The long form post",
            author=self.user,
        )

    def test_string_repr(self):
        post = Post(title="a test title")
        self.assertEqual(str(post), "a test title")

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), "/posts/1/")

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.summary}", "My short summary")
        self.assertEqual(f"{self.post.body}", "The long form post")

    def test_post_create_view(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "summary": "New summary",
                "body": "New text",
                "author": self.user,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New title")
        self.assertContains(response, "New text")

    def test_post_update_view(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {"title": "Updated Title", "body": "Updated text",},
        )
        self.assertEqual(response.status_code, 200)

    def test_post_delete_view(self):
        response = self.client.get(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 200)
