from django import forms
from core.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ('name',)