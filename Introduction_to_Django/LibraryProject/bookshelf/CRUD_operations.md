# Django Shell: CRUD Operations
This document captures the commands and outputs for performing Create, Retrieve, Update, and Delete operations on a Book model using the Django shell.

### Create Operation

Objective: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

**Command:**
```python
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

### Retrieve Operation

Objective: Retrieve and display all attributes of the book you just created.

**Commands:**
```python
>>> book = Book.objects.get(pk=1)
>>> print(book)
>>> print(book.title)
>>> print(book.author)
>>> print(book.publication_year)
```
**Outputs (for each of the command above respectively):** 
```python
'1984' authored by George Orwell
1984
George Orwell
1949
```

### Update Operation

Objective: Update the title of “1984” to “Nineteen Eighty-Four

**Command:**
```python
>>> book = Book.objects.get(title='1984')
>>> book.title = 'Nineteen Eighty-Four'
>>> book.save()
>>> print(book.title)
```

**Output (for the update commands above):**
```python
(1, {'bookshelf.Book': 1})
<QuerySet []>
```


### Delete Operation

Objective: Delete the book and confirm deletion by checking if any books exist.

**Command:**
```python
from bookshelf.models import Book

>>> book = Book.objects.get(title='Nineteen Eighty-Four')
>>> book.delete()
>>> Book.objects.all()
```
**Output (for the delete commands above):**
```python
(1, {'bookshelf.Book': 1})
<QuerySet []>
```
