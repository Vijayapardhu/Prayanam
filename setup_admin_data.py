#!/usr/bin/env python
"""
Setup script for admin dashboard data
This script creates initial admin settings, roles, and sample data
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from django.contrib.auth import get_user_model
from admin_dashboard.models import (
    AdminSettings, AdminRole, AdminNotification, 
    SystemMaintenance, AdminDashboardWidget
)
from datetime import datetime, timedelta
import json

User = get_user_model()

def create_admin_settings():
    """Create initial admin settings"""
    settings_data = [
        {
            'key': 'site_name',
            'value': 'Prayanam Travel Platform',
            'setting_type': 'general',
            'description': 'Name of the travel platform',
            'is_active': True
        },
        {
            'key': 'site_description',
            'value': 'A comprehensive travel booking platform',
            'setting_type': 'general',
            'description': 'Description of the platform',
            'is_active': True
        },
        {
            'key': 'max_booking_days',
            'value': '30',
            'setting_type': 'booking',
            'description': 'Maximum days in advance for booking',
            'is_active': True
        },
        {
            'key': 'cancellation_hours',
            'value': '24',
            'setting_type': 'booking',
            'description': 'Hours before trip for free cancellation',
            'is_active': True
        },
        {
            'key': 'email_notifications',
            'value': 'true',
            'setting_type': 'email',
            'description': 'Enable email notifications',
            'is_active': True
        },
        {
            'key': 'smtp_host',
            'value': 'smtp.gmail.com',
            'setting_type': 'email',
            'description': 'SMTP server host',
            'is_active': True
        },
        {
            'key': 'smtp_port',
            'value': '587',
            'setting_type': 'email',
            'description': 'SMTP server port',
            'is_active': True
        },
        {
            'key': 'payment_gateway',
            'value': 'razorpay',
            'setting_type': 'payment',
            'description': 'Default payment gateway',
            'is_active': True
        },
        {
            'key': 'currency',
            'value': 'INR',
            'setting_type': 'payment',
            'description': 'Default currency',
            'is_active': True
        },
        {
            'key': 'maintenance_mode',
            'value': 'false',
            'setting_type': 'system',
            'description': 'Enable maintenance mode',
            'is_active': True
        },
        {
            'key': 'backup_frequency',
            'value': 'daily',
            'setting_type': 'system',
            'description': 'Database backup frequency',
            'is_active': True
        },
        {
            'key': 'api_rate_limit',
            'value': '1000',
            'setting_type': 'api',
            'description': 'API rate limit per hour',
            'is_active': True
        }
    ]
    
    for setting_data in settings_data:
        setting, created = AdminSettings.objects.get_or_create(
            key=setting_data['key'],
            defaults=setting_data
        )
        if created:
            print(f"Created setting: {setting.key}")
        else:
            print(f"Setting already exists: {setting.key}")

def create_admin_roles():
    """Create initial admin roles"""
    roles_data = [
        {
            'name': 'Super Admin',
            'description': 'Full access to all admin features',
            'permissions': [
                'view_dashboard', 'manage_users', 'manage_places', 'manage_packages',
                'manage_bookings', 'manage_feedback', 'manage_payments', 'view_analytics',
                'manage_settings', 'manage_notifications', 'export_data', 'bulk_actions',
                'view_audit_logs', 'manage_roles', 'system_maintenance'
            ],
            'is_active': True
        },
        {
            'name': 'Content Manager',
            'description': 'Manage content and bookings',
            'permissions': [
                'view_dashboard', 'manage_places', 'manage_packages', 'manage_bookings',
                'manage_feedback', 'view_analytics', 'export_data', 'bulk_actions'
            ],
            'is_active': True
        },
        {
            'name': 'User Manager',
            'description': 'Manage users and customer support',
            'permissions': [
                'view_dashboard', 'manage_users', 'manage_bookings', 'manage_feedback',
                'view_analytics', 'manage_notifications'
            ],
            'is_active': True
        },
        {
            'name': 'Analyst',
            'description': 'View analytics and reports',
            'permissions': [
                'view_dashboard', 'view_analytics', 'export_data'
            ],
            'is_active': True
        }
    ]
    
    for role_data in roles_data:
        role, created = AdminRole.objects.get_or_create(
            name=role_data['name'],
            defaults=role_data
        )
        if created:
            print(f"Created role: {role.name}")
        else:
            print(f"Role already exists: {role.name}")

def create_sample_notifications():
    """Create sample notifications"""
    notifications_data = [
        {
            'title': 'Welcome to Admin Dashboard',
            'message': 'Welcome to the Prayanam admin dashboard. You can now manage all aspects of the travel platform.',
            'notification_type': 'system',
            'priority': 'medium',
            'is_global': True,
            'is_read': False
        },
        {
            'title': 'System Update Available',
            'message': 'A new system update is available. Please review the changelog and schedule maintenance.',
            'notification_type': 'system',
            'priority': 'high',
            'is_global': True,
            'is_read': False
        },
        {
            'title': 'Backup Completed',
            'message': 'Daily database backup has been completed successfully.',
            'notification_type': 'system',
            'priority': 'low',
            'is_global': True,
            'is_read': True
        }
    ]
    
    for notification_data in notifications_data:
        notification, created = AdminNotification.objects.get_or_create(
            title=notification_data['title'],
            defaults=notification_data
        )
        if created:
            print(f"Created notification: {notification.title}")
        else:
            print(f"Notification already exists: {notification.title}")

def create_dashboard_widgets():
    """Create default dashboard widgets"""
    widgets_data = [
        {
            'name': 'user_stats',
            'widget_type': 'metric',
            'title': 'Total Users',
            'description': 'Total number of registered users',
            'configuration': json.dumps({
                'metric_type': 'count',
                'model': 'User',
                'color': 'blue'
            }),
            'position_x': 0,
            'position_y': 0,
            'width': 3,
            'height': 2,
            'is_active': True
        },
        {
            'name': 'booking_stats',
            'widget_type': 'metric',
            'title': 'Total Bookings',
            'description': 'Total number of bookings',
            'configuration': json.dumps({
                'metric_type': 'count',
                'model': 'Booking',
                'color': 'green'
            }),
            'position_x': 3,
            'position_y': 0,
            'width': 3,
            'height': 2,
            'is_active': True
        },
        {
            'name': 'revenue_chart',
            'widget_type': 'chart',
            'title': 'Revenue Over Time',
            'description': 'Revenue trends over the last 30 days',
            'configuration': json.dumps({
                'chart_type': 'line',
                'data_source': 'revenue_analytics',
                'time_range': '30d'
            }),
            'position_x': 0,
            'position_y': 2,
            'width': 6,
            'height': 4,
            'is_active': True
        },
        {
            'name': 'recent_activities',
            'widget_type': 'list',
            'title': 'Recent Activities',
            'description': 'Latest system activities',
            'configuration': json.dumps({
                'list_type': 'activities',
                'limit': 10
            }),
            'position_x': 6,
            'position_y': 0,
            'width': 6,
            'height': 6,
            'is_active': True
        }
    ]
    
    # Get the first admin user to assign as creator
    admin_user = User.objects.filter(role='admin').first()
    if not admin_user:
        print("No admin user found. Please create an admin user first.")
        return
    
    for widget_data in widgets_data:
        widget_data['created_by'] = admin_user
        widget, created = AdminDashboardWidget.objects.get_or_create(
            name=widget_data['name'],
            defaults=widget_data
        )
        if created:
            print(f"Created widget: {widget.title}")
        else:
            print(f"Widget already exists: {widget.title}")

def create_system_maintenance():
    """Create sample system maintenance records"""
    maintenance_data = [
        {
            'title': 'Scheduled Database Maintenance',
            'description': 'Regular database optimization and cleanup',
            'scheduled_start': datetime.now() + timedelta(days=7),
            'scheduled_end': datetime.now() + timedelta(days=7, hours=2),
            'is_public_notice': True,
            'public_message': 'The system will be under maintenance for 2 hours. We apologize for any inconvenience.',
            'status': 'scheduled'
        }
    ]
    
    # Get the first admin user to assign as creator
    admin_user = User.objects.filter(role='admin').first()
    if not admin_user:
        print("No admin user found. Please create an admin user first.")
        return
    
    for maintenance_item in maintenance_data:
        maintenance_item['created_by'] = admin_user
        maintenance, created = SystemMaintenance.objects.get_or_create(
            title=maintenance_item['title'],
            defaults=maintenance_item
        )
        if created:
            print(f"Created maintenance: {maintenance.title}")
        else:
            print(f"Maintenance already exists: {maintenance.title}")

def main():
    """Main setup function"""
    print("Setting up admin dashboard data...")
    
    # Create admin settings
    print("\n1. Creating admin settings...")
    create_admin_settings()
    
    # Create admin roles
    print("\n2. Creating admin roles...")
    create_admin_roles()
    
    # Create sample notifications
    print("\n3. Creating sample notifications...")
    create_sample_notifications()
    
    # Create dashboard widgets
    print("\n4. Creating dashboard widgets...")
    create_dashboard_widgets()
    
    # Create system maintenance
    print("\n5. Creating system maintenance records...")
    create_system_maintenance()
    
    print("\n✅ Admin dashboard setup completed successfully!")
    print("\nYou can now access the admin dashboard at: /admin-dashboard/")

if __name__ == '__main__':
    main()
