#!/usr/bin/env python
"""
Script to set up admin user with proper password
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import User

User = get_user_model()

def setup_admin():
    """Set up admin user with proper password"""
    try:
        # Get the admin user
        admin_user = User.objects.get(username='admin')
        
        # Set password
        admin_user.set_password('admin123')
        admin_user.role = 'admin'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        
        print("✅ Admin user setup successfully!")
        print("Username: admin")
        print("Password: admin123")
        print("Role: admin")
        
    except User.DoesNotExist:
        print("❌ Admin user not found. Please create it first using:")
        print("python manage.py createsuperuser --username admin --email admin@example.com --noinput")
    except Exception as e:
        print(f"❌ Error setting up admin user: {e}")

if __name__ == '__main__':
    setup_admin()
"""
Script to set up admin user with proper password
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import User

User = get_user_model()

def setup_admin():
    """Set up admin user with proper password"""
    try:
        # Get the admin user
        admin_user = User.objects.get(username='admin')
        
        # Set password
        admin_user.set_password('admin123')
        admin_user.role = 'admin'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        
        print("✅ Admin user setup successfully!")
        print("Username: admin")
        print("Password: admin123")
        print("Role: admin")
        
    except User.DoesNotExist:
        print("❌ Admin user not found. Please create it first using:")
        print("python manage.py createsuperuser --username admin --email admin@example.com --noinput")
    except Exception as e:
        print(f"❌ Error setting up admin user: {e}")

if __name__ == '__main__':
    setup_admin()
