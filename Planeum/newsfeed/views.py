from django.shortcuts import render
from django.db.models import Q 
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Comment
from userprofile.models import UserProfile
from multiprocessing import context
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.

class PostListView(LoginRequiredMixin, View):
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
    
class PostDetailView(LoginRequiredMixin, View):      
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
    

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'newsfeed/comment-delete.html'
    
    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    
class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)    

class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }

        return render(request, 'search.html', context) 