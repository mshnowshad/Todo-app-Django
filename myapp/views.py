from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from .models import Task
from .forms import TaskForm
from django.contrib import messages










def task_list(request):
    lists = Task.objects.all()

    #add task in list
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('home')
    else:
        form = TaskForm()


    context = {
        "lists":lists,
        "form":form,
    }
    return render(request,'index.html',context)


def task_update(request, pe):
    task = get_object_or_404(Task, id=pe)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  # Pass the task instance here
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
        "task": task,
    }
    return render(request, 'update.html', context)


def task_delete(request,pd):
    task = Task.objects.get(id=pd)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('home')
    context = {}
    return render(request,'delete.html',context)