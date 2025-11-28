from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, FormView, CreateView, View
from .models import BookInstance
from .forms import BookAddForm, BookMoveForm

class BookInstanceListView(ListView):
    model = BookInstance
    context_object_name = 'bookinstance_list'
    template_name = 'bookinstance.html'

class BookInstanceSearchListView(ListView):
    model = BookInstance
    template_name = 'search_result_list.html'
    context_object_name = 'search_bookinstance_list'
 
    def get_queryset(self): # тут мы ограничиваем вывод данных из модели Bookinstance пользовательским зпросом
        query = self.request.GET.get('q')
        object_list = BookInstance.objects.filter(author__icontains=query)
        return object_list
    
class BookInstanceCreateView(CreateView):
    model = BookInstance
    form_class = BookAddForm
    template_name = 'bookadd.html'
    success_url = reverse_lazy('index')

    def form_valid(self,form):
        return super().form_valid(form)
    
class BookInstanceLoanView(FormView):
    model = BookInstance
    form_class = BookMoveForm
    template_name = 'bookloan.html'

    def get_success_url(self):
        messages.success(self.request, "Книга выдана!")
        return reverse_lazy('index')
    
    def form_valid(self, form):
        book = form.cleaned_data['name']
        requested_quantity = form.cleaned_data['quantity']
        
        if book.quantity >= requested_quantity:
            book.quantity -= requested_quantity
            book.save()
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Недостаточно книг.')
            return self.form_invalid(form)

class BookInstanceReturnView(FormView):
    model = BookInstance
    form_class = BookMoveForm
    template_name = 'bookreturn.html'

    def get_success_url(self):
        messages.success(self.request, "Книга принята!")
        return reverse_lazy('index')
    
    def form_valid(self, form):
        book = form.cleaned_data['name']
        requested_quantity = form.cleaned_data['quantity']
        
        book.quantity += requested_quantity
        book.save()
        return super().form_valid(form)
        # else:
        #     messages.error(self.request, 'Недостаточно книг.')
        #     return self.form_invalid(form)
