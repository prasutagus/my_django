from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all()
    # queryset 'qs' bringing all posts
    template_name = 'post_list.html'
    context = {'posts': qs}
    # context is python dictionary(key:value) - key is 'posts'; value is 'qs'
    return render(request, template_name, context)

# CRUD
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

def post_delete(request, pk): # delete
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
