#!/usr/bin/env python
"""
Script to add sample images to events
This will download and assign appropriate images to events based on their type and location
"""

import os
import sys
import django
import requests
from PIL import Image
from io import BytesIO

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from events.models import Event
from django.core.files.base import ContentFile

def add_images_to_events():
    """Add sample images to events based on their type and content"""
    print("🖼️ Adding images to events...")
    
    events = Event.objects.all()
    updated_events = []
    
    # Image URLs based on event types and locations
    image_urls = {
        'temple': [
            'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
        ],
        'fort': [
            'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
        ],
        'valley': [
            'https://images.unsplash.com/photo-1506905925346-14b5e6d4c4b0?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1506905925346-14b5e6d4c4b0?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1506905925346-14b5e6d4c4b0?w=800&h=600&fit=crop',
        ],
        'cave': [
            'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
        ],
        'default': [
            'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1506905925346-14b5e6d4c4b0?w=800&h=600&fit=crop',
            'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=600&fit=crop',
        ]
    }
    
    for event in events:
        try:
            # Skip if event already has an image
            if event.image:
                continue
                
            print(f"Adding image to: {event.title}")
            
            # Determine image category based on event content
            event_lower = event.title.lower()
            place_lower = event.package.place.name.lower()
            
            if any(keyword in event_lower or keyword in place_lower for keyword in ['temple', 'darshan', 'pooja', 'aarti', 'spiritual']):
                category = 'temple'
            elif any(keyword in event_lower or keyword in place_lower for keyword in ['fort', 'historical', 'tour', 'exploration']):
                category = 'fort'
            elif any(keyword in event_lower or keyword in place_lower for keyword in ['valley', 'coffee', 'plantation', 'nature']):
                category = 'valley'
            elif any(keyword in event_lower or keyword in place_lower for keyword in ['cave', 'geological', 'adventure']):
                category = 'cave'
            else:
                category = 'default'
            
            # Select image based on day number and time slot
            image_index = (event.day_number + hash(event.time_slot)) % len(image_urls[category])
            image_url = image_urls[category][image_index]
            
            # Download and process image
            response = requests.get(image_url, timeout=30)
            if response.status_code == 200:
                # Process image
                img = Image.open(BytesIO(response.content))
                
                # Resize to standard size
                img = img.resize((800, 600), Image.Resampling.LANCZOS)
                
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save to BytesIO
                img_io = BytesIO()
                img.save(img_io, format='JPEG', quality=85)
                img_io.seek(0)
                
                # Create filename
                filename = f"{event.title.replace(' ', '_').lower()}_{event.id}.jpg"
                
                # Save to model
                event.image.save(
                    filename,
                    ContentFile(img_io.getvalue()),
                    save=True
                )
                
                updated_events.append(event)
                print(f"✅ Added image to: {event.title}")
                
            else:
                print(f"❌ Failed to download image for: {event.title}")
                
        except Exception as e:
            print(f"❌ Error adding image to {event.title}: {e}")
            continue
    
    print(f"\n🎉 Image addition completed!")
    print(f"📊 Summary:")
    print(f"   - Events processed: {len(events)}")
    print(f"   - Images added: {len(updated_events)}")
    print(f"   - Events now have images for better visual appeal")

def main():
    """Main function to add images to events"""
    print("🚀 Starting addition of images to events...")
    
    try:
        add_images_to_events()
        print("\n✅ Event images addition completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during event images addition: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
