#!/usr/bin/env python
"""
Script to create sample data for Telugu states (Andhra Pradesh and Telangana)
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

def create_telugu_states_data():
    """Create sample data for Telugu states"""
    print("Creating Telugu states sample data...")
    
    # Create admin user if not exists
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@prayanam.com',
            'first_name': 'Admin',
            'last_name': 'User',
            'role': 'admin',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("Created admin user: admin / admin123")
    else:
        print("Admin user already exists")
    
    # Telugu states places data
    places_data = [
        # Andhra Pradesh
        {
            'name': 'Tirupati Temple',
            'description': 'Sacred Hindu temple dedicated to Lord Venkateswara, one of the most visited pilgrimage sites in the world',
            'location': 'Tirupati, Andhra Pradesh',
            'latitude': 13.6288,
            'longitude': 79.4192,
            'season': 'winter',
            'is_featured': True,
            'category': 'temples'
        },
        {
            'name': 'Visakhapatnam Beach',
            'description': 'Beautiful coastal city with pristine beaches, hills, and port city charm',
            'location': 'Visakhapatnam, Andhra Pradesh',
            'latitude': 17.6868,
            'longitude': 83.2185,
            'season': 'winter',
            'is_featured': True,
            'category': 'beaches'
        },
        {
            'name': 'Araku Valley',
            'description': 'Scenic hill station with coffee plantations, waterfalls, and tribal culture',
            'location': 'Araku Valley, Andhra Pradesh',
            'latitude': 18.3333,
            'longitude': 83.0000,
            'season': 'summer',
            'is_featured': True,
            'category': 'hills'
        },
        {
            'name': 'Kurnool Caves',
            'description': 'Ancient limestone caves with historical significance and natural formations',
            'location': 'Kurnool, Andhra Pradesh',
            'latitude': 15.8305,
            'longitude': 78.0364,
            'season': 'winter',
            'is_featured': False,
            'category': 'heritage'
        },
        {
            'name': 'Rajahmundry',
            'description': 'Cultural city on the banks of Godavari river with rich history and traditions',
            'location': 'Rajahmundry, Andhra Pradesh',
            'latitude': 17.0005,
            'longitude': 81.8040,
            'season': 'winter',
            'is_featured': False,
            'category': 'cultural'
        },
        
        # Telangana
        {
            'name': 'Charminar',
            'description': 'Iconic monument and mosque, symbol of Hyderabad with bustling markets around',
            'location': 'Hyderabad, Telangana',
            'latitude': 17.3616,
            'longitude': 78.4747,
            'season': 'winter',
            'is_featured': True,
            'category': 'heritage'
        },
        {
            'name': 'Golconda Fort',
            'description': 'Historic fort with magnificent architecture and sound and light show',
            'location': 'Hyderabad, Telangana',
            'latitude': 17.3833,
            'longitude': 78.4011,
            'season': 'winter',
            'is_featured': True,
            'category': 'heritage'
        },
        {
            'name': 'Warangal Fort',
            'description': 'Ancient fort with Kakatiya architecture and Thousand Pillar Temple',
            'location': 'Warangal, Telangana',
            'latitude': 17.9689,
            'longitude': 79.5941,
            'season': 'winter',
            'is_featured': True,
            'category': 'heritage'
        },
        {
            'name': 'Nagarjuna Sagar',
            'description': 'Dam and reservoir with Buddhist heritage sites and wildlife sanctuary',
            'location': 'Nagarjuna Sagar, Telangana',
            'latitude': 16.5720,
            'longitude': 79.3310,
            'season': 'winter',
            'is_featured': False,
            'category': 'heritage'
        },
        {
            'name': 'Bhadrachalam Temple',
            'description': 'Sacred temple dedicated to Lord Rama on the banks of Godavari river',
            'location': 'Bhadrachalam, Telangana',
            'latitude': 17.6667,
            'longitude': 80.8833,
            'season': 'winter',
            'is_featured': False,
            'category': 'temples'
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
    
    # Create packages for Telugu states
    packages_data = [
        {
            'name': 'Tirupati Pilgrimage Package',
            'place': places[0],  # Tirupati Temple
            'description': '2 days spiritual journey to Tirupati with darshan, accommodation, and meals',
            'base_price': Decimal('5000.00'),
            'duration_days': 2,
            'max_capacity': 4,
            'is_featured': True
        },
        {
            'name': 'Vizag Beach Holiday',
            'place': places[1],  # Visakhapatnam Beach
            'description': '3 days beach vacation with water sports, city tour, and local cuisine',
            'base_price': Decimal('8000.00'),
            'duration_days': 3,
            'max_capacity': 6,
            'is_featured': True
        },
        {
            'name': 'Araku Valley Hill Station',
            'place': places[2],  # Araku Valley
            'description': '2 days hill station retreat with coffee plantation tour and tribal village visit',
            'base_price': Decimal('6000.00'),
            'duration_days': 2,
            'max_capacity': 4,
            'is_featured': True
        },
        {
            'name': 'Hyderabad Heritage Tour',
            'place': places[5],  # Charminar
            'description': '2 days heritage tour covering Charminar, Golconda Fort, and old city markets',
            'base_price': Decimal('7000.00'),
            'duration_days': 2,
            'max_capacity': 6,
            'is_featured': True
        },
        {
            'name': 'Warangal Historical Package',
            'place': places[7],  # Warangal Fort
            'description': '2 days historical tour of Warangal with Thousand Pillar Temple and fort exploration',
            'base_price': Decimal('5500.00'),
            'duration_days': 2,
            'max_capacity': 4,
            'is_featured': False
        },
        {
            'name': 'Telangana Cultural Experience',
            'place': places[6],  # Golconda Fort
            'description': '3 days cultural immersion with heritage sites, local cuisine, and traditional arts',
            'base_price': Decimal('9000.00'),
            'duration_days': 3,
            'max_capacity': 8,
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
    
    # Create sample users
    users_data = [
        {
            'username': 'suresh_ap',
            'email': 'suresh@example.com',
            'first_name': 'Suresh',
            'last_name': 'Kumar',
            'role': 'tourist',
            'phone': '9876543210',
            'language_preference': 'te'
        },
        {
            'username': 'priya_tg',
            'email': 'priya@example.com',
            'first_name': 'Priya',
            'last_name': 'Reddy',
            'role': 'tourist',
            'phone': '9876543211',
            'language_preference': 'te'
        },
        {
            'username': 'ravi_hyderabad',
            'email': 'ravi@example.com',
            'first_name': 'Ravi',
            'last_name': 'Sharma',
            'role': 'tourist',
            'phone': '9876543212',
            'language_preference': 'en'
        }
    ]
    
    users = [admin_user]
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults=user_data
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"Created user: {user.username}")
        users.append(user)
    
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
                user=users[j % len(users)],
                package=package,
                booking_date=booking_date,
                defaults={
                    'members_count': members_count,
                    'total_amount': total_price,
                    'status': status,
                    'food_preference': 'veg' if j % 2 == 0 else 'non_veg',
                    'special_requests': f'Special request for {package.name} booking'
                }
            )
            if created:
                print(f"Created booking: {booking.user.username} - {package.name}")
    
    # Create sample feedback
    feedback_data = [
        {
            'user': users[1],
            'place': places[0],
            'rating': 5,
            'comment': 'Amazing spiritual experience! The temple is beautiful and well maintained.',
            'category': 'experience'
        },
        {
            'user': users[2],
            'place': places[1],
            'rating': 4,
            'comment': 'Great beach destination with good facilities. Highly recommended!',
            'category': 'location'
        },
        {
            'user': users[1],
            'package': packages[0],
            'rating': 5,
            'comment': 'Excellent package with good accommodation and food. Will book again!',
            'category': 'service'
        },
        {
            'user': users[2],
            'package': packages[3],
            'rating': 4,
            'comment': 'Good heritage tour with knowledgeable guide. Worth the money.',
            'category': 'experience'
        }
    ]
    
    for feedback_item in feedback_data:
        feedback, created = Feedback.objects.get_or_create(
            user=feedback_item['user'],
            place=feedback_item.get('place'),
            package=feedback_item.get('package'),
            defaults={
                'rating': feedback_item['rating'],
                'comment': feedback_item['comment'],
                'category': feedback_item['category']
            }
        )
        if created:
            print(f"Created feedback: {feedback.user.username} - {feedback.rating} stars")
    
    print("\n✅ Telugu states sample data created successfully!")
    print(f"📊 Created:")
    print(f"   - {len(places)} places (Andhra Pradesh & Telangana)")
    print(f"   - {len(packages)} travel packages")
    print(f"   - {len(users)} users (including admin)")
    print(f"   - {Booking.objects.count()} bookings")
    print(f"   - {Feedback.objects.count()} feedback entries")
    print(f"\n🔑 Admin Login: admin / admin123")
    print(f"👥 Test Users: suresh_ap, priya_tg, ravi_hyderabad (password: password123)")

if __name__ == '__main__':
    create_telugu_states_data()