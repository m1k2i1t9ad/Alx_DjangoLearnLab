#### 2. `retrieve.md`

```markdown
# Retrieve Operation

## Command
```python
all_books = Book.objects.all()
for b in all_books:
    print(b.title, b.author, b.publication_year)
