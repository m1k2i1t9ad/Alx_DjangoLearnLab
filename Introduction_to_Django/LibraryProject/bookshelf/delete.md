# Delete Operation

## Command
```python
from bookshelf.models import Book  # Import the Book model
book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book first
book.delete()
