# Update Operation

**Task**: Update the title of "1984" to "Nineteen Eighty-Four" and save the changes.

### Python Commands:

```python
>>> update_book = Book.objects.get(title='1984')
>>> update_book.title = 'Nineteen Eighty-Four'
>>> update_book.save()
>>> print(update_book.title)
```

**Output:**
```python
Nineteen Eighty-Four
```

### Comment: 
- This first command retrieves the `Book` instance from the database into memory, where the title is `'1984'`. 
- The second command updates the `title` attribute of the `Book` instance now in memory. However, it isn't updated in the database yet. 
- The third command is what saves the updated `Book` object to the database. Note that without the third command, the change to `title` stays only in memory and would not persist. 
- The last command simply prints the now updated value of the book's `title` field. This is done just to confirm that the update was successful.
