from django.shortcuts import render, get_object_or_404
from Houses.models import House_Location, House_Details

def frontpage(request):
    houses = House_Details.objects.all()[0:8]

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
    return render(request,
                  'Agency/frontpage.html',
                  {'location': location,
                   'locations': locations,
                   'houses': houses}) 

