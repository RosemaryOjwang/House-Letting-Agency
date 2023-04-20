from django.urls import path
from . import views
from . views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('accounts/login/', SignUpView.as_view(), name='login'),
    path('accounts/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('user_admin/', views.user_admin, name='user_admin'),
    path('user_admin/add_house/', views.add_house, name='add_house'),
    path('user_admin/edit_house/<int:pk>/', views.edit_house, name='edit_house'),
    path('user_admin/delete_house/<int:pk>/', views.delete_house, name='delete_house'),
    path('owners/<int:pk>/', views.owner_detail, name='owner_detail'),
]