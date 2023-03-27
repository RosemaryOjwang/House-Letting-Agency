from django.shortcuts import render, get_object_or_404
from Houses.models import House_Location, House_Details

def frontpage(request):
    houses = House_Details.objects.exclude(available=False)

    return render(request, 'Agency/frontpage.html',
                  {'houses': houses})

def about(request):
    return render(request, 'Agency/about.html')



