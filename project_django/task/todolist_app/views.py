from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib import messages

from todolist_app.models import TaskList
from todolist_app.forms import TaskForm

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:   
        all_tasks = TaskList.objects.all
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def update_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Updated!"))
        return redirect('todolist')
    else:   
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'update.html', {'task_object': task_object})

def contact(request):
    context = {
        "contact_text":"Welcome Contact Page!",
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        "about_text":"Welcome About Page!",
    }
    return render(request, 'about.html', context)