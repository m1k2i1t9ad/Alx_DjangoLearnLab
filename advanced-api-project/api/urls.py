from django.urls import path
from .views import AuthorList, BookList,BookDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/', BookList.as_view(), name='book-list'),          # List and create books
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),  # Retrieve, update, delete a book
]