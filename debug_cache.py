#!/usr/bin/env python
"""
Debug script to check cache configuration
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings_production')
django.setup()

from django.conf import settings
from django.core.cache import cache

print("=== Cache Configuration Debug ===")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
print(f"Cache backend: {settings.CACHES['default']['BACKEND']}")
print(f"Cache location: {settings.CACHES['default']['LOCATION']}")

# Test cache
try:
    cache.set('test_key', 'test_value', 60)
    result = cache.get('test_key')
    print(f"Cache test: {'PASSED' if result == 'test_value' else 'FAILED'}")
    print(f"Cache result: {result}")
except Exception as e:
    print(f"Cache test: FAILED - {e}")

print("=== End Debug ===")
