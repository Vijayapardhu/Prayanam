from django.urls import path
from . import views

app_name = 'itinerary'

urlpatterns = [
    path('', views.itinerary_list, name='itinerary_list'),
    path('<int:itinerary_id>/', views.itinerary_detail, name='itinerary_detail'),
    path('create/', views.create_itinerary, name='create_itinerary'),
    path('<int:itinerary_id>/edit/', views.edit_itinerary, name='edit_itinerary'),
    path('<int:itinerary_id>/delete/', views.delete_itinerary, name='delete_itinerary'),
    path('<int:itinerary_id>/add-item/', views.add_item, name='add_item'),
    path('<int:itinerary_id>/remove-item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('templates/', views.template_list, name='template_list'),
    path('templates/<int:template_id>/use/', views.use_template, name='use_template'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('preferences/', views.set_preferences, name='set_preferences'),
]
