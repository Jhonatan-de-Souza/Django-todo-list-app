from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
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


def update(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list:home')
    form = TodoForm(instance=todo)
    return render(request, 'todo/update.html', context={'form': form, 'todo': todo})


def delete(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list:home')
    return render(request, 'todo/delete.html', context={'todo': todo})
