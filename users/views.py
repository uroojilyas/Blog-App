from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
# Create your views/logics here
def register(request):
    form=UserCreationForm()
    return render(request,'register.html',{'form':form})

