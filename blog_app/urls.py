from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
   path('authors',author_list,name='authors'), 
   path('authors/<author_name>',author_post,name='author-post'), 
   path('categories',categories_list,name='categories'), 
   path('categories/<category_name>',categories_post,name='categories-post'), 
   path('post_list/',post_list,name='post_list'), 
   path('post_detail/<int:id>',post_detail,name='post_detail'),
   path('',home,name='home'),
    
]