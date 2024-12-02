from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookList(generics.ListCreateAPIView):
    """View to list all books and create a new book."""
    queryset = Book.objects.all()  # Queryset for retrieving all Book objects
    serializer_class = BookSerializer  # Serializer to convert Book instances to/from JSON
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access to unauthenticated users, but restrict write access

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, or deleting a specific book."""
    queryset = Book.objects.all()  # Queryset for retrieving all Book objects
    serializer_class = BookSerializer  # Serializer for handling Book data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict modification access to authenticated users