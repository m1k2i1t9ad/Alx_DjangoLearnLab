from django.urls import path,include
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView


urlpatterns = [
    # path('authors/', AuthorList.as_view(), name='author-list'),
    path('books/', ListView.as_view(), name='book-list'),  # List and create books
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),  # Retrieve, update, delete a book
    path('books/create/', CreateView.as_view(), name='book-create'),  # Create a new book
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),  # Update a book
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),  # Delete a book
]