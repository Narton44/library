from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.BookInstanceList.as_view(),
        name='index'
        ),

    path(
        'books/',
        views.BookInstanceSearchListView.as_view(),
        name='books' # имя для ссылок, когда мы делаем "кнопки" в шаблонах
        ),
]