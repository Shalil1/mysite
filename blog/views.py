from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts=Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

# Create your views here.


def post_detail(request, year, month, day, post):
    post = get_object_or_404(post, slug=post,
                             statuse='published',
                             publish__year=year,
                             publish__month=month,
                             publish_day=day)
    return render(request, 'blog/ post/detail.html',{'post':post})
