from django.shortcuts import render
# from django.db.models import Sum, F
# from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import BookInstance

class BookInstanceListView(ListView):
    model = BookInstance
