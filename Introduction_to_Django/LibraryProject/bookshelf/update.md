# Update Operation

**Task**: Update the title of "1984" to "Nineteen Eighty-Four" and save the changes.

### Python Commands:

```python
>>> update_book = Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')
```

### Comment: 
This command updates the record field specified in the filter. It also persist any changes made to the database.



