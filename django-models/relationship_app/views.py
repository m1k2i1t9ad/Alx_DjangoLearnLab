from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.contrib.auth.decorators import permission_required
from .models import Book

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


# Function to check if user is an Admin
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

# Function to check if user is a Librarian
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

# Function to check if user is a Member
def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')  # Render the admin view template

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')  # Render the librarian view template

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')  # Render the member view template


@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        # Create a new book instance and save it
        if title and author and published_date:  # Basic validation
            new_book = Book(title=title, author=author, published_date=published_date)
            new_book.save()
            return redirect('book_list')  # Redirect to the book list view

    return render(request, 'relationship_app/add_book.html')  # Render the add book template

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        # Update the book instance
        if title and author and published_date:  # Basic validation
            book.title = title
            book.author = author
            book.published_date = published_date
            book.save()
            return redirect('book_detail', pk=book.pk)  # Redirect to the book detail view

    return render(request, 'relationship_app/edit_book.html', {'book': book})  # Render the edit book template

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list view

    return render(request, 'relationship_app/delete_book.html', {'book': book})  # Render the delete confirmation template