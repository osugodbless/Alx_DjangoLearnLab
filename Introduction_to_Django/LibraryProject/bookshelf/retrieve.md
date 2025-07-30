# Retrieve Operation

**Task**: Retrieve and display all attributes of the book that was created.

### Python Commands:

#### Command:
```python
>>> book = Book.objects.get(pk=1)
>>> print(book)
```
#### Output:
```python
'1984' authored by George Orwell
```

#### Command
```python
>>> print(book.title)
```
#### Output:
```python
1984
```

#### Command:
```python
>>> print(book.author)
```
#### Output:
```python
George Orwell
```

#### Command:
```python
>>> print(book.publication_year)
```
#### Output:
```python
1949
```

### Comment: 
The first command retrieved the specific book record using the `primary key` as filter. Then each attribute field of the specified record were printed using the print function.



