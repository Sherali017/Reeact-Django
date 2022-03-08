from django.contrib import admin

from todos.models import TodoModel


@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'body']
