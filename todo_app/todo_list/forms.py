from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo

        fields = ['title', 'description', 'status']

        labels = {
            'title': 'Title',
            'description': 'Description',
            'status': 'Status'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'model-form', 'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'class': 'model-form', 'placeholder': 'Task description'}),
            'status': forms.CheckboxInput(attrs={'class': 'model-form'}),
        }
