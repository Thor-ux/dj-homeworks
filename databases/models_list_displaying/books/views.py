from django.shortcuts import render, get_list_or_404
from .models import Book

def index(request):
    from django.http import HttpResponse
    return HttpResponse("Main page")

def all_books(request):
    books = Book.objects.all()
    return render(request, "books/all_books.html", {"books": books})

def books_by_date(request, pub_date):
    # request date
    books = get_list_or_404(Book, pub_date=pub_date)

    # previous date
    prev_date = (
        Book.objects
        .filter(pub_date__lt=pub_date)
        .order_by("-pub_date")
        .values_list("pub_date", flat=True)
        .first()
    )

    # next date
    next_date = (
        Book.objects
        .filter(pub_date__gt=pub_date)
        .order_by("pub_date")
        .values_list("pub_date", flat=True)
        .first()
    )

    context = {
        "books": books,
        "pub_date": pub_date,
        "prev_date": prev_date,
        "next_date": next_date,
    }

    return render(request, "books/books_by_date.html", context)