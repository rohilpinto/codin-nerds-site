from django.shortcuts import render
from .models import Post


def posts(request):
    posts = Post.objects.filter(active=True)

    context = {
        'posts': posts,
    }
    return render(request, 'blog/posts.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)
