from django.urls import path
from . import views

urlpatterns = [
    path('owners/<int:pk>/', views.owner_detail, name='owner_detail'),
]