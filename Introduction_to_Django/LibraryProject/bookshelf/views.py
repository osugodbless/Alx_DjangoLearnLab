from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    result = "<br><br>".join([str(book) for book in books])
    return HttpResponse(f"<h1 style='color: blue'>List of Books in my Database:</h1>" +  result)
