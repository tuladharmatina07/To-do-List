from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    task = List.objects.all()

    form = ListForm()

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context ={'tasks': task , 'form': form}
    return render(request, 'list/home.html', context)

def updateTask(request, pk):
    task = List.objects.get(id=pk)
    form = ListForm(instance=task)

    if request.method=="POST":
        form= ListForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
        return redirect('/')

    context ={'form': form}

    return render(request, 'list/update_list.html', context)

def deleteTask(request, pk):

    item = List.objects.get(id=pk)
    if request.method== "POST":
        item.delete()
        return redirect('/')

    context= {'item': item }
    return render(request, 'list/delete.html', context)