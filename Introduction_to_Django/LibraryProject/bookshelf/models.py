from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"<strong>'{self.title}'</strong> authored by <strong>{self.author}</strong> and publsihed in (<strong>{self.publication_year}</strong>)"
