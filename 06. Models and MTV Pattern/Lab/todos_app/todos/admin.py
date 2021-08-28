from django.contrib import admin

from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person, Category


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['text', 'owner']
    sortable_by = ['text']
    list_filter = ['owner']


admin.site.register(Todo, ToDoAdmin)
admin.site.register(Person)
admin.site.register(Category)
