from django.urls import path
from . import views
from .views import SignUpView #MyLoginView, RegisterView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', SignUpView.as_view(), name='login'),
    #path('login/', MyLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #path('register/', RegisterView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('user_admin/', views.user_admin, name='user_admin'),
    path('user_admin/add_house/', views.add_house, name='add_house'),
    path('user_admin/edit_house/<int:pk>/', views.edit_house, name='edit_house'),
    path('user_admin/delete_house/<int:pk>/', views.delete_house, name='delete_house'),
    path('owners/<int:pk>/', views.owner_detail, name='owner_detail'),
]