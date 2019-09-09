from .models import *
from .forms import ContributeForm
from django.shortcuts import render, redirect

# Create your views here.

def post_list(request):
    #post_details = Post.objects.all()
    travel_details =Post.travel_category.through.objects.all()
    food_details = Post.food_category.through.objects.all()
    return render(request, 'blog/header.html', context={"post_details": travel_details, 'travel_details': travel_details,
                                                      'food_details': food_details})

def about(request):
    about_details = About.objects.all()
    return render(request, 'blog/about.html', {"about_details": about_details})

def category(request):
    #travel = Travel.objects.all()
    return render(request, 'blog/category.html')

def blog_info(request, blog_id):
    blog_info = Blog.objects.get(id=blog_id)
    return render(request, 'blog/blog-single.html', {'blog_info': blog_info})


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

def base_site(request):
    return render(request, 'blog/base.html')


def blog_list(request):
    blog_details = Blog.objects.all() #using created manager in models
    return render(request, 'blog/home.html', {'blog_details': blog_details})

    #user_contribute_field = Contribute.objects.all()
    # form =ContributeForm
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    # return render(request, 'blog/contribution.html', {'form': form}