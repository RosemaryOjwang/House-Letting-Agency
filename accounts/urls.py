from django.urls import path
from . import views
from . views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('accounts/login/', SignUpView.as_view(), name='login'),
    
    path('user_admin/', views.user_admin, name='user_admin'),
    path('user_admin/add_house/', views.add_house, name='add_house'),
    path('user_admin/edit_house/<int:pk>/', views.edit_house, name='edit_house'),
    path('user_admin/delete_house/<int:pk>/', views.delete_house, name='delete_house'),
    path('owners/<int:pk>/', views.owner_detail, name='owner_detail'),
]