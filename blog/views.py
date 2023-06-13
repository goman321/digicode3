from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Post


def show_post(request, slug):
    result = get_object_or_404(Post, slug=slug)

    return render(request, "pages/blog_single.html", context={"post": result})
