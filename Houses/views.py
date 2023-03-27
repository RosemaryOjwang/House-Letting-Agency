from django.shortcuts import render, get_object_or_404
from .models import House_Details, House_Location, MultipleImage
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger


# Create your views here.
def house_list(request, location_slug=None):
    location = None
    locations = House_Location.objects.all()
    houses = House_Details.objects.filter(available=True)
    if location_slug:
        location = get_object_or_404(House_Location,
                                     slug=location_slug)
        houses = houses.filter(location=location)
    paginator = Paginator(House_Location.objects.all(), 2)
    page = request.GET.get('page')
    location_pages = paginator.get_page(page)


    return render(request,
                  'Agency/frontpage.html',
                  {'location': location,
                   'locations': locations,
                   'houses': houses,
                   'location_pages': location_pages}) 
    
    #return render(request,
    #              'Agency/frontpage.html',
    #              {'location': location,
    #               'locations': locations,
    #               'houses': houses}) 



def house_detail(request, id, slug):
    house = get_object_or_404(House_Details,
                              id=id,
                              slug=slug,
                              available=True)
    images = MultipleImage.objects.filter(house=house)
    return render(request,
                  'houses/house_detail.html',
                  {'house': house,
                   'images': images})

