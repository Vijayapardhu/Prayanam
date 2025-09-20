from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    # Main dashboard
    path('', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    
    # User management
    path('users/', views.user_management, name='user_management'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    
    # Content management
    path('places/', views.place_management, name='place_management'),
    path('packages/', views.package_management, name='package_management'),
    path('bookings/', views.booking_management, name='booking_management'),
    path('feedback/', views.feedback_management, name='feedback_management'),
    
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
