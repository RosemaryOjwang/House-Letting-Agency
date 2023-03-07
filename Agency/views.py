from django.shortcuts import render, get_object_or_404
from .models import House_Location, House_Details

# Create your views here.
def house_list(request, locations_slug=None):
    location = None
    locations = House_Location.objects.all()
    details = House_Details.objects.filter(available=True)
    if locations_slug:
        location = get_object_or_404(House_Location,
                                     slug=locations_slug)
        details = details.filter(location=location)
    return render(request,
                  'Agency/house-details/list.html',
                  {'location': location,
                   'details': details})

def house_detail(request, id, slug):
    detail = get_object_or_404(House_Location,
                               id=id,
                               slug=slug,
                               available=True)
    return render(request,
                  'Agency/house-detail/detail.html',
                  {'detail': detail})

