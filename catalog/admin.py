from django.contrib import admin
from .models import BookInstance, Author

admin.site.register(BookInstance)
admin.site.register(Author)