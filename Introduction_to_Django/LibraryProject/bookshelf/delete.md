#### 4. `delete.md`

```markdown
# Delete Operation

## Command
```python
book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book first
book.delete()
