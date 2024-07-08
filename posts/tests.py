from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        # Create a superuser
        self.superuser = User.objects.create_superuser(username='retrogamer', password='qwerty92', email='retrogamer@pixelstation.com')

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
        
class PostDetailViewTests(APITestCase):

    def setUp(self):
        self.retro_gamer = User.objects.create_superuser(username='retrogamer', email='retrogamer@pixelstation', password='qwerty92')
        self.client.force_login(self.retro_gamer)

        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')
        self.post1 = Post.objects.create(
            owner=self.adam, title='a title', content='adams content'
        )
        self.post2 = Post.objects.create(
            owner=self.brian, title='another title', content='brians content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get(f'/posts/{self.post1.id}/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_cannot_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')  # Invalid ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(f'/posts/{self.post1.id}/', {'title': 'a new title'})
        post = Post.objects.get(pk=self.post1.id)
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.force_login(self.adam)
        response = self.client.put(f'/posts/{self.post2.id}/', {'title': 'Updated Title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)