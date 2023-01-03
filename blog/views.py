from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post
from blog.models import Category
# Create your views here.

def base(request):
    return HttpResponseRedirect('home')

def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)

def posts(request, url):
    post = Post.objects.filter(url = url)
    cats = Category.objects.all()
    data = {
        'post':post,
        'cats':cats
    }
    return render(request, 'posts.html', data)

def cats(request, url):
    catg = Category.objects.get(url = url)
    post = Post.objects.filter(cat = catg)
    cats = Category.objects.all()
    data = {
        'post':post,
        'catg' :catg,
        'cats' :cats
    }
    return render(request, 'category.html', data)