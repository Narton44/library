from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.BookInstanceListView.as_view(),
        name='index'
        ),

    path(
        'search/',
        views.BookInstanceSearchListView.as_view(),
        name='books' # имя для ссылок, которые мы делаем из текста в шаблонах
        ),
    
    path(
        'create/',
        views.BookInstanceCreateView.as_view(),
        name='book_create'
        ),
]