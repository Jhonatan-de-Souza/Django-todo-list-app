from django.shortcuts import render, redirect, HttpResponse
from .forms import TodoForm

# def create(request):
#     return render(request, template_name='todo/create.html')


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:home')
    else:
        form = TodoForm()
    return render(request, 'todo/create.html', {'form': form})


def home(request):
    return HttpResponse('WE HOME 😎')
