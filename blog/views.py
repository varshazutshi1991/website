from django.shortcuts import render, HttpResponseRedirect
from .models import Post, About, Travel
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import ContributeForm
from django.forms.models import modelformset_factory
from django.shortcuts import render, redirect

# Create your views here.

def post_list(request):
    post_details = Post.objects.all()
    #travel_details = Travel.objects.filter(id__in=Post.travel_category.through.objects.through.filter(post__in=post_details).values('id'))
    #travel_details = Travel.objects.filter(id__in=Post.travel_category.through.objects.filter(post__in=post_details).values('id'))

    travel_details =Post.travel_category.through.objects.all()
    food_details = Post.food_category.through.objects.all()
    return render(request, 'blog/home.html', context={"post_details": post_details, 'travel_details': travel_details,
                                                      'food_details': food_details})

def about(request):
    about_details = About.objects.all()
    return render(request, 'blog/about.html', {"about_details": about_details})

def category(request, travel_id):
    travel = Travel.objects.all()
    return render(request, 'blog/category.html', {"travel": travel, id: travel_id})

def travel_info(request, travel_id):
    travel_info = Travel.objects.get(id=travel_id)
    return render(request, 'blog/blog-single.html', {'travel_info': travel_info})

def user_contribution(request):
    if request.method == 'POST':
        form = ContributeForm(request.POST, action="{% url 'post_list' %}")
        if form.is_valid():
            u = form.save()
            return HttpResponseRedirect('about')
            #users = ContributeForm.objects.all()

            #return render(request, 'blog/home.html')



    else:
        form_class = ContributeForm

    return render(request, 'blog/contribution.html', {
        'form': form_class,
    })

    #user_contribute_field = Contribute.objects.all()
    # form =ContributeForm
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    # return render(request, 'blog/contribution.html', {'form': form}