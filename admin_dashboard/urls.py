from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('users/', views.user_management, name='user_management'),
    path('places/', views.place_management, name='place_management'),
    path('packages/', views.package_management, name='package_management'),
    path('bookings/', views.booking_management, name='booking_management'),
    path('feedback/', views.feedback_management, name='feedback_management'),
    path('analytics/', views.analytics, name='analytics'),
    path('api/stats/', views.get_dashboard_stats, name='get_dashboard_stats'),
]
