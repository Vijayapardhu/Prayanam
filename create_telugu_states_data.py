#!/usr/bin/env python
"""
Create sample data for Telugu states (Andhra Pradesh and Telangana) tourism places
"""
import os
import django
from decimal import Decimal
from django.core.files.base import ContentFile

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from places.models import Place
from packages.models import Package
from django.contrib.auth import get_user_model

User = get_user_model()

def create_telugu_states_places():
    """Create sample places for Telugu states"""
    
    # Andhra Pradesh Places
    ap_places = [
        {
            'name': 'Tirupati Balaji Temple',
            'location': 'Tirupati, Chittoor District',
            'description': 'The most visited religious site in the world, Sri Venkateswara Temple is dedicated to Lord Venkateswara. Known for its spiritual significance and architectural beauty.',
            'category': 'temples',
            'state': 'ap',
            'district': 'Chittoor',
            'latitude': 13.6288,
            'longitude': 79.4192,
            'season': 'winter',
            'average_temperature': 28.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 0,
            'opening_hours': '3:30 AM - 11:30 PM',
            'rating': 4.8,
            'total_reviews': 15000,
            'is_featured': True,
            'is_popular': True,
        },
        {
            'name': 'Araku Valley',
            'location': 'Araku Valley, Visakhapatnam District',
            'description': 'A picturesque hill station known for its coffee plantations, tribal culture, and scenic beauty. Famous for the Borra Caves and tribal museum.',
            'category': 'hills',
            'state': 'ap',
            'district': 'Visakhapatnam',
            'latitude': 18.3333,
            'longitude': 82.8667,
            'season': 'winter',
            'average_temperature': 22.0,
            'best_time_to_visit': 'November to February',
            'entry_fee': 50,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.5,
            'total_reviews': 8500,
            'is_featured': True,
            'is_popular': True,
        },
        {
            'name': 'Borra Caves',
            'location': 'Borra Village, Visakhapatnam District',
            'description': 'Ancient limestone caves with stunning stalactite and stalagmite formations. One of the largest cave systems in India.',
            'category': 'adventure',
            'state': 'ap',
            'district': 'Visakhapatnam',
            'latitude': 18.1667,
            'longitude': 82.9667,
            'season': 'winter',
            'average_temperature': 24.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 75,
            'opening_hours': '10:00 AM - 5:00 PM',
            'rating': 4.3,
            'total_reviews': 6200,
            'is_featured': True,
            'is_popular': False,
        },
        {
            'name': 'Belum Caves',
            'location': 'Belum Village, Kurnool District',
            'description': 'The second largest cave system in India, known for its underground passages, chambers, and natural formations.',
            'category': 'adventure',
            'state': 'ap',
            'district': 'Kurnool',
            'latitude': 15.1000,
            'longitude': 78.1167,
            'season': 'winter',
            'average_temperature': 30.0,
            'best_time_to_visit': 'November to February',
            'entry_fee': 60,
            'opening_hours': '10:00 AM - 5:00 PM',
            'rating': 4.2,
            'total_reviews': 4800,
            'is_featured': False,
            'is_popular': True,
        },
        {
            'name': 'Gandikota Fort',
            'location': 'Gandikota, Kadapa District',
            'description': 'Known as the Grand Canyon of India, this ancient fort offers breathtaking views of the Pennar River gorge.',
            'category': 'heritage',
            'state': 'ap',
            'district': 'Kadapa',
            'latitude': 14.8167,
            'longitude': 78.2833,
            'season': 'winter',
            'average_temperature': 32.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 25,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.4,
            'total_reviews': 3200,
            'is_featured': True,
            'is_popular': False,
        },
        {
            'name': 'Srisailam Temple',
            'location': 'Srisailam, Kurnool District',
            'description': 'One of the 12 Jyotirlingas, this ancient temple is dedicated to Lord Shiva and Goddess Parvati.',
            'category': 'temples',
            'state': 'ap',
            'district': 'Kurnool',
            'latitude': 16.0740,
            'longitude': 78.8680,
            'season': 'winter',
            'average_temperature': 28.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 0,
            'opening_hours': '4:30 AM - 10:00 PM',
            'rating': 4.6,
            'total_reviews': 7800,
            'is_featured': True,
            'is_popular': True,
        },
        {
            'name': 'Kolleru Lake',
            'location': 'Kolleru, West Godavari District',
            'description': 'One of the largest freshwater lakes in India, famous for bird watching and migratory birds.',
            'category': 'wildlife',
            'state': 'ap',
            'district': 'West Godavari',
            'latitude': 16.6500,
            'longitude': 81.2000,
            'season': 'winter',
            'average_temperature': 30.0,
            'best_time_to_visit': 'November to March',
            'entry_fee': 30,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.1,
            'total_reviews': 2100,
            'is_featured': False,
            'is_popular': False,
        },
        {
            'name': 'Pulicat Lake',
            'location': 'Pulicat, Nellore District',
            'description': 'Second largest brackish water lake in India, known for flamingos and other migratory birds.',
            'category': 'wildlife',
            'state': 'ap',
            'district': 'Nellore',
            'latitude': 13.4167,
            'longitude': 80.3167,
            'season': 'winter',
            'average_temperature': 28.0,
            'best_time_to_visit': 'November to March',
            'entry_fee': 20,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.0,
            'total_reviews': 1800,
            'is_featured': False,
            'is_popular': False,
        },
        {
            'name': 'Mangalagiri Temple',
            'location': 'Mangalagiri, Guntur District',
            'description': 'Ancient temple dedicated to Lord Panakala Narasimha Swamy, known for its unique architecture.',
            'category': 'temples',
            'state': 'ap',
            'district': 'Guntur',
            'latitude': 16.4333,
            'longitude': 80.5500,
            'season': 'winter',
            'average_temperature': 32.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 0,
            'opening_hours': '6:00 AM - 8:00 PM',
            'rating': 4.3,
            'total_reviews': 4500,
            'is_featured': False,
            'is_popular': True,
        },
        {
            'name': 'Undavalli Caves',
            'location': 'Undavalli, Guntur District',
            'description': 'Ancient rock-cut caves with beautiful sculptures and architecture from the 4th-5th century.',
            'category': 'heritage',
            'state': 'ap',
            'district': 'Guntur',
            'latitude': 16.5000,
            'longitude': 80.6000,
            'season': 'winter',
            'average_temperature': 32.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 25,
            'opening_hours': '9:00 AM - 5:00 PM',
            'rating': 4.2,
            'total_reviews': 2800,
            'is_featured': False,
            'is_popular': False,
        },
    ]
    
    # Telangana Places
    ts_places = [
        {
            'name': 'Charminar',
            'location': 'Hyderabad, Telangana',
            'description': 'Iconic monument and mosque, symbol of Hyderabad. Built in 1591, it is a masterpiece of Indo-Islamic architecture.',
            'category': 'heritage',
            'state': 'telangana',
            'district': 'Hyderabad',
            'latitude': 17.3616,
            'longitude': 78.4747,
            'season': 'winter',
            'average_temperature': 30.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 25,
            'opening_hours': '9:00 AM - 5:30 PM',
            'rating': 4.5,
            'total_reviews': 12500,
            'is_featured': True,
            'is_popular': True,
        },
        {
            'name': 'Golconda Fort',
            'location': 'Hyderabad, Telangana',
            'description': 'Ancient fort known for its acoustic architecture and diamond mines. Once the capital of the Qutb Shahi dynasty.',
            'category': 'heritage',
            'state': 'telangana',
            'district': 'Hyderabad',
            'latitude': 17.3833,
            'longitude': 78.4000,
            'season': 'winter',
            'average_temperature': 30.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 25,
            'opening_hours': '9:00 AM - 5:30 PM',
            'rating': 4.4,
            'total_reviews': 8900,
            'is_featured': True,
            'is_popular': True,
        },
        {
            'name': 'Warangal Fort',
            'location': 'Warangal, Telangana',
            'description': 'Ancient fort complex with beautiful stone gateways and temples. Capital of the Kakatiya dynasty.',
            'category': 'heritage',
            'state': 'telangana',
            'district': 'Warangal',
            'latitude': 17.9500,
            'longitude': 79.6000,
            'season': 'winter',
            'average_temperature': 32.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 20,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.3,
            'total_reviews': 5600,
            'is_featured': True,
            'is_popular': False,
        },
        {
            'name': 'Bhadrachalam Temple',
            'location': 'Bhadrachalam, Bhadradri Kothagudem District',
            'description': 'Famous temple dedicated to Lord Rama, built by Bhakta Ramadas. Known for its spiritual significance.',
            'category': 'temples',
            'state': 'telangana',
            'district': 'Bhadradri Kothagudem',
            'latitude': 17.6667,
            'longitude': 80.8833,
            'season': 'winter',
            'average_temperature': 28.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 0,
            'opening_hours': '4:30 AM - 9:00 PM',
            'rating': 4.6,
            'total_reviews': 7200,
            'is_featured': True,
            'is_popular': True,
        },
        {
            'name': 'Yadagirigutta Temple',
            'location': 'Yadagirigutta, Yadadri Bhuvanagiri District',
            'description': 'Ancient temple dedicated to Lord Lakshmi Narasimha, known for its healing powers and spiritual significance.',
            'category': 'temples',
            'state': 'telangana',
            'district': 'Yadadri Bhuvanagiri',
            'latitude': 17.6000,
            'longitude': 78.9500,
            'season': 'winter',
            'average_temperature': 30.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 0,
            'opening_hours': '4:00 AM - 9:30 PM',
            'rating': 4.5,
            'total_reviews': 6800,
            'is_featured': True,
            'is_popular': True,
        },
        {
            'name': 'Kaleshwaram Temple',
            'location': 'Kaleshwaram, Jayashankar Bhupalpally District',
            'description': 'Ancient temple dedicated to Lord Shiva, located at the confluence of Godavari and Pranahita rivers.',
            'category': 'temples',
            'state': 'telangana',
            'district': 'Jayashankar Bhupalpally',
            'latitude': 18.8000,
            'longitude': 79.9000,
            'season': 'winter',
            'average_temperature': 32.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 0,
            'opening_hours': '6:00 AM - 8:00 PM',
            'rating': 4.2,
            'total_reviews': 3400,
            'is_featured': False,
            'is_popular': False,
        },
        {
            'name': 'Pakhal Lake',
            'location': 'Warangal, Telangana',
            'description': 'Artificial lake built in 1213 AD, surrounded by hills and forests. Perfect for boating and bird watching.',
            'category': 'wildlife',
            'state': 'telangana',
            'district': 'Warangal',
            'latitude': 17.9500,
            'longitude': 79.9500,
            'season': 'winter',
            'average_temperature': 30.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 30,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.1,
            'total_reviews': 2200,
            'is_featured': False,
            'is_popular': False,
        },
        {
            'name': 'Kawal Wildlife Sanctuary',
            'location': 'Jannaram, Mancherial District',
            'description': 'Wildlife sanctuary known for its diverse flora and fauna, including tigers, leopards, and various bird species.',
            'category': 'wildlife',
            'state': 'telangana',
            'district': 'Mancherial',
            'latitude': 19.0000,
            'longitude': 79.5000,
            'season': 'winter',
            'average_temperature': 28.0,
            'best_time_to_visit': 'November to March',
            'entry_fee': 50,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.0,
            'total_reviews': 1800,
            'is_featured': False,
            'is_popular': False,
        },
        {
            'name': 'Medak Cathedral',
            'location': 'Medak, Telangana',
            'description': 'Largest church in Asia, built in Gothic architecture. Known for its beautiful stained glass windows.',
            'category': 'heritage',
            'state': 'telangana',
            'district': 'Medak',
            'latitude': 18.0333,
            'longitude': 78.2667,
            'season': 'winter',
            'average_temperature': 30.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 0,
            'opening_hours': '7:00 AM - 6:00 PM',
            'rating': 4.2,
            'total_reviews': 3100,
            'is_featured': False,
            'is_popular': False,
        },
        {
            'name': 'Nagarjuna Sagar Dam',
            'location': 'Nagarjuna Sagar, Nalgonda District',
            'description': 'One of the largest masonry dams in the world, built across the Krishna River. Offers scenic views and boating.',
            'category': 'adventure',
            'state': 'telangana',
            'district': 'Nalgonda',
            'latitude': 16.5833,
            'longitude': 79.3167,
            'season': 'winter',
            'average_temperature': 32.0,
            'best_time_to_visit': 'October to March',
            'entry_fee': 20,
            'opening_hours': '6:00 AM - 6:00 PM',
            'rating': 4.3,
            'total_reviews': 4200,
            'is_featured': True,
            'is_popular': False,
        },
    ]
    
    # Create places
    all_places = ap_places + ts_places
    created_places = []
    
    for place_data in all_places:
        place, created = Place.objects.get_or_create(
            name=place_data['name'],
            defaults=place_data
        )
        if created:
            print(f"✅ Created place: {place.name}")
        else:
            print(f"⏭️  Place already exists: {place.name}")
        created_places.append(place)
    
    return created_places

def create_telugu_states_packages():
    """Create sample packages for Telugu states"""
    
    packages_data = [
        {
            'name': 'Tirupati Spiritual Journey',
            'place_name': 'Tirupati Balaji Temple',
            'description': 'Complete spiritual experience including darshan, accommodation, and local sightseeing.',
            'base_price': 2500,
            'duration_days': 2,
            'max_capacity': 20,
            'is_featured': True,
        },
        {
            'name': 'Araku Valley Adventure',
            'place_name': 'Araku Valley',
            'description': 'Explore the beautiful hill station with coffee plantations, tribal culture, and adventure activities.',
            'base_price': 3500,
            'duration_days': 3,
            'max_capacity': 15,
            'is_featured': True,
        },
        {
            'name': 'Hyderabad Heritage Tour',
            'place_name': 'Charminar',
            'description': 'Explore the rich heritage of Hyderabad including Charminar, Golconda Fort, and local cuisine.',
            'base_price': 4000,
            'duration_days': 3,
            'max_capacity': 12,
            'is_featured': True,
        },
        {
            'name': 'Warangal Historical Expedition',
            'place_name': 'Warangal Fort',
            'description': 'Discover the ancient Kakatiya dynasty heritage with guided tours and cultural experiences.',
            'base_price': 2800,
            'duration_days': 2,
            'max_capacity': 18,
            'is_featured': False,
        },
        {
            'name': 'Bhadrachalam Temple Visit',
            'place_name': 'Bhadrachalam Temple',
            'description': 'Spiritual journey to the sacred temple with accommodation and local exploration.',
            'base_price': 2200,
            'duration_days': 2,
            'max_capacity': 25,
            'is_featured': True,
        },
        {
            'name': 'Cave Exploration Package',
            'place_name': 'Borra Caves',
            'description': 'Adventure package exploring the magnificent cave systems with expert guides.',
            'base_price': 1800,
            'duration_days': 1,
            'max_capacity': 30,
            'is_featured': False,
        },
        {
            'name': 'Wildlife Safari Package',
            'place_name': 'Kawal Wildlife Sanctuary',
            'description': 'Wildlife safari with accommodation, meals, and expert naturalist guides.',
            'base_price': 4500,
            'duration_days': 2,
            'max_capacity': 10,
            'is_featured': False,
        },
        {
            'name': 'Yadagirigutta Healing Retreat',
            'place_name': 'Yadagirigutta Temple',
            'description': 'Spiritual healing retreat with meditation sessions and temple rituals.',
            'base_price': 3200,
            'duration_days': 2,
            'max_capacity': 20,
            'is_featured': True,
        },
    ]
    
    created_packages = []
    
    for package_data in packages_data:
        try:
            place = Place.objects.get(name=package_data['place_name'])
            package, created = Package.objects.get_or_create(
                name=package_data['name'],
                defaults={
                    'place': place,
                    'description': package_data['description'],
                    'base_price': package_data['base_price'],
                    'duration_days': package_data['duration_days'],
                    'max_capacity': package_data['max_capacity'],
                    'is_featured': package_data['is_featured'],
                }
            )
            if created:
                print(f"✅ Created package: {package.name}")
            else:
                print(f"⏭️  Package already exists: {package.name}")
            created_packages.append(package)
        except Place.DoesNotExist:
            print(f"❌ Place not found: {package_data['place_name']}")
    
    return created_packages

def main():
    """Main function to create Telugu states data"""
    print("🌍 Creating Telugu States Tourism Data...")
    print("=" * 50)
    
    # Create places
    print("\n📍 Creating Places...")
    places = create_telugu_states_places()
    print(f"✅ Created {len(places)} places")
    
    # Create packages
    print("\n📦 Creating Packages...")
    packages = create_telugu_states_packages()
    print(f"✅ Created {len(packages)} packages")
    
    print("\n🎉 Telugu States Tourism Data Created Successfully!")
    print(f"📍 Total Places: {Place.objects.count()}")
    print(f"📦 Total Packages: {Package.objects.count()}")
    
    # Print summary by state
    ap_places = Place.objects.filter(state='ap').count()
    ts_places = Place.objects.filter(state='telangana').count()
    
    print(f"\n📊 Summary:")
    print(f"   Andhra Pradesh: {ap_places} places")
    print(f"   Telangana: {ts_places} places")

if __name__ == "__main__":
    main()
