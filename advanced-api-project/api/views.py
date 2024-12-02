from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class ListView(generics.ListCreateAPIView):
    """View to list all books and create a new book."""
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for data serialization
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access for everyone, write access for authenticated users

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, or deleting a specific book."""
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for data serialization
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict write access to authenticated users

# Optional: If you want to create separate views for Create, Update, and Delete
class CreateView(generics.CreateAPIView):
    """View to create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UpdateView(generics.UpdateAPIView):
    """View to update an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DeleteView(generics.DestroyAPIView):
    """View to delete a specific book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]