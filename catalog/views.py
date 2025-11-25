from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BookInstance, Author

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация количества книг и авторов
    num_bookinstances=BookInstance.objects.all().count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_bookinstances,'num_authors':num_authors},
    )



class BookInstanceListView(ListView):
    model = BookInstance
    context_object_name = 'bookinstance_list'
    template_name = 'templates/book_list.html'