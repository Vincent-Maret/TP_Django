'''Manage django views'''
from django.http import HttpResponse
from .models import Task


def index(request):
    '''Return a list of tasks'''
    return HttpResponse(Task.objects.all())


def edit(request, task_id):
    '''Return a task edition page'''
    return HttpResponse("You're editing task %s." % task_id)
