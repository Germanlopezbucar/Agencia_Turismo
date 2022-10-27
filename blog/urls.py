from django.urls import path
from blog.views import  index, PostList

urlpatterns = [
    path('',index, name='index'),
    path('lista', PostList.as_view(), name='post-list'),
]