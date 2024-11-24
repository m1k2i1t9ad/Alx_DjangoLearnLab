# api/urls.py

from django.urls import path,include
from .views import BookList
from rest_framework.routers import DefaultRouter  # Import DefaultRouter for routing
from .views import BookViewSet  # Import the BookViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookViewSet, CustomAuthToken  # Import the custom auth token view

# Create a router and register our BookViewSet with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the ViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('auth/', CustomAuthToken.as_view(), name='api-token-auth'),  # Token retrieval endpoint
    path('', include(router.urls)),  # Include the router URLs for all CRUD operations
]