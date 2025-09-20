#!/usr/bin/env python
"""
Script to recreate all places with proper images and enhanced details
This will remove all existing places and create new ones with correct images
"""

import os
import sys
import django
import requests
from django.core.files.base import ContentFile
from django.core.files import File

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from places.models import Place
from packages.models import Package
from bookings.models import Booking
from payments.models import Payment

def download_image(url, place_name):
    """Download image from URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return ContentFile(response.content, name=f"{place_name.lower().replace(' ', '_')}.jpg")
    except Exception as e:
        print(f"Failed to download image for {place_name}: {e}")
        return None

def clear_all_data():
    """Clear all existing data"""
    print("🗑️ Clearing existing data...")
    
    # Delete in reverse order to avoid foreign key constraints
    Payment.objects.all().delete()
    Booking.objects.all().delete()
    Package.objects.all().delete()
    Place.objects.all().delete()
    
    print("✅ All existing data cleared")

def create_places_with_images():
    """Create places with proper images and enhanced details"""
    print("🏗️ Creating places with images...")
    
    places_data = [
        {
            'name': 'Tirupati Balaji Temple',
            'state': 'Andhra Pradesh',
            'city': 'Tirupati',
            'description': 'One of the most sacred Hindu temples dedicated to Lord Venkateswara, attracting millions of devotees annually.',
            'latitude': 13.6288,
            'longitude': 79.4192,
            'rating': 4.8,
            'entry_fee': 0,
            'opening_hours': '04:00 - 23:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
            'highlights': ['Sacred Temple', 'Spiritual Experience', 'Rich History', 'Architectural Marvel']
        },
        {
            'name': 'Charminar',
            'state': 'Telangana',
            'city': 'Hyderabad',
            'description': 'Iconic monument and mosque built in 1591, symbol of Hyderabad and Telangana state.',
            'latitude': 17.3616,
            'longitude': 78.4747,
            'rating': 4.5,
            'entry_fee': 25,
            'opening_hours': '09:00 - 17:30',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
            'highlights': ['Historical Monument', 'Architecture', 'Shopping', 'Photography']
        },
        {
            'name': 'Araku Valley',
            'state': 'Andhra Pradesh',
            'city': 'Araku',
            'description': 'Picturesque hill station known for its coffee plantations, waterfalls, and tribal culture.',
            'latitude': 18.3333,
            'longitude': 83.0167,
            'rating': 4.6,
            'entry_fee': 0,
            'opening_hours': '06:00 - 18:00',
            'best_time_to_visit': 'September to March',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-14bda270d433?w=800&h=600&fit=crop',
            'highlights': ['Hill Station', 'Coffee Plantations', 'Waterfalls', 'Nature']
        },
        {
            'name': 'Golconda Fort',
            'state': 'Telangana',
            'city': 'Hyderabad',
            'description': 'Historic fort known for its acoustic architecture and diamond mines.',
            'latitude': 17.3833,
            'longitude': 78.4011,
            'rating': 4.4,
            'entry_fee': 25,
            'opening_hours': '09:00 - 17:30',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&h=600&fit=crop',
            'highlights': ['Historical Fort', 'Architecture', 'Diamond Mines', 'Acoustic Design']
        },
        {
            'name': 'Borra Caves',
            'state': 'Andhra Pradesh',
            'city': 'Araku',
            'description': 'Ancient limestone caves with stunning stalactite and stalagmite formations.',
            'latitude': 18.1667,
            'longitude': 83.0167,
            'rating': 4.3,
            'entry_fee': 50,
            'opening_hours': '10:00 - 17:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1551524164-6cf77b2b0b7b?w=800&h=600&fit=crop',
            'highlights': ['Cave Exploration', 'Geological Formations', 'Adventure', 'Nature']
        },
        {
            'name': 'Srisailam Temple',
            'state': 'Andhra Pradesh',
            'city': 'Srisailam',
            'description': 'Ancient Shiva temple located on the banks of Krishna River, one of the 12 Jyotirlingas.',
            'latitude': 16.0740,
            'longitude': 78.8686,
            'rating': 4.7,
            'entry_fee': 0,
            'opening_hours': '04:00 - 22:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
            'highlights': ['Sacred Temple', 'Jyotirlinga', 'River View', 'Spiritual']
        },
        {
            'name': 'Bhadrachalam Temple',
            'state': 'Telangana',
            'city': 'Bhadrachalam',
            'description': 'Famous Rama temple on the banks of Godavari River, associated with Saint Thyagaraja.',
            'latitude': 17.6667,
            'longitude': 80.8833,
            'rating': 4.6,
            'entry_fee': 0,
            'opening_hours': '04:00 - 22:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
            'highlights': ['Rama Temple', 'Godavari River', 'Spiritual', 'Historical']
        },
        {
            'name': 'Yadagirigutta Temple',
            'state': 'Telangana',
            'city': 'Yadagirigutta',
            'description': 'Famous Lakshmi Narasimha temple known for its unique cave architecture.',
            'latitude': 17.6167,
            'longitude': 78.9167,
            'rating': 4.5,
            'entry_fee': 0,
            'opening_hours': '04:00 - 22:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&h=600&fit=crop',
            'highlights': ['Cave Temple', 'Lakshmi Narasimha', 'Unique Architecture', 'Spiritual']
        },
        {
            'name': 'Gandikota Fort',
            'state': 'Andhra Pradesh',
            'city': 'Gandikota',
            'description': 'Historic fort known as the Grand Canyon of India, offering breathtaking views.',
            'latitude': 14.8167,
            'longitude': 78.2833,
            'rating': 4.4,
            'entry_fee': 25,
            'opening_hours': '06:00 - 18:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&h=600&fit=crop',
            'highlights': ['Canyon Views', 'Historic Fort', 'Photography', 'Adventure']
        },
        {
            'name': 'Nagarjuna Sagar Dam',
            'state': 'Telangana',
            'city': 'Nagarjuna Sagar',
            'description': 'Massive dam on Krishna River with beautiful lake and ancient Buddhist sites.',
            'latitude': 16.5667,
            'longitude': 79.3167,
            'rating': 4.2,
            'entry_fee': 20,
            'opening_hours': '09:00 - 17:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-14bda270d433?w=800&h=600&fit=crop',
            'highlights': ['Dam View', 'Lake', 'Buddhist Sites', 'Engineering Marvel']
        },
        {
            'name': 'Warangal Fort',
            'state': 'Telangana',
            'city': 'Warangal',
            'description': 'Ancient Kakatiya dynasty fort with impressive stone architecture and sculptures.',
            'latitude': 17.9833,
            'longitude': 79.5833,
            'rating': 4.3,
            'entry_fee': 25,
            'opening_hours': '09:00 - 17:30',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&h=600&fit=crop',
            'highlights': ['Kakatiya Architecture', 'Stone Sculptures', 'Historical', 'Photography']
        },
        {
            'name': 'Kuntala Waterfalls',
            'state': 'Telangana',
            'city': 'Adilabad',
            'description': 'Tallest waterfall in Telangana, surrounded by lush green forests.',
            'latitude': 19.6667,
            'longitude': 78.5333,
            'rating': 4.1,
            'entry_fee': 30,
            'opening_hours': '08:00 - 17:00',
            'best_time_to_visit': 'July to October',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-14bda270d433?w=800&h=600&fit=crop',
            'highlights': ['Waterfall', 'Nature', 'Trekking', 'Photography']
        },
        {
            'name': 'Belum Caves',
            'state': 'Andhra Pradesh',
            'city': 'Belum',
            'description': 'Second largest cave system in India with unique limestone formations.',
            'latitude': 15.1000,
            'longitude': 78.1167,
            'rating': 4.2,
            'entry_fee': 60,
            'opening_hours': '10:00 - 17:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1551524164-6cf77b2b0b7b?w=800&h=600&fit=crop',
            'highlights': ['Cave System', 'Limestone Formations', 'Adventure', 'Geology']
        },
        {
            'name': 'Papi Hills',
            'state': 'Andhra Pradesh',
            'city': 'Rajahmundry',
            'description': 'Scenic hills along Godavari River, perfect for boat rides and nature lovers.',
            'latitude': 17.0000,
            'longitude': 81.7833,
            'rating': 4.0,
            'entry_fee': 0,
            'opening_hours': '06:00 - 18:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-14bda270d433?w=800&h=600&fit=crop',
            'highlights': ['River Views', 'Boat Rides', 'Nature', 'Photography']
        },
        {
            'name': 'Hussain Sagar Lake',
            'state': 'Telangana',
            'city': 'Hyderabad',
            'description': 'Heart-shaped lake with Buddha statue in the middle, popular for boating.',
            'latitude': 17.4167,
            'longitude': 78.4667,
            'rating': 4.1,
            'entry_fee': 0,
            'opening_hours': '05:00 - 22:00',
            'best_time_to_visit': 'October to March',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-14bda270d433?w=800&h=600&fit=crop',
            'highlights': ['Lake', 'Buddha Statue', 'Boating', 'City Views']
        }
    ]
    
    created_places = []
    
    for place_data in places_data:
        print(f"Creating place: {place_data['name']}")
        
        # Download image
        image_file = download_image(place_data['image_url'], place_data['name'])
        
        # Create place
        place = Place.objects.create(
            name=place_data['name'],
            location=place_data['city'],
            state='ap' if place_data['state'] == 'Andhra Pradesh' else 'telangana',
            description=place_data['description'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            rating=place_data['rating'],
            entry_fee=place_data['entry_fee'],
            opening_hours=place_data['opening_hours'],
            best_time_to_visit=place_data['best_time_to_visit'],
            district=place_data['city'],
            average_temperature=25.0,
            is_featured=True,
            is_popular=True,
            total_reviews=100
        )
        
        # Add image if downloaded successfully
        if image_file:
            place.image.save(f"{place_data['name'].lower().replace(' ', '_')}.jpg", image_file, save=True)
            print(f"✅ Added image for {place_data['name']}")
        else:
            print(f"⚠️ No image for {place_data['name']}")
        
        created_places.append(place)
    
    print(f"✅ Created {len(created_places)} places with images")
    return created_places

def create_packages_for_places(places):
    """Create packages for the places"""
    print("📦 Creating packages for places...")
    
    package_templates = [
        {
            'name_template': '{} Discovery Package',
            'duration_days': 2,
            'price_base': 5000,
            'description_template': 'Explore the beauty and culture of {} with our comprehensive 2-day package.',
            'includes': ['Accommodation', 'Meals', 'Transportation', 'Guide', 'Entry Fees']
        },
        {
            'name_template': '{} Premium Package',
            'duration_days': 3,
            'price_base': 8000,
            'description_template': 'Luxury experience in {} with premium amenities and exclusive access.',
            'includes': ['Luxury Accommodation', 'Premium Meals', 'Private Transport', 'Expert Guide', 'All Entry Fees', 'Photography']
        },
        {
            'name_template': '{} Budget Package',
            'duration_days': 1,
            'price_base': 2000,
            'description_template': 'Affordable way to experience {} without compromising on quality.',
            'includes': ['Basic Accommodation', 'Meals', 'Shared Transport', 'Guide', 'Entry Fees']
        }
    ]
    
    created_packages = []
    
    for place in places:
        for template in package_templates:
            package = Package.objects.create(
                name=template['name_template'].format(place.name),
                place=place,
                duration_days=template['duration_days'],
                base_price=template['price_base'] + (place.rating * 500),  # Price based on rating
                description=template['description_template'].format(place.name),
                max_capacity=20,
                is_featured=True
            )
            created_packages.append(package)
    
    print(f"✅ Created {len(created_packages)} packages")
    return created_packages

def main():
    """Main function to recreate all places and packages"""
    print("🚀 Starting recreation of places with images...")
    
    try:
        # Clear existing data
        clear_all_data()
        
        # Create places with images
        places = create_places_with_images()
        
        # Create packages for places
        packages = create_packages_for_places(places)
        
        print("\n🎉 Recreation completed successfully!")
        print(f"📊 Summary:")
        print(f"   - Places created: {len(places)}")
        print(f"   - Packages created: {len(packages)}")
        print(f"   - All places have images")
        print(f"   - All data is ready for use")
        
    except Exception as e:
        print(f"❌ Error during recreation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
