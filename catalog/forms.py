from django import forms
from .models import BookInstance,Author

class BookAddForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['name','author','quantity']
        