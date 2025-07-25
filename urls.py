from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_dashboard, name='client_dashboard'),
    path('gecmis/', views.client_call_history, name='client_call_history'),
    path('odeme/', views.client_payment, name='client_payment'),
    path('giris/', views.login_view, name='login'),
    path('kayit/', views.register_view, name='register'),
    path('cikis/', views.logout_view, name='logout'),
    path('musteri/', views.client_dashboard),  # legacy, can be removed later
    path('saglayici/', views.provider_dashboard, name='provider_dashboard'),
]
