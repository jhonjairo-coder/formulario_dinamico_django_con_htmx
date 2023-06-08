from django.shortcuts import render
from .forms import BookFormSet
from .forms import Author, Book, BookForm
from django.shortcuts import get_list_or_404, redirect, render

def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    formset = BookFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-book", pk=author.id)

    context = {
        "formset": formset,
        "author": author
    }

    return render(request, "create_book.html", context)

def create_book_form(request):
    context = {
        "form" : BookForm()
    }

    return render(request, "partials/book_form.html", context)
