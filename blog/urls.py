from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    # api to postComment
    path('postcomment', views.postcomment, name='postcomment'),
    
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]