from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def edit(request, taskId):
    return HttpResponse("You're editing task %s." % taskId)
