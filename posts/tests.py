from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        # Create a superuser
        self.superuser = User.objects.create_superuser(username='retrogamer', password='qwerty92', email='retrogamer@example.com')

        # Create a regular user
        self.user = User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        # Log in as a regular user
        self.client.login(username='adam', password='pass')

        # Create a post
        Post.objects.create(owner=self.user, title='a title')

        # Log out and try to get the list of posts
        self.client.logout()
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        # Log in as a regular user
        self.client.login(username='adam', password='pass')

        # Try to create a post
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        # Try to create a post without logging in
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
