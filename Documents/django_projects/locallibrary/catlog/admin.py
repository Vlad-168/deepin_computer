from django.contrib import admin
from catlog.models import Author, Genre, Book,BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
