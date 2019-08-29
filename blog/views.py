from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm


def logout_view(request):
    logout(request)
    redirect('post_list')

def post_list(request):
    qs = Post.objects.filter(published_date__isnull=False)
    # queryset 'qs' bringing all posts
    paginator = Paginator(qs, 4)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    template_name = 'post_list.html'
    # context = {'posts': qs} #basic context without pagination
    context = {'posts':posts}
    # context is python dictionary(key:value) - key is 'posts'; value is 'qs' or 'posts'
    return render(request, template_name, context)

def post_drafts(request):
    qs = Post.objects.filter(published_date__isnull=True)
    # queryset 'qs' bringing all posts
    paginator = Paginator(qs, 4)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    template_name = 'post_drafts.html'
    # context = {'posts': qs} #basic context without pagination
    context = {'posts':posts}
    # context is python dictionary(key:value) - key is 'posts'; value is 'qs' or 'posts'
    return render(request, template_name, context)
# CRUD functions

@login_required
def post_create(request): # create
    form = PostForm(request.POST)
    if form.is_valid():
        # post = form.save(commit=False) # to stop the save until dated 
        form.save()
        return redirect('post_list')
    else:
        form = PostForm()

    template_name = 'post_create.html'
    context = {'form': form}
    return render(request, template_name, context)

def post_detail(request, pk): # retrieve
    post = get_object_or_404(Post, pk=pk)
    template_name = 'post_detail.html'
    return render(request, template_name, {'post':post})

@login_required
def post_edit(request, pk): # update
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # post = form.save(commit=False) # to stop the save until dated 
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    template_name = 'post_edit.html'
    return render(request, template_name, {'form':form})

@login_required
def post_delete(request, pk): # delete
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
