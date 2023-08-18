from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

from .forms import PostBaseForm, PostCreateForm

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_at')
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

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/new_post.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content = content,
            writer = request.user
        )
        return redirect('index')

# def post_create_form_view(request):
#     if request.method == 'GET':
#         #form = PostBaseForm()
#         form = PostCreateForm()
#         context = {'form':form}
#         return render(request, 'posts/new_post.html', context)
#     else:
#         form = PostBaseForm(request.POST, request.FILES)
#         if form.is_valid():
#             Post.objects.create(
#                 image=form.cleaned_data['image'],
#                 content = form.cleaned_data['content'],
#                 writer = request.user
#             )
#         else:
#             return redirect('posts:post-create')
#         return redirect('index')