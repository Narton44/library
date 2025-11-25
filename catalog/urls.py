from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.BookInstanceListView.as_view(),
        name='main'
        ), # переменная контекста в шаблоне 'main'

]