from django.shortcuts import render
from django.views import View
from .models import Post
from multiprocessing import context
from .forms import PostForm
from django.http import HttpResponse, JsonResponse
# Create your views here.

class PostListView(View):
    def get(self,request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        context = {'post_list':posts,
                   'form': form,
        }
        return render(request,'post-list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'post-list.html', context)    

# Create your views here.
