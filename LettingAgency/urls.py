from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Agency.views import frontpage, about
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
    
    path('password_reset/', views.password_reset_request, name="password_reset"),
    #path("accounts/", include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),  
    path('', include('Houses.urls', namespace='Houses')),
    path('payments/', include('payments.urls', namespace='payments')),  
    #path('', include('Agency.urls', namespace='Agency')),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


