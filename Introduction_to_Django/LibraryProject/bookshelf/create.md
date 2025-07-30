# Create Operation

**Task**: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

### Python Commands:

```python
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```
This command creates a `Book` instance and stores it in the variable book. This instance of `Book` is then saved to the database as a record of a single book.

### Comment: 
The book was successfully created and saved to the database.


