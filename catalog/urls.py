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

]