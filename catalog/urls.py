from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
        ), # переменная контекста в шаблоне 'index'

    path(
        'books/',
        views.BookInstanceListView.as_view(),
        name='books' # имя для ссылок, когда мы делаем "кнопки" в шаблонах
        ), # переменная контекста в шаблоне 'bookinstance_list'
    path(
        'search_results/',
        views.BookInstanceSearchResultsListView.as_view(),
        name='search_results' # имя для ссылок, когда мы делаем "кнопки" в шаблонах
        ), # переменная контекста в шаблоне 'bookinstance_list'

]