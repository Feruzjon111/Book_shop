from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'number', 'genre')
    search_fields = ('title', 'author')
    filter_fields = ('price', 'number')
    ordering = ('id',)


admin.site.register(Book, BookAdmin)