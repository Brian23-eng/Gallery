from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Image, Location, Category

# Create your views here.
def photos(request):
    images = Image.get_all_images()
    
    return render(request,'photos.html', {'images':images})
    
