from django.shortcuts import render, HttpResponseRedirect
from .models import Post, About, Travel
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *
from django.forms.models import modelformset_factory

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


#@csrf_protect
# def travel_info(request, travel_id):
#     template = 'blog/blog-single.html'
#     ImageFormSet = modelformset_factory(Travel, form=ImageForm, extra=15)
#     if request.method == 'POST':
#         user_form = Travel(request.POST, prefix='form1')
#         formset = ImageFormSet(request.POST, request.FILES, queryset=Travel.objects.none(), prefix='form2')
#
#         if user_form.is_valid() and formset.is_valid():
#             # Save User form, and get user ID
#             a = user_form.save(commit=False)
#             a.save()
#
#             images = formset.save(commit=False)
#             for image in images:
#                 image.user = a
#                 image.save()
#
#             return HttpResponseRedirect('/success/')
#         else:
#             user_form = Travel(prefix='form1')
#             formset = ImageFormSet(queryset=Travel.objects.none(), prefix='form2')
#         return render(request, template, {'form_user':user_form,'formset':formset})