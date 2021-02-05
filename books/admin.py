#books/admin.py
from django.contrib import admin
from .models import Book, Review

class ReviewInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    List_display = ("title", "author", "price",)

# Register your models here.
admin.site.register(Book, BookAdmin)