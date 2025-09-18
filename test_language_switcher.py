#!/usr/bin/env python
"""
Test script for language switcher functionality
"""
import os
import django
from django.test import Client
from django.urls import reverse

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

def test_language_switcher():
    """Test the language switcher functionality"""
    client = Client()
    
    print("🧪 Testing Language Switcher...")
    print("=" * 50)
    
    # Test home page access
    print("\n1. Testing home page access...")
    response = client.get('/')
    print(f"   Status: {response.status_code}")
    print(f"   Language: {response.get('Content-Language', 'Not set')}")
    
    # Test language change to Telugu
    print("\n2. Testing language change to Telugu...")
    response = client.get('/language/te/')
    print(f"   Status: {response.status_code}")
    print(f"   Redirect: {response.url if hasattr(response, 'url') else 'No redirect'}")
    
    # Test home page after language change
    print("\n3. Testing home page after Telugu language change...")
    response = client.get('/')
    print(f"   Status: {response.status_code}")
    print(f"   Language: {response.get('Content-Language', 'Not set')}")
    
    # Test language change to Hindi
    print("\n4. Testing language change to Hindi...")
    response = client.get('/language/hi/')
    print(f"   Status: {response.status_code}")
    print(f"   Redirect: {response.url if hasattr(response, 'url') else 'No redirect'}")
    
    # Test home page after Hindi language change
    print("\n5. Testing home page after Hindi language change...")
    response = client.get('/')
    print(f"   Status: {response.status_code}")
    print(f"   Language: {response.get('Content-Language', 'Not set')}")
    
    # Test language change back to English
    print("\n6. Testing language change back to English...")
    response = client.get('/language/en/')
    print(f"   Status: {response.status_code}")
    print(f"   Redirect: {response.url if hasattr(response, 'url') else 'No redirect'}")
    
    print("\n✅ Language switcher test completed!")

if __name__ == "__main__":
    test_language_switcher()
