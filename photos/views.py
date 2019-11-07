from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def photos(request):
    return render(request,'photos.html' )
    
