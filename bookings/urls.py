from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings_list, name='bookings_list'),
    path('create/<int:package_id>/', views.create_booking, name='create_booking'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('member/add/<int:booking_id>/', views.add_member, name='add_member'),
]
from . import views

urlpatterns = [
    path('', views.bookings_list, name='bookings_list'),
    path('create/<int:package_id>/', views.create_booking, name='create_booking'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('member/add/<int:booking_id>/', views.add_member, name='add_member'),
]
