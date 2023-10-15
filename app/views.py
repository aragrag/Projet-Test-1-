from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'app/book_list.html', {'books': books})


def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)  # On recupere author par son ID
    books = Book.objects.filter(author=author)  # On recupere les livres de author
    return render(request, 'app/author.html', {'author': author, 'books': books})
