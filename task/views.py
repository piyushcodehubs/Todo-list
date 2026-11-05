from django.shortcuts import render, redirect
from .models import Task
from django.contrib import  messages
# Create your views here.
def home(request):
  task = Task.objects.all()
  return render(request,'home.html',{'tasks':task})



def add_task(request):
  if request.method == 'POST':
    task = request.POST.get('task')

    if task and task.strip():
      Task.objects.create(
      task = task
    )

  return redirect('home')



def delete_taks(request,id):
  if request.method == 'POST':
    Task.objects.filter(id=id).delete()
    messages.success(request,'Task delete successfuly')

  return redirect('home')


def edit_task(request,id):
  task = Task.objects.get(id=id)
  if request.method == 'POST':
    new_task = request.POST.get('task')
    if new_task and new_task.strip():
      task.task = new_task.strip()
      task.save()
      messages.success(request,'Task update successfully')
      return redirect('home')
  
    messages.error(request, 'Task cannot be empty!')

  return render(request, 'edit.html', {'task': task})
