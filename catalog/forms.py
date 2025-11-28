from django import forms
from .models import BookInstance

class BookAddForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['name','author','quantity']

class BookMoveForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['name', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Заменяем CharField на ModelChoiceField для выбора книги
        self.fields['name'] = forms.ModelChoiceField(
            queryset=BookInstance.objects.all(),
            label="Книга",
            empty_label="-- Выберите книгу --"
        )
