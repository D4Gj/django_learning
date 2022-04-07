from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A',
            body="ABC",
            author=self.user,
        )

    def test_string_repr(self):
        post = Post(title='A')
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A')
        self.assertTemplateUsed(response, 'post_detail.html')
