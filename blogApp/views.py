from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request,'index.html')

def post(request):
  return render(request,'post.html')

def create(request):
  return redirect('/')
  
