from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse, HttpResponseRedirect

def index(request):

    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('list')

    context = {
        'form' : form,
    }
    return render(request, 'form.html', context)

def list(request):
    allJobs = Job.objects.order_by('isCompleted', 'dateAdded')
    return render(request, 'list.html', {'allJobs' : allJobs})

def complete(request, todo_id):
    todo = Job.objects.get(pk=todo_id)
    todo.isCompleted = True
    todo.save()
    return redirect('list')

def delete(request, todo_id):
    todo = Job.objects.get(pk=todo_id)
    todo.delete()
    return redirect('list')
