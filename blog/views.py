from .models import *
from .forms import ContributeForm, UserCommentForm
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def about(request):
    about_details = About.objects.all()
    return render(request, 'blog/about.html', {"about_details": about_details})

def category(request):
    #travel = Travel.objects.all()
    return render(request, 'blog/category.html')

def blog_info(request, blog_id):
    if request.method == "GET":
        blog_info = Blog.objects.get(id=blog_id)
        user_comments = UserComment.objects.filter().order_by("name")
        #user_comments = UserComment.objects.all()
        form = UserCommentForm
        return render(request, 'blog/blog-single.html', {'blog_info': blog_info, 'form': form,
                                                         'user_comments': user_comments})
    elif request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.save()
            return redirect('post_list')
    else:
        form = UserCommentForm
        #blog_info = Blog.objects.get(id=blog_id)
        return render(request, 'blog/blog-single.html', {'form': form})

    #blog_info = Blog.objects.get(id=blog_id)
    #return render(request, 'blog/blog-single.html', {'blog_info': blog_info})


def user_contribution(request):
    if request.method == 'POST':
        form = ContributeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = ContributeForm

    return render(request, 'blog/contribution.html', {'form': form})


def user_comment(request):
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.save()
            return redirect('blog_info')
    else:
        form = UserCommentForm
    return render(request, 'blog/blog-single.html', {'form': form})


def base_site(request):
    return render(request, 'blog/base.html')


def blog_list(request):
    blog_details = Blog.objects.all() #using created manager in models
    return render(request, 'blog/home.html', {'blog_details': blog_details})


