from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Book

class BookTest(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        data = {'title': 'Test Book', 'author': 'John Doe', 'publication_year': 2023}
        url = reverse('book-list')
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.get(pk=response.data['id'])
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.author, data['author'])
        self.assertEqual(book.publication_year, data['publication_year'])