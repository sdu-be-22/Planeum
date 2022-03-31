from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Comment
from multiprocessing import context
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
# Create your views here.

class PostListView(View):
    def get(self,request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        context = {'post_list':posts,
                   'form': form,
        }
        return render(request, 'newsfeed/post-list.html', context)

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

        return render(request, 'newsfeed/post-list.html', context)
    
class PostDetailView(View):      
    def get(self,request,pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)
        form = CommentForm()
        
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        
        return render(request, 'newsfeed/post-detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            
        comments = Comment.objects.filter(post=post).order_by('-created_on')
            
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'newsfeed/post-detail.html', context)
    

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'newsfeed/comment-delete.html'
    
    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})
