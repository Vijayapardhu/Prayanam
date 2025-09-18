#!/usr/bin/env python
"""
Script to create sample data for the Prayanam travel platform
"""
import os
import sys
import django
from datetime import date, timedelta
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from accounts.models import User
from places.models import Place
from packages.models import Package
from bookings.models import Booking
from feedback.models import Feedback

def create_sample_data():
    """Create sample data for testing"""
    print("Creating sample data...")
    
    # Create sample places
    places_data = [
        {
            'name': 'Goa Beach Resort',
            'description': 'Beautiful beach resort with pristine beaches and water sports',
            'location': 'Goa, India',
            'latitude': 15.2993,
            'longitude': 74.1240,
            'season': 'summer',
            'is_featured': True
        },
        {
            'name': 'Kerala Backwaters',
            'description': 'Serene backwaters with houseboat experience',
            'location': 'Kerala, India',
            'latitude': 9.9312,
            'longitude': 76.2673,
            'season': 'monsoon',
            'is_featured': True
        },
        {
            'name': 'Rajasthan Desert',
            'description': 'Majestic desert with camel safaris and forts',
            'location': 'Rajasthan, India',
            'latitude': 26.9124,
            'longitude': 75.7873,
            'season': 'winter',
            'is_featured': False
        },
        {
            'name': 'Himalayan Trek',
            'description': 'Adventure trekking in the mighty Himalayas',
            'location': 'Himachal Pradesh, India',
            'latitude': 31.1048,
            'longitude': 77.1734,
            'season': 'summer',
            'is_featured': True
        }
    ]
    
    places = []
    for place_data in places_data:
        place, created = Place.objects.get_or_create(
            name=place_data['name'],
            defaults=place_data
        )
        places.append(place)
        if created:
            print(f"Created place: {place.name}")
    
    # Create sample packages
    packages_data = [
        {
            'name': 'Goa Beach Package',
            'place': places[0],
            'description': '3 days beach vacation with water sports',
            'base_price': Decimal('15000.00'),
            'duration_days': 3,
            'max_capacity': 4,
            'is_featured': True
        },
        {
            'name': 'Kerala Houseboat Experience',
            'place': places[1],
            'description': '2 days houseboat stay with traditional meals',
            'base_price': Decimal('12000.00'),
            'duration_days': 2,
            'max_capacity': 6,
            'is_featured': True
        },
        {
            'name': 'Rajasthan Desert Safari',
            'place': places[2],
            'description': '4 days desert adventure with camel safari',
            'base_price': Decimal('20000.00'),
            'duration_days': 4,
            'max_capacity': 8,
            'is_featured': False
        },
        {
            'name': 'Himalayan Adventure Trek',
            'place': places[3],
            'description': '5 days trekking adventure in the mountains',
            'base_price': Decimal('25000.00'),
            'duration_days': 5,
            'max_capacity': 10,
            'is_featured': True
        }
    ]
    
    packages = []
    for package_data in packages_data:
        package, created = Package.objects.get_or_create(
            name=package_data['name'],
            defaults=package_data
        )
        packages.append(package)
        if created:
            print(f"Created package: {package.name}")
    
    # Get admin user
    admin_user = User.objects.filter(role='admin').first()
    if not admin_user:
        print("No admin user found. Please run setup_admin.py first.")
        return
    
    # Create sample bookings
    booking_dates = [
        date.today() + timedelta(days=7),
        date.today() + timedelta(days=14),
        date.today() + timedelta(days=21),
        date.today() - timedelta(days=3),
        date.today() - timedelta(days=10)
    ]
    
    booking_statuses = ['pending', 'confirmed', 'completed', 'cancelled']
    
    for i, package in enumerate(packages):
        for j in range(2):  # Create 2 bookings per package
            booking_date = booking_dates[i % len(booking_dates)]
            status = booking_statuses[i % len(booking_statuses)]
            members_count = (i + 1) * 2
            total_price = package.base_price * members_count
            
            booking, created = Booking.objects.get_or_create(
                user=admin_user,
                package=package,
                booking_date=booking_date,
                defaults={
                    'members_count': members_count,
                    'total_price': total_price,
                    'status': status,
                    'special_requests': f'Sample booking {i+1}-{j+1}'
                }
            )
            if created:
                print(f"Created booking: {booking.package.name} - {booking.status}")
    
    # Create sample feedback
    feedback_data = [
        {
            'user': admin_user,
            'place': places[0],
            'rating': 5,
            'category': 'experience',
            'comment': 'Amazing beach experience! The resort was perfect and the staff was very friendly.',
            'is_helpful': True
        },
        {
            'user': admin_user,
            'package': packages[0],
            'rating': 4,
            'category': 'service',
            'comment': 'Great package with good value for money. Would recommend to others.',
            'is_helpful': True
        },
        {
            'user': admin_user,
            'place': places[1],
            'rating': 5,
            'category': 'location',
            'comment': 'The backwaters are absolutely beautiful. Peaceful and serene experience.',
            'is_helpful': False
        },
        {
            'user': admin_user,
            'package': packages[2],
            'rating': 3,
            'category': 'price',
            'comment': 'Good experience but a bit expensive for the facilities provided.',
            'is_helpful': True
        }
    ]
    
    for feedback_item in feedback_data:
        feedback, created = Feedback.objects.get_or_create(
            user=feedback_item['user'],
            place=feedback_item.get('place'),
            package=feedback_item.get('package'),
            defaults={
                'rating': feedback_item['rating'],
                'category': feedback_item['category'],
                'comment': feedback_item['comment'],
                'is_helpful': feedback_item['is_helpful']
            }
        )
        if created:
            print(f"Created feedback: {feedback.rating}/5 stars")
    
    print("\n✅ Sample data created successfully!")
    print(f"Created {len(places)} places")
    print(f"Created {len(packages)} packages")
    print(f"Created {Booking.objects.count()} bookings")
    print(f"Created {Feedback.objects.count()} feedback entries")

if __name__ == '__main__':
    create_sample_data()
"""
Script to create sample data for the Prayanam travel platform
"""
import os
import sys
import django
from datetime import date, timedelta
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from accounts.models import User
from places.models import Place
from packages.models import Package
from bookings.models import Booking
from feedback.models import Feedback

def create_sample_data():
    """Create sample data for testing"""
    print("Creating sample data...")
    
    # Create sample places
    places_data = [
        {
            'name': 'Goa Beach Resort',
            'description': 'Beautiful beach resort with pristine beaches and water sports',
            'location': 'Goa, India',
            'latitude': 15.2993,
            'longitude': 74.1240,
            'season': 'summer',
            'is_featured': True
        },
        {
            'name': 'Kerala Backwaters',
            'description': 'Serene backwaters with houseboat experience',
            'location': 'Kerala, India',
            'latitude': 9.9312,
            'longitude': 76.2673,
            'season': 'monsoon',
            'is_featured': True
        },
        {
            'name': 'Rajasthan Desert',
            'description': 'Majestic desert with camel safaris and forts',
            'location': 'Rajasthan, India',
            'latitude': 26.9124,
            'longitude': 75.7873,
            'season': 'winter',
            'is_featured': False
        },
        {
            'name': 'Himalayan Trek',
            'description': 'Adventure trekking in the mighty Himalayas',
            'location': 'Himachal Pradesh, India',
            'latitude': 31.1048,
            'longitude': 77.1734,
            'season': 'summer',
            'is_featured': True
        }
    ]
    
    places = []
    for place_data in places_data:
        place, created = Place.objects.get_or_create(
            name=place_data['name'],
            defaults=place_data
        )
        places.append(place)
        if created:
            print(f"Created place: {place.name}")
    
    # Create sample packages
    packages_data = [
        {
            'name': 'Goa Beach Package',
            'place': places[0],
            'description': '3 days beach vacation with water sports',
            'base_price': Decimal('15000.00'),
            'duration_days': 3,
            'max_capacity': 4,
            'is_featured': True
        },
        {
            'name': 'Kerala Houseboat Experience',
            'place': places[1],
            'description': '2 days houseboat stay with traditional meals',
            'base_price': Decimal('12000.00'),
            'duration_days': 2,
            'max_capacity': 6,
            'is_featured': True
        },
        {
            'name': 'Rajasthan Desert Safari',
            'place': places[2],
            'description': '4 days desert adventure with camel safari',
            'base_price': Decimal('20000.00'),
            'duration_days': 4,
            'max_capacity': 8,
            'is_featured': False
        },
        {
            'name': 'Himalayan Adventure Trek',
            'place': places[3],
            'description': '5 days trekking adventure in the mountains',
            'base_price': Decimal('25000.00'),
            'duration_days': 5,
            'max_capacity': 10,
            'is_featured': True
        }
    ]
    
    packages = []
    for package_data in packages_data:
        package, created = Package.objects.get_or_create(
            name=package_data['name'],
            defaults=package_data
        )
        packages.append(package)
        if created:
            print(f"Created package: {package.name}")
    
    # Get admin user
    admin_user = User.objects.filter(role='admin').first()
    if not admin_user:
        print("No admin user found. Please run setup_admin.py first.")
        return
    
    # Create sample bookings
    booking_dates = [
        date.today() + timedelta(days=7),
        date.today() + timedelta(days=14),
        date.today() + timedelta(days=21),
        date.today() - timedelta(days=3),
        date.today() - timedelta(days=10)
    ]
    
    booking_statuses = ['pending', 'confirmed', 'completed', 'cancelled']
    
    for i, package in enumerate(packages):
        for j in range(2):  # Create 2 bookings per package
            booking_date = booking_dates[i % len(booking_dates)]
            status = booking_statuses[i % len(booking_statuses)]
            members_count = (i + 1) * 2
            total_price = package.base_price * members_count
            
            booking, created = Booking.objects.get_or_create(
                user=admin_user,
                package=package,
                booking_date=booking_date,
                defaults={
                    'members_count': members_count,
                    'total_price': total_price,
                    'status': status,
                    'special_requests': f'Sample booking {i+1}-{j+1}'
                }
            )
            if created:
                print(f"Created booking: {booking.package.name} - {booking.status}")
    
    # Create sample feedback
    feedback_data = [
        {
            'user': admin_user,
            'place': places[0],
            'rating': 5,
            'category': 'experience',
            'comment': 'Amazing beach experience! The resort was perfect and the staff was very friendly.',
            'is_helpful': True
        },
        {
            'user': admin_user,
            'package': packages[0],
            'rating': 4,
            'category': 'service',
            'comment': 'Great package with good value for money. Would recommend to others.',
            'is_helpful': True
        },
        {
            'user': admin_user,
            'place': places[1],
            'rating': 5,
            'category': 'location',
            'comment': 'The backwaters are absolutely beautiful. Peaceful and serene experience.',
            'is_helpful': False
        },
        {
            'user': admin_user,
            'package': packages[2],
            'rating': 3,
            'category': 'price',
            'comment': 'Good experience but a bit expensive for the facilities provided.',
            'is_helpful': True
        }
    ]
    
    for feedback_item in feedback_data:
        feedback, created = Feedback.objects.get_or_create(
            user=feedback_item['user'],
            place=feedback_item.get('place'),
            package=feedback_item.get('package'),
            defaults={
                'rating': feedback_item['rating'],
                'category': feedback_item['category'],
                'comment': feedback_item['comment'],
                'is_helpful': feedback_item['is_helpful']
            }
        )
        if created:
            print(f"Created feedback: {feedback.rating}/5 stars")
    
    print("\n✅ Sample data created successfully!")
    print(f"Created {len(places)} places")
    print(f"Created {len(packages)} packages")
    print(f"Created {Booking.objects.count()} bookings")
    print(f"Created {Feedback.objects.count()} feedback entries")

if __name__ == '__main__':
    create_sample_data()
