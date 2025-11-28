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

    path(
        'loan/',
        views.BookInstanceLoanView.as_view(),
        name='book_loan'
        ),

    path(
        'return/',
        views.BookInstanceReturnView.as_view(),
        name='book_return'
        ),
]