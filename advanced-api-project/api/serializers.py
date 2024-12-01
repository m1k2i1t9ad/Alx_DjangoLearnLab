from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Fields to be serialized

    def validate_publication_year(self, value):
        """Validate that the publication year is not in the future."""
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model, including related books."""
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Fields to be serialized, including nested books