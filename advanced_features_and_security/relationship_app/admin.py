# Importing admin functionalities from Django
from django.contrib import admin

# Register your models here.

# Importing the UserAdmin class to customize admin for user management
from django.contrib.auth.admin import UserAdmin
# Importing the custom user model
from .models import CustomUser

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