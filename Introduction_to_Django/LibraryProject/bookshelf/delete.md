# Delete Operation

**Task**: Delete the book you created and confirm the deletion by trying to retrieve all books again.

### Python Commands:
#### Command:
```python
from bookshelf.models import Book

>>> book = Book.objects.get(title='Nineteen Eighty-Four')
>>> book.delete()
```
#### Output:
```python
(1, {'bookshelf.Book': 1})
```

#### Command:
```python
>>> Book.objects.all()
```
#### Output:
```python
<QuerySet []>
```


### Comment: 
- The first line simply imports the `Bokk` model c;ass from the Django app (`bookshelf`). 
- The second line retrieves the `Book` instance whose `title` is 'Nineteen Eighty Four'.
- The third then performs the actual deletion of the `book` instance from the database. The `delete()` method returns a tuple showing the number of objects deleted and its type, as seen in the output.
- The fourth line is expected to retrieve all remaining `Book` objects from the database. However, in this case, we had only one `Book` object which has been deleted already. Which is why the output of this command is an empty `QuerySet` (`<QuerySet []>`). This confirms that the deletion was successful.


