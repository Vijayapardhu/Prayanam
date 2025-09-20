from django.urls import path
from . import views
from . import views_custom

app_name = 'admin_dashboard'

urlpatterns = [
    # Custom Admin Dashboard
    path('custom/', views_custom.custom_admin_dashboard, name='custom_admin_dashboard'),
    
    # Main dashboard
    path('', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    
    # User Management (Custom)
    path('users/', views_custom.user_management, name='user_management'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/', views_custom.user_detail, name='user_detail'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('users/<int:user_id>/activate/', views_custom.activate_user, name='activate_user'),
    path('users/<int:user_id>/deactivate/', views_custom.deactivate_user, name='deactivate_user'),
    
    # Place Management (Custom)
    path('places/', views_custom.place_management, name='place_management'),
    path('places/create/', views_custom.create_place, name='create_place'),
    path('places/<int:place_id>/', views_custom.place_detail, name='place_detail'),
    path('places/<int:place_id>/edit/', views_custom.edit_place, name='edit_place'),
    path('places/<int:place_id>/toggle-featured/', views_custom.toggle_featured_place, name='toggle_featured_place'),
    path('places/<int:place_id>/delete/', views_custom.delete_place, name='delete_place'),
    
    # Package Management (Custom)
    path('packages/', views_custom.package_management, name='package_management'),
    path('packages/create/', views.create_package, name='create_package'),
    path('packages/<int:package_id>/', views.package_detail, name='package_detail'),
    path('packages/<int:package_id>/edit/', views.edit_package, name='edit_package'),
    path('packages/<int:package_id>/delete/', views.delete_package, name='delete_package'),
    
    # Booking Management (Custom)
    path('bookings/', views_custom.booking_management, name='booking_management'),
    path('bookings/<int:booking_id>/', views_custom.booking_detail, name='booking_detail'),
    path('bookings/<int:booking_id>/edit/', views_custom.edit_booking, name='edit_booking'),
    path('bookings/<int:booking_id>/confirm/', views_custom.confirm_booking, name='confirm_booking'),
    path('bookings/<int:booking_id>/cancel/', views_custom.cancel_booking, name='cancel_booking'),
    
    # Event Management (Custom)
    path('events/', views_custom.event_management, name='event_management'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    
    # Payment Management (Custom)
    path('payments/', views_custom.payment_management, name='payment_management'),
    path('payments/<int:payment_id>/', views.payment_detail, name='payment_detail'),
    path('payments/<int:payment_id>/edit/', views.edit_payment, name='edit_payment'),
    path('payments/<int:payment_id>/delete/', views.delete_payment, name='delete_payment'),
    
    # Feedback Management (Custom)
    path('feedback/', views_custom.feedback_management, name='feedback_management'),
    path('feedback/<int:feedback_id>/', views.feedback_detail, name='feedback_detail'),
    path('feedback/<int:feedback_id>/edit/', views.edit_feedback, name='edit_feedback'),
    path('feedback/<int:feedback_id>/delete/', views.delete_feedback, name='delete_feedback'),
    
    # System management
    path('settings/', views.system_settings, name='system_settings'),
    path('settings/<int:setting_id>/edit/', views.edit_setting, name='edit_setting'),
    path('notifications/', views.notifications, name='notifications'),
    path('audit-logs/', views.audit_logs, name='audit_logs'),
    
    # Bulk operations
    path('bulk-operations/', views.bulk_operations, name='bulk_operations'),
    
    # Data management
    path('data-export/', views.data_export, name='data_export'),
    path('data-export/<int:export_id>/download/', views.download_export, name='download_export'),
    
    # API endpoints
    path('api/stats/', views.get_dashboard_stats, name='get_dashboard_stats'),
    path('api/notifications/<int:notification_id>/mark-read/', views.mark_notification_read, name='mark_notification_read'),
    path('api/bulk-actions/<str:action_id>/progress/', views.get_bulk_action_progress, name='get_bulk_action_progress'),
    path('api/notifications/count/', views.get_notification_count, name='get_notification_count'),
    path('api/recent-activities/', views.get_recent_activities, name='get_recent_activities'),
    path('api/recent-bookings/', views.get_recent_bookings, name='get_recent_bookings'),
    path('api/system-status/', views.get_system_status, name='get_system_status'),
]
