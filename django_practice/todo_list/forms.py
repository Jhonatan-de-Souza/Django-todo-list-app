from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']

        labels = {
            'title': 'Title',
            'description': 'Description',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of the task'}),

        }
