from django.contrib import admin
from django.urls import path
from books.views import (create_book, create_book_form)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htmx/book-form', create_book_form, name='book-form'),
    path('<pk>/',create_book, name="create-book")
]
