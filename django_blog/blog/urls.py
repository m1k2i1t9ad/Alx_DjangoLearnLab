from django.urls import path  # Import path function for URL patterns
from . import views  # Import views from the current app
from django.contrib.auth import views as auth_views  # Import built-in auth views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'
urlpatterns = [
    path('register/', views.register, name='register'),  # URL for registration
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL for login using Django's built-in view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL for logout using Django's built-in view
    path('profile/', views.profile, name='profile'),  # URL for user profile
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]