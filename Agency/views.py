from django.shortcuts import render, get_object_or_404
from Houses.models import House_Details
from django.core.paginator import Paginator

def frontpage(request):
    houses_list = House_Details.objects.exclude(available=False)
    paginator = Paginator(houses_list, 10)
    page_number = request.GET.get('page', 1)
    listing = paginator.get_page(page_number)

    return render(request, 'Agency/frontpage.html',
                  {'listing': listing})

def about(request):
    return render(request, 'Agency/about.html')



