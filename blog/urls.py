from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_list, name="post_list"),
    path('about', views.about, name="about"),
    path('category/', views.category, name='category'),
    path('blog-info/<int:blog_id>', views.blog_info, name='blog_info'),
    path('contribute/', views.user_contribution, name='contribution'),
    path('base', views.base_site, name='base')
    #path('category', views.category, name='category')
]

