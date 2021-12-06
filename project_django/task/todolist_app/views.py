from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from todolist_app.models import TaskList
from todolist_app.forms import TaskForm


# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:   
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

@login_required
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

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

@login_required
def uncompleted_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def index(request):
    context = {
        "index_text":"Welcome Index Page!",
    }
    return render(request, 'index.html', context)

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