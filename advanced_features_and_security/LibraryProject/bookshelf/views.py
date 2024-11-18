from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required  # Import decorator to enforce permission checks
from django.shortcuts import render, redirect, get_object_or_404  # Import shortcuts for rendering and redirecting
from .models import Book, Author  # Import Book and Author models from the current app

@permission_required('yourapp.can_view', raise_exception=True)  # Ensure the user has permission to view books
def book_list(request):
    """View to list all books, requires can_view permission."""
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/book_list.html', {'books': books})  # Render the book_list template with the books context

@permission_required('yourapp.can_create', raise_exception=True)  # Ensure the user has permission to create books
def add_book(request):
    """View to add a new book, requires can_create permission."""
    if request.method == 'POST':  # Check if the request method is POST (form submission)
        title = request.POST.get('title')  # Get the title from the submitted form data
        author_id = request.POST.get('author')  # Get the author ID from the form data
        published_date = request.POST.get('published_date')  # Get the published date from the form data

        if title and author_id and published_date:  # Basic validation to ensure all fields are filled
            author = get_object_or_404(Author, pk=author_id)  # Retrieve the author instance or return 404 if not found
            new_book = Book(title=title, author=author, published_date=published_date)  # Create a new book instance
            new_book.save()  # Save the new book to the database
            return redirect('book_list')  # Redirect to the list of books after saving

    return render(request, 'relationship_app/add_book.html')  # Render the add_book template for GET requests

@permission_required('yourapp.can_edit', raise_exception=True)  # Ensure the user has permission to edit books
def edit_book(request, pk):
    """View to edit an existing book, requires can_edit permission."""
    book = get_object_or_404(Book, pk=pk)  # Retrieve the book instance or return 404 if not found
    if request.method == 'POST':  # Check if the request method is POST (form submission)
        title = request.POST.get('title')  # Get the new title from the submitted form data
        author_id = request.POST.get('author')  # Get the new author ID from the form data
        published_date = request.POST.get('published_date')  # Get the new published date from the form data

        if title and author_id and published_date:  # Basic validation to ensure all fields are filled
            author = get_object_or_404(Author, pk=author_id)  # Retrieve the author instance or return 404 if not found
            book.title = title  # Update the book's title
            book.author = author  # Update the book's author
            book.published_date = published_date  # Update the book's published date
            book.save()  # Save the updated book to the database
            return redirect('book_list')  # Redirect to the list of books after saving

    return render(request, 'relationship_app/edit_book.html', {'book': book})  # Render the edit_book template with the book context

@permission_required('yourapp.can_delete', raise_exception=True)  # Ensure the user has permission to delete books
def delete_book(request, pk):
    """View to delete a book, requires can_delete permission."""
    book = get_object_or_404(Book, pk=pk)  # Retrieve the book instance or return 404 if not found
    if request.method == 'POST':  # Check if the request method is POST (form submission)
        book.delete()  # Delete the book from the database
        return redirect('book_list')  # Redirect to the list of books after deletion

    return render(request, 'relationship_app/delete_book.html', {'book': book})  # Render the delete_book template with the book context