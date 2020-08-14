from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


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


@login_required(login_url="login")
def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('blog-main')

    context = {
        'form': form,
    }
    return render(request, 'blog/post_form.html', context)
