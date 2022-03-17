from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from .models import Post
# Create your views here.
def homepage(request):
    return render(request=request, template_name='home.html')
def yes(request):
    return HttpRequest("sss")



class PostListView(View):
    def get(self,request, *args, **kwargs):
        posts = Post.objects.all().order_by('created_on')
        context = {'post_list':posts,
        
        }
        return render(request,'home/post_list.html', context)