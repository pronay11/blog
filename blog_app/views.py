from django.shortcuts import render
from .models import Post,Author,Category

def author_list(request):
   
    authors = Author.objects.all()
    return render(request,'blog_app/author_list.html',{'authors':authors})



def author_post(request,author_name):
    posts = Post.objects.filter(author=author_name)
    return render(request,'blog_app/author_post.html',{'posts':posts})

def post_list(request):
   
    info = Post.objects.all()
    context={
        'post_list':info
    }
    return render(request,'blog_app/post_list.html',context)

def post_detail(request,id):
   
    detail_info = Post.objects.get(id=id)
    context={
        'detail_info':detail_info
    }
    return render(request,'blog_app/post_detail.html',context)   

def categories_list(request):
   
    categories = Category.objects.all()
    return render(request,'blog_app/categories_list.html',{'category':categories})

def categories_post(request,category_name):
    posts = Post.objects.filter(category=category_name)
    return render(request,'blog_app/categories_post.html',{'posts':posts})



def home(request): 
     return render(request,'base.html')  

