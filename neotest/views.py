from django.shortcuts import render

# Create your views here.

from .models import Book

def get_books(request):
    return render('yourapp/books.html', request, {'books': Book.nodes.all()})