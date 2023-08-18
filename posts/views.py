from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
# Create your views here.
def index(request):
    post_list = Post.objects.all()
    context = {
        'post_list' : post_list,
    }
    return render(request, 'index.html', context)

def comment(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post':post,
    }
    return render(request, 'posts/comment.html', context)