#### 3. `update.md`

```markdown
# Update Operation

## Command
```python
book = Book.objects.get(title="1984")  # Retrieve the book first
book.title = "Nineteen Eighty-Four"
book.save()
