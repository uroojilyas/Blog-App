from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

def home(request):
    #key of this context will be available within template
    context={'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})