from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    qs = Post.objects.filter(published_date__lte=timezone.now())
    # queryset 'qs' with field lookup using __ (double underscore) & lte (later than or equal to
    template_name = 'post_list.html'
    context = {'posts': qs}
    # context is python dictionary(key:value) - key is 'posts'; value is 'qs'
    return render(request, template_name, context)
    
