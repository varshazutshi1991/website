from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('about', views.about, name="about"),
    path('category/<int:travel_id>', views.category, name='category'),
    path('blog-single/<int:travel_id>', views.travel_info, name='travel_info'),
    #path('category', views.category, name='category')
]

