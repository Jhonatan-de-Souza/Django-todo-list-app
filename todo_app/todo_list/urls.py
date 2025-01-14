from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.list_todos, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
