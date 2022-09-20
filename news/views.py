from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import News



class BlogListView(ListView):
    model = News
    template_name = 'blog/index.html'





def archive(request) -> render:
    return render(request, template_name='blog/archive.html')


def blog_details(request):
    return render(request, template_name='blog/blog-details.html')


def category(request) -> render:
    return render(request, template_name='blog/category.html')


def contact(request) -> render:
    return render(request, template_name='blog/contact.html')


def blog_single(request) -> render:
    return render(request, template_name='blog/blog-single.html')
