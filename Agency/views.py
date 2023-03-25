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
    
    paginator = Paginator(house_list, 2)
    page_number = request.GET.get('page')
    try:
        houses = paginator.page(page_number)
    except PageNotAnInteger:
        #If page_number is not an integer deliver the first page
        houses = paginator.page(1)
    except EmptyPage:
        #if page_number is out of range deliver last page of results
        houses = paginator.page(paginator.num_pages)

    return render(request,
                  'Agency/frontpage.html',
                  {'location': location,
                   'locations': locations,
                   'houses': houses}) 

