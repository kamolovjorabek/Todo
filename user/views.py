from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def todo(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request,'todo.html', context)


def created_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    return render(request, 'created_todo.html')


def update_todo(request):
    todo_id = request.GET.get('id')
    todo = Todo.objects.filter(id=todo_id).first()
    context = {
        'todo': todo
    }
    if request.method == 'POST':
        form=TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    return render(request, 'update_todo.html', context)


def delete_todo(request):
    todo_id = request.GET.get('id')
    todo = Todo.objects.filter(id=todo_id).first()
    todo.delete()
    return redirect('todo')
