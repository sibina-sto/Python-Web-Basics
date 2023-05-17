from django.shortcuts import render, redirect

from OnlineLibrary.web.forms import CreateProfileForm, CreateBookForm, EditBookForm, DeleteBookForm, EditProfileForm, \
    DeleteProfileForm
from OnlineLibrary.web.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books,
    }

    return render(request, 'home-with-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBookForm()

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditBookForm(instance=book)

    context = {
        'profile': profile,
        'book': book,
        'form': form,
    }
    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)

    form = DeleteBookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()

    return redirect('home')


def show_book_details(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)

    context = {
        'profile': profile,
        'book': book,
    }
    return render(request, 'book-details.html', context)


def show_profile(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'delete-profile.html', context)


