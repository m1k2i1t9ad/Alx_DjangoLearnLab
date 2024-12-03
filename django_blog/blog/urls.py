from django.urls import path  # Import path function for URL patterns
from . import views  # Import views from the current app
from django.contrib.auth import views as auth_views  # Import built-in auth views

urlpatterns = [
    path('register/', views.register, name='register'),  # URL for registration
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL for login using Django's built-in view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL for logout using Django's built-in view
    path('profile/', views.profile, name='profile'),  # URL for user profile
]