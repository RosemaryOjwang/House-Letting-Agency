from django.shortcuts import render, get_object_or_404, redirect
from .models import House_Location, House_Details, Image
from .forms import HouseForm, ImageForm, House_LocationForm
from django.contrib import messages

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
    return render(request,
                  'Agency/house-detail/detail.html',
                  {'detail': detail})



def index(request):
    context = {}
    return render(request, 'index.html', context)

def create_product(request):
    house_form =  HouseForm()
    image_form = ImageForm()

    if request.method == "POST":

        files = request.FILES.getlist('images')

        house_form = HouseForm(request.POST, request.FILES)
        if house_form.is_valid():
            detail = house_form.save(commit=False)
            detail.save()
            messages.success(request, "House Posted successfully")

            for file in files:
                Image.objects.create(detail=detail, images=file)
            return redirect('index')
    context = {"d_form": house_form, "I_form": image_form}
    return render(request, 'create.html', context)

