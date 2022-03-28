from django.test import TestCase
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_post_name = f"{post.text}"
        self.assertEqual(expected_post_name, "test")
