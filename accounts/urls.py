from django.urls import path
from . import views
from . views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('accounts/login/', SignUpView.as_view(), name='login'),
    path('owners/<int:pk>/', views.owner_detail, name='owner_detail'),
]