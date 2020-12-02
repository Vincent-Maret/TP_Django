'''Manage django views'''
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task


def index(request):
    '''Return a list of tasks'''
    task_list = Task.objects.order_by('-created_date')[:10]
    return render(request, 'todo/index.html', {'task_list': task_list})


def edit(request, task_id):
    '''Return a task edition page'''
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/edit.html', {'task': task})


def add_task(request):
    '''Add a task in database'''
    task_content = request.POST['newTask']
    new_task = Task(content=task_content)
    new_task.save()
    return HttpResponseRedirect(reverse('todo:index'))


def finish_task(request, task_id):
    '''Set task.is_done to true'''
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))


def delete_task(request, task_id):
    '''Delete targeted task'''
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('todo:index'))


def update_task(request, task_id):
    '''Update task'''
    task = get_object_or_404(Task, pk=task_id)
    new_content = request.POST['updatedTask']
    task.content = new_content
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))
