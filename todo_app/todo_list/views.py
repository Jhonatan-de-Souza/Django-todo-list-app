from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import TodoForm
from .models import Todo
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST


@require_POST
def toggle_status(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo, id=id)
    todo.status = not todo.status
    todo.save()
    return redirect('todo_list:home')


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
    todos = Todo.objects.all().filter(status=False).order_by('-created_at')
    paginator = Paginator(todos, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'todo/home.html', context={'page_obj': page_obj})


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
