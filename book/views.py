from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return JsonResponse({
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "publication_year": book.publication_year

    })
