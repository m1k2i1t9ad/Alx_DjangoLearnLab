from django import forms  # Import Django forms module
from .models import Book  # Import the Book model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model to use
        fields = ['title', 'author', 'published_date']  # Specify the fields to include in the form