from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm


def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:home')
        else:
            print('fields are not filled out correctly')
    else:
        form = TodoForm()
    return render(request, 'todo/create.html', context={'form': form})


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse('WE HOME AGAINNNN 😎')
