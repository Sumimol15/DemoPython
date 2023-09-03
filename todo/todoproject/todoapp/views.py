from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task'
class TaskDetailView(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'deletes.html'
    success_url = reverse_lazy('classhome')
# Create your views here.

def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        task=Task(name=name,priority=priority)
        task.save()
    return render(request,'home.html',{'task':task1})

#def details(request):
    #task=Task.objects.all()
   # return render(request,'detail.html',{'task':task})
def add(request):
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date_str = request.POST.get('date', '')

        # Convert the date string to a Python datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None

        task = Task(name=name, priority=priority, date=date)
        task.save()


   # return render(request,'home.html')
#def delete(request,taskid):
 #   task=Task.objects.get(id=taskid)
  #  if request.method=='POST':
   #     task.delete()
    #    return redirect('/')
    #return render(request,'delete.html',{'task': task})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)

    if request.method == 'POST':
        # Handle the deletion logic here
        task.delete()
        return redirect('/')  # Redirect to the desired page after deletion

    # Render the 'delete.html' template if the request method is GET
    return render(request, 'deletes.html', {'task': task})

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task
                                       })