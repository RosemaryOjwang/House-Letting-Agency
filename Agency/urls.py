from .import views
from django.urls import path

app_name = 'Agency'

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('<slug:location_slug>/', views.house_list,
         name='house_list_by_location'),
]  