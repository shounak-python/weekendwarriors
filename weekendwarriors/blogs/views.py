from django.shortcuts import render
from blogs.author import (
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
    AuthorListView,
    AuthorDetailView,
)
from blogs.models import Blogs

# Create your views here.


class BlogListView(AuthorListView):
    model = Blogs


class BlogDetailView(AuthorDetailView):
    model = Blogs


class BlogCreateView(AuthorCreateView):
    model = Blogs
    fields = ["title", "content"]


class BlogUpdateView(AuthorUpdateView):
    model = Blogs
    fields = ["title", "content"]


class BlogDeleteView(AuthorDeleteView):
    model = Blogs