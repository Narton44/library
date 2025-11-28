from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import BookInstance
from .forms import BookAddForm

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
    template_name = 'bookadd_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self,form):
        return super().form_valid(form)