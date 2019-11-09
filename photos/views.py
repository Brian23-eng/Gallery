from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from . models import Image, Location, Category

# Create your views here.
def photos(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    
    return render(request,'photos.html', {'images':images, 'locations':locations})

def search_results(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',
                      {'images': images, 'message': message, 'categories': categories,
                       "locations": locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html', {"message": message})
    
def get_image_by_location(request,location_name):
    location_images = Image.filter_by_location(location_name)
    locations = Location.objects.all()
    location = location_name
    return render(request, 'location.html', {"location_images": location_images, "location": location, "locations":locations})

# def image(request, image_id):
#     try:
#         image = Image.get_image_by_id(image_id)
#     except DoesNotExists:
#         raise Http404()
#     return render(request, "details.html", {"image":image})
            


