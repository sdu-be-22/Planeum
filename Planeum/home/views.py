from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def homepage(request):
    return render(request=request, template_name='home.html')
def yes(request):
    return HttpRequest("sss")