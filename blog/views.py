from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import PostForm, TagForm

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    redirect_url = 'posts_list_url'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    redirect_url = 'tags_list_url'
