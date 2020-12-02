from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:task_id>', views.edit, name='editTask'),
    path('addTask', views.add_task, name='addTask')
]
