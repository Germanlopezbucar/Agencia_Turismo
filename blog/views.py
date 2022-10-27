from django.shortcuts import render
from blog.models import Configuracion, Post
from django.views.generic import ListView

def index(request):
    configuracion = Configuracion.objects.first()
    return render(request,'blog/index.html',{"configuracion":configuracion})

class PostList(ListView):
  model = Post

