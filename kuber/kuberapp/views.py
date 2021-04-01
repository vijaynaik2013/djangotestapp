from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    kuberapp = Kuberapp.objects.all()
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'Tasks': kuberapp, 'form': form}
    return render(request,'kuberapp\list.html',context)

def updateTask(request,pk):
    kuberapp = Kuberapp.objects.get(id=pk)
    form = TaskForm(instance=kuberapp)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=kuberapp)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'kuberapp/update_task.html',context)

def deleteTask(request,pk):
    item = Kuberapp.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request,'kuberapp/delete.html',context)