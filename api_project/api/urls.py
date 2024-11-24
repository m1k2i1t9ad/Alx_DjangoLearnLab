# api/urls.py

from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter  # Import DefaultRouter for routing
from .views import BookViewSet  # Import the BookViewSet

# Create a router and register our BookViewSet with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the ViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),  # Include the router URLs for all CRUD operations
]