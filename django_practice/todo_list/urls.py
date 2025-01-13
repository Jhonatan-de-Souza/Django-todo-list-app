from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    path('create', views.create, name='create'),
    path('home', views.home, name='home')
]
