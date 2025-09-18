from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('create/', views.create_feedback, name='create_feedback'),
    path('<int:feedback_id>/', views.feedback_detail, name='feedback_detail'),
    path('<int:feedback_id>/edit/', views.edit_feedback, name='edit_feedback'),
    path('<int:feedback_id>/delete/', views.delete_feedback, name='delete_feedback'),
    path('place/<int:place_id>/', views.place_feedback, name='place_feedback'),
    path('package/<int:package_id>/', views.package_feedback, name='package_feedback'),
]
from . import views

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('create/', views.create_feedback, name='create_feedback'),
    path('<int:feedback_id>/', views.feedback_detail, name='feedback_detail'),
    path('<int:feedback_id>/edit/', views.edit_feedback, name='edit_feedback'),
    path('<int:feedback_id>/delete/', views.delete_feedback, name='delete_feedback'),
    path('place/<int:place_id>/', views.place_feedback, name='place_feedback'),
    path('package/<int:package_id>/', views.package_feedback, name='package_feedback'),
]
