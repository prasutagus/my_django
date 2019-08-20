from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    qs = Post.objects.all() # query set 'qs'
    template_name = 'blog/post_list.html'
    context = {'posts': qs} #python dictionary - key is 'posts'; value is 'qs'
    return render(request, template_name, context)
    
