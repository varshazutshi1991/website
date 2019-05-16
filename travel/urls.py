from django.conf.urls import url
from django.urls import path
from travel import views

urlpatterns = [
    path('', views.homepage, name="landing_page"),
    ]
