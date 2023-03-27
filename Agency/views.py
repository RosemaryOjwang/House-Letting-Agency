from django.shortcuts import render, get_object_or_404
from Houses.models import House_Location, House_Details
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger


def frontpage(request):
    houses = House_Details.objects.exclude(available=False)

    return render(request, 'Agency/frontpage.html',
                  {'houses': houses})

def about(request):
    return render(request, 'Agency/about.html')


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
                  {'location_pages': location_pages,
                   'locations': locations,
                   'houses': houses}) 

