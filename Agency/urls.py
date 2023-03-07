from django.urls import path
from . import views

app_name = 'Agency'

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('<slug:locations_slug>/', views.house_list, name='house_list_by_location'),
    path('<int:id>/<slug:slug>/', views.house_detail, name='house_detail'),
]