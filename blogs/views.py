from django.shortcuts import render
from django.views.generic import DetailView, ListView
from blogs.models import *
from common.mixins import ViewMixin


class Posts(ListView, ViewMixin):
    model = Post
    template_name = 'blogs/posts.html'
    context_object_name = 'posts'
    active = 'posts'


class Tags(ListView, ViewMixin):
    model = Tag
    template_name = 'blogs/tags.html'
    context_object_name = 'tags'
    active = 'tags'


class Post(DetailView, ViewMixin):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'
    active = 'posts'


class Tag(DetailView, ViewMixin):
    model = Tag
    template_name = 'blogs/posts.html'
    context_object_name = 'tag'
    active = 'posts'
