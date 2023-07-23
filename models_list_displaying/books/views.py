from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator
from books import converters


def books_view(request):
    books = Book.objects.all()    
    template = 'books/books_list.html'
    
    context = {
        'books' : books
    }
    return render(request, template, context)



def books(request, p_date):
    books_from_date = Book.objects.filter(pub_date=p_date)
    try:
        books_previous = Book.objects.filter(pub_date__lt=p_date).first()
    except Book.DoesNotExist:
        books_previous = None
    try: 
        books_next = Book.objects.filter(pub_date__gt=p_date).first()
    except Book.DoesNotExist:
        books_previous = None
    print(books_next)
    context = {
        'books' : books_from_date,
        'previous' : books_previous,
        'next' : books_next,
    }
    return render(request, 'books/pub_date.html', context)


