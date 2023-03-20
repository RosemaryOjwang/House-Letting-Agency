from django.urls import path
from . import views

app_name = 'Houses'


urlpatterns = [
    path('<int:id>/<slug:slug>/', views.house_detail,
         name='house_detail'),
]