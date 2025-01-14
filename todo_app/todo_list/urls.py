from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
]
