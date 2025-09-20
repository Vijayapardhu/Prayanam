#!/usr/bin/env python
"""
Script to add sample images to places
"""
import os
import sys
import django
import requests
from io import BytesIO
from django.core.files.base import ContentFile

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from places.models import Place

def add_place_images():
    """Add sample images to places"""
    print("Adding sample images to places...")
    
    # Sample image URLs (using free stock images)
    place_images = {
        'Tirupati Temple': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
        'Visakhapatnam Beach': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&h=600&fit=crop',
        'Araku Valley': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop',
        'Kurnool Caves': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop',
        'Rajahmundry': 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&h=600&fit=crop',
        'Charminar': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
        'Golconda Fort': 'https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&h=600&fit=crop',
        'Warangal Fort': 'https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&h=600&fit=crop',
        'Nagarjuna Sagar': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop',
        'Bhadrachalam Temple': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
    }
    
    for place_name, image_url in place_images.items():
        try:
            place = Place.objects.get(name=place_name)
            
            # Skip if image already exists
            if place.image:
                print(f"Image already exists for {place_name}")
                continue
            
            # Download image
            print(f"Downloading image for {place_name}...")
            response = requests.get(image_url, timeout=30)
            response.raise_for_status()
            
            # Create filename
            filename = f"{place_name.lower().replace(' ', '_')}.jpg"
            
            # Save image to place
            image_file = ContentFile(response.content)
            place.image.save(filename, image_file, save=True)
            
            print(f"✅ Added image for {place_name}")
            
        except Place.DoesNotExist:
            print(f"❌ Place not found: {place_name}")
        except requests.RequestException as e:
            print(f"❌ Error downloading image for {place_name}: {e}")
        except Exception as e:
            print(f"❌ Error processing {place_name}: {e}")
    
    print("\n✅ Image addition completed!")

if __name__ == '__main__':
    add_place_images()
