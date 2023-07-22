from django.shortcuts import render
from django.views.generic import ListView, DetailView
from news.models import Post

# Create your views here.
class PostsList(ListView):
    model = Post
    template_name = 'templates/news/allnews.html'
    context_object_name = 'allNews'

class PostDetail(DetailView):
    model = Post
    template_name = 'templates/news/news.html'
    context_object_name = 'news'