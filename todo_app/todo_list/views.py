from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpRequest
from .forms import TodoForm
from .models import Todo


def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:home')
    form = TodoForm()
    return render(request, 'todo/create.html', context={'form': form})


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse('we home 😎')


def list_todos(request: HttpRequest) -> HttpResponse:
    print('listing all todos')
    todos = Todo.objects.all()[:10]  # Maybe find out how to get only a subset
    return render(request, 'todo/home.html', context={'todos': todos})


def delete(request: HttpRequest) -> HttpResponse:
    pass


def update(request: HttpRequest) -> HttpResponse:
    pass
