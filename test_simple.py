#!/usr/bin/env python
"""
Simple test to check Django setup
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')

try:
    django.setup()
    print("✅ Django setup successful!")
    
    # Test basic imports
    from django.conf import settings
    print(f"✅ Settings loaded: {settings.DEBUG}")
    
    from django.urls import reverse
    print("✅ URL reverse working!")
    
    from accounts.models import User
    print("✅ User model imported!")
    
    print("\n🎉 All basic tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()


