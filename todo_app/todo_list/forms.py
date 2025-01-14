from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo

        fields = ['title', 'description']

        labels = {
            'title': 'Title',
            'description': 'Description'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'model-form', 'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'class': 'model-form', 'placeholder': 'Task description'}),
        }
