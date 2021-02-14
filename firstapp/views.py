from django.shortcuts import render
from django.http import HttpResponse
from .models import places

# Create your views here.
def index(request):
    obj=places.objects.all()
		
    return render(request, 'index.html',{'result':obj})
        # return HttpResponse('hello world')
def Home(request):
    return render (request,'Home.html')

def News(request):
    return render (request,'News.html')

def contact(request):
    return render (request,'contact.html')