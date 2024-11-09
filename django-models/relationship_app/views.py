from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.http import HttpResponse

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Use the correct path
    context_object_name = 'library'

# Registration view
def register(request):
    if request.method == 'POST':  # Check if the request is a POST (form submission)
        form = UserCreationForm(request.POST)  # Create a form instance with the submitted data
        if form.is_valid():  # Check if the form is valid (all fields meet requirements)
            form.save()  # Save the new user to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()  # If the request is not POST, instantiate a blank form
    return render(request, 'relationship_app/register.html', {'form': form})  # Render the registration template with the form

# Login view
def user_login(request):
    if request.method == 'POST':  # Check if the request is a POST (form submission)
        username = request.POST['username']  # Get the username from the submitted form
        password = request.POST['password']  # Get the password from the submitted form
        user = authenticate(request, username=username, password=password)  # Authenticate the user
        if user is not None:  # If authentication is successful
            login(request, user)  # Log the user in
            return redirect('list_books')  # Redirect to the books list page after successful login
        else:
            return HttpResponse("Invalid login")  # Return an error response if login fails
    return render(request, 'relationship_app/login.html')  # Render the login template if the request is not POST

# Logout view
def user_logout(request):
    logout(request)  # Log the user out
    return render(request, 'relationship_app/logout.html')  # Render the logout confirmation template
