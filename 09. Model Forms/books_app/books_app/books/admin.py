from django.contrib import admin

# Register your models here.
from books_app.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
