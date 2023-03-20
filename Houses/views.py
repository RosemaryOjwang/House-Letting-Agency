from django.shortcuts import render, get_object_or_404
from .models import House_Details

# Create your views here.

def house_detail(request, id, slug):
    house = get_object_or_404(House_Details,
                              id=id,
                              slug=slug,
                              available=True)
    return render(request,
                  'houses/house_detail.html',
                  {'house': house})