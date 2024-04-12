from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from datetime import datetime

# Create your views here.
def index(request):
  blogs = Blog.objects.all()
  context = {"blog":blogs}
  return render(request,'index.html',context=context)

def post(request):
  return render(request,'post.html')

def details(request,id):
  blog = Blog.objects.get(id=id)
  return render(request,'details.html',{'blog':blog})

# def create(request):
#   blog = Blog.objects.create(
#     title=None,
   
#     creation_date=datetime.now(),
    
#   )
#   return redirect(f'/{blog.id}')
  
