from django.contrib import admin
from .models import Book
# Importing the UserAdmin class to customize admin for user management
from django.contrib.auth.admin import UserAdmin
# Importing the custom user model
from .models import CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Allow filtering by publication year

# Register the Book model with the custom admin options
admin.site.register(Book, BookAdmin)



# Creating a custom admin class for the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser  # Specify the model to be used in the admin

    # Extend existing fieldsets to include custom fields
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  # Add custom fields
    )
    # Extend the add_fieldsets for the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  # Add custom fields
    )

# Register the custom user model and admin class
admin.site.register(CustomUser, CustomUserAdmin)