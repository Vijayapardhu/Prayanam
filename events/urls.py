from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events_list, name='events_list'),
    path('package/<int:package_id>/', views.package_events, name='package_events'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),
]
