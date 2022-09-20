
from django.urls import path

from .views import *
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('archive.html/', archive, name='archive'),
    path('blog-details.html/', blog_details, name='blog_details'),
    path('category.html/', category, name='category'),
    path('contact.html/', contact, name='contact'),
    # path('index.html/', index, name='index'),
    path('css-single.html/', blog_single, name='css-single'),


]