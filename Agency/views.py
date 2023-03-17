from django.shortcuts import render, get_object_or_404, redirect
from .models import House_Location, House_Details
#from .forms import ImageForm
from django.views.decorators.http import require_POST


# Create your views here.
def house_list(request, location_slug=None):
    location = None
    locations = House_Location.objects.all()
    details = House_Details.objects.filter(available=True)
    if location_slug:
        location = get_object_or_404(House_Location,
                                     slug=location_slug)
        details = details.filter(location=location)
    return render(request,
                  'Agency/house-detail/list.html',
                  {'location': location,
                   'locations': locations,
                   'details': details})

def house_detail(request, id, slug):
    detail = get_object_or_404(House_Details,
                               id=id,
                               slug=slug,
                               available=True)
    #images = detail.house.filter()
    #form = ImageForm()
    return render(request,
                  'Agency/house-detail/detail.html',
                  {'detail': detail,
                   #'images': images,
                   #'form': form
                   })


#@require_POST
#def house_images(request, id):
#    detail = get_object_or_404(House_Details, 
#                               id=id)
#    images = None
#    form = ImageForm(data=request.POST)
#    if form.is_valid():
#        images = form.save(commit=False)
#        images.detail = detail
#        images.save()
#    return render(request, 'Agency/house-detail/images.html',
#                  {'detail': detail,
#                   'form': form,
#                   'images': images})
