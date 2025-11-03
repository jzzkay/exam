from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('-created_date')
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.number_of_views += 1
    book.save(update_fields=['number_of_views'])
    return render(request, 'bookstore/book_detail.html', {'book': book})