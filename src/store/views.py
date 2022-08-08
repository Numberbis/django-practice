from django.shortcuts import HttpResponse, get_object_or_404, render

from store.models import Book


def books(request):
    return render(request,"index.html",context={"book":Book.objects.all()})


def book(request, book_pk):
    b = get_object_or_404(Book, pk=book_pk)
    return render(request,"book.html",context={"book":b})
