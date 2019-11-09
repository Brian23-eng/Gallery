from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from . models import Image, Location, Category

# Create your views here.
def photos(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    
    return render(request,'photos.html', {'images':images, 'locations':locations})

def search_results(request):
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, "search.html", {"message": message, "category":searched_image})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})
    
def location(request,location_id):
    try:
        location:location.objects.get(id = location_id)
    except DoesNotExit:
        raise Http404()
    return render(request, "details.html", {"location":location})
        
    
