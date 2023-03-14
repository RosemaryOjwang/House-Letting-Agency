from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Agency'

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('<slug:location_slug>/', views.house_list, 
         name='house_list_by_location'),
    path('<int:id>/<slug:slug>/', views.house_detail,
          name='house_detail'),
    path('create_product', views.create_product, name='create'),
]