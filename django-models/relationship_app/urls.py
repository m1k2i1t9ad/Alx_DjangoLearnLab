from django.urls import path
from .views import register
from .views import list_books, LibraryDetailView, user_login,user_logout
from django.contrib.auth.views import LoginView, LogoutView  # Import class-based views for login/logout
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # URL for login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # URL for logout
    path('register/',register, name='register'),  # URL for registration
    
    path('admin/', admin_view, name='admin_view'),  # URL for Admin view
    path('librarian/', librarian_view, name='librarian_view'),  # URL for Librarian view
    path('member/', member_view, name='member_view'),  # URL for Member view
]
