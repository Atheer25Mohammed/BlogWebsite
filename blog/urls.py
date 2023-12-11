from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('Posts/', views.Posts, name='Posts'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blogdetails/<int:blog_id>/', views.blogdetails, name='blogdetails'),
]