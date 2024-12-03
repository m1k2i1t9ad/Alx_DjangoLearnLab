from django import forms  # Import Django forms module
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for registration
from django.contrib.auth.models import User  # Import the User model

# Create a custom user registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field, making it required

    class Meta:
        model = User  # Specify the model to use
        fields = ('username', 'email', 'password1', 'password2')  # Define fields to include in the form