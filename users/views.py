from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def owner_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/owner_detail.html',
                  {'user': user})
