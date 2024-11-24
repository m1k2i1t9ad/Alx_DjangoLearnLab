from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Queryset for all books
    serializer_class = BookSerializer  # Serializer for book instances