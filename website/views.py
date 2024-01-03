from django.shortcuts import render
from website.models import Post

def website_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "website/index.html", context)

def website_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "website/category.html", context)


def website_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }

    return render(request, "website/detail.html", context)