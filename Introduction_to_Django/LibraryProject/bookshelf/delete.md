# Delete Operation

**Task**: Delete the book you created and confirm the deletion by trying to retrieve all books again.

### Python Commands:
#### Command:
```python
>>> Book.objects.filter(title='Nineteen Eighty-Four').delete()
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
The first command deletes the record directly from the database using a filter. The `delete()` method returns a tuple showing the number of objects deleted, as seen in the output. The second command retrieves all records for the `Book` model. As shown in the output, the Book model contain no records.



