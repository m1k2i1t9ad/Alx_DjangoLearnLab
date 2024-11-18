from django.db import models
#Importing the AbstractUser class from Django's auth models
from django.contrib.auth.models import AbstractUser
# Importing BaseUserManager to create a custom manager for user creation
from django.contrib.auth.models import BaseUserManager

from django.contrib.auth.models import User  # Import the User model for user authentication
from django.db.models.signals import post_save  # Import signal for post-save actions
from django.dispatch import receiver  # Import receiver to handle signals
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
#
# Defining a custom user model by extending AbstractUser
class CustomUser(AbstractUser):
    # Adding a date_of_birth field that allows null and blank values
    date_of_birth = models.DateField(null=True, blank=True)
    # Adding a profile_photo field to upload images, also allows null and blank
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # String representation of the user; returns the username
    def __str__(self):
        return self.username
        

# Defining a custom user manager to handle user creation
class CustomUserManager(BaseUserManager):
    # Method to create a regular user
    def create_user(self, username, password=None, **extra_fields):
        # Ensure the username is provided
        if not username:
            raise ValueError('The Username field must be set')  # Raise an error if username is missing
        # Create a user instance with the provided username and extra fields
        user = self.model(username=username, **extra_fields)
        # Set the user's password securely
        user.set_password(password)
        # Save the user instance to the database
        user.save(using=self._db)
        return user  # Return the created user

    # Method to create a superuser (admin)
    def create_superuser(self, username, password=None, **extra_fields):
        # Set extra fields to ensure the user is an admin
        extra_fields.setdefault('is_staff', True)  # User can access admin
        extra_fields.setdefault('is_superuser', True)  # User has all permissions
        # Call create_user to create the superuser
        return self.create_user(username, password, **extra_fields)
    
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)  # Field for the author's name with a max length of 100 characters

    def __str__(self):
        return self.name  # Return the name of the author when the object is printed

class Book(models.Model):
    title = models.CharField(max_length=200)  # Field for the book's title with a max length of 200 characters
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Foreign key relationship to the Author model
    published_date = models.DateField()  # Field for the book's published date

    class Meta:
        permissions = [  # Define custom permissions for the Book model
            ('can_view', 'Can view book'),  # Permission to view books
            ('can_create', 'Can create book'),  # Permission to create new books
            ('can_edit', 'Can edit book'),  # Permission to edit existing books
            ('can_delete', 'Can delete book'),  # Permission to delete books
        ]

    def __str__(self):
        return self.title  # Return the title of the book when the object is printed
