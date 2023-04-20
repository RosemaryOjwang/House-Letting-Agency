from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    #path('completed/session_id', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    #path('api/checkout-session/<id>/', views.stripe_webhook, name='stripe_webhook')
]