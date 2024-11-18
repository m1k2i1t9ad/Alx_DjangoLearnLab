from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # Role field with choices

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Automatically save the UserProfile when the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    # Add other fields as necessary

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]

    def __str__(self):
        return self.title
    
    class Customer(AbstractUser):
         # Assign the custom user manager to the model
        objects = CustomUserManager()
        date_of_birth=models.DateField(null=True, blank=True)
        profile_photo=models.ImageField(upload_to='profile_photos/',null=True,blank=True) 
        
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