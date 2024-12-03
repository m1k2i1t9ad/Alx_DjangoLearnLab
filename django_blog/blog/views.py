from django.shortcuts import render, redirect  # Import render and redirect functions
from django.contrib.auth import login, authenticate  # Import login and authenticate methods
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .forms import CustomUserCreationForm  # Import the custom user creation form

# View for user registration
def register(request):
    if request.method == 'POST':  # Check if the request is a POST
        form = CustomUserCreationForm(request.POST)  # Create a form instance with the submitted data
        if form.is_valid():  # Check if the form is valid
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log in the user after registration
            return redirect('profile')  # Redirect to the profile page
    else:
        form = CustomUserCreationForm()  # Create a blank form for GET requests
    return render(request, 'registration/register.html', {'form': form})  # Render the registration template

# View for user profile
@login_required  # Ensure that the user is logged in to access this view
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})  # Render the profile template with user info