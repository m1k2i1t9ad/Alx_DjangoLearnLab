from django.db import models

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)  # Name of the author

class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()   # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  
    # Foreign key linking to the Author model; establishes a one-to-many relationship

    def __str__(self):
        return self.title  # Return the title of the book when the object is printed