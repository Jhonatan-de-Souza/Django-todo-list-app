from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpRequest
from .forms import TodoForm


def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:home')
    else:
        form = TodoForm()
    return render(request, 'todo/create.html', context={'form': form})


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse('we home 😎')
