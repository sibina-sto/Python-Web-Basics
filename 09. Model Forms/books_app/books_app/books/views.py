from django.shortcuts import render, redirect

# Create your views here.
from books_app.books.forms import BookForm
from books_app.books.models import Book


def show_create_form(req, form):
    context = {
        'form': form,
    }
    return render(req, 'create.html', context)


def show_update_form(req, form):
    context = {
        'form': form,
    }
    return render(req, 'edit.html', context)


def index(req):
    context = {
        'books': Book.objects.all()
    }
    return render(req, 'index.html', context)


def create_book(req):
    if req.method == "GET":
        return show_create_form(req, BookForm())

    else:
        form = BookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_create_form(req, form)


def update_book(req, pk):
    book = Book.objects.get(pk=pk)
    if req.method == 'GET':
        form = BookForm(
            initial=book.__dict__,
        )
        return show_update_form(req, form)
    else:

        form = BookForm(
            req.POST,
            instance=book,
        )
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_update_form(req, form)
