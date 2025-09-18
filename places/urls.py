from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.places_list, name='places_list'),
    path('<int:place_id>/', views.place_detail, name='place_detail'),
    path('search/', views.search_places, name='search_places'),
    path('<int:place_id>/weather/', views.get_weather_data, name='get_weather_data'),
    path('popular/', views.popular_places, name='popular_places'),
    path('featured/', views.featured_places, name='featured_places'),
    path('category/<str:category>/', views.places_by_category, name='places_by_category'),
    path('state/<str:state>/', views.places_by_state, name='places_by_state'),
]
