from django.shortcuts import render
from .models import User, Post, Comment, Category

def index(request):
    return render(request, 'index.html')

def users(request):
    users_list = User.objects.all()
    return render(request, 'users.html', {'users': users_list})

def blogs(request):
    blogs_list = Post.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs_list})

def comments(request):
    comments_list = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments_list})

def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories_list})

def blogdetails(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    return render(request, 'blogdetails.html', {'blog': blog})