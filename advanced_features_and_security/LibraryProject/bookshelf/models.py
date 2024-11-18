from django.db import models
#Importing the AbstractUser class from Django's auth models
from django.contrib.auth.models import AbstractUser
# Importing BaseUserManager to create a custom manager for user creation
from django.contrib.auth.models import BaseUserManager

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