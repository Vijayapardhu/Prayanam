from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    path('', views.package_list, name='packages_list'),
    path('<int:package_id>/', views.package_detail, name='package_detail'),
    path('<int:package_id>/trip-details/', views.trip_details, name='trip_details'),
    path('<int:package_id>/calculate-price/', views.calculate_price, name='calculate_price'),
]
