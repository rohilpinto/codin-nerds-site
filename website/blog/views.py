from django.shortcuts import render


def blog_main(request):
    context = {}
    return render(request, 'blog/blog.html', context)
