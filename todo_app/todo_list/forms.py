from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo

        fields = ['title', 'status']

        labels = {
            'title': 'Title',
            'status': 'Status'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'model-form', 'placeholder': 'Task title'}),
            'status': forms.CheckboxInput(attrs={'class': 'model-form'}),
        }
