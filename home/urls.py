from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
    path('',views.index, name="home"),
    path('index',views.index, name="index"),
    path('aboutus',views.aboutus, name="aboutus"),
    path('Resume',views.Resume, name="Resume"),
    path('contact',views.contact, name="contact"),
    
]
