#!/usr/bin/env python
"""
Script to create events for existing packages
This will add various events to make the packages more detailed and interesting
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

from events.models import Event
from packages.models import Package

def create_events_for_packages():
    """Create events for all existing packages"""
    print("🎉 Creating events for packages...")
    
    packages = Package.objects.all()
    created_events = []
    
    for package in packages:
        print(f"Creating events for: {package.name}")
        
        # Create events based on package duration and place
        place_name = package.place.name.lower()
        
        if package.duration_days == 1:
            # Single day packages
            events = create_single_day_events(package, place_name)
        elif package.duration_days == 2:
            # Two day packages
            events = create_two_day_events(package, place_name)
        else:
            # Three day packages
            events = create_three_day_events(package, place_name)
        
        for event_data in events:
            event = Event.objects.create(
                package=package,
                title=event_data['title'],
                description=event_data['description'],
                time_slot=event_data['time_slot'],
                location=event_data['location'],
                duration_hours=event_data['duration_hours'],
                includes_food=event_data['includes_food'],
                food_description=event_data.get('food_description', ''),
                day_number=event_data['day_number']
            )
            created_events.append(event)
    
    print(f"✅ Created {len(created_events)} events for {len(packages)} packages")
    return created_events

def create_single_day_events(package, place_name):
    """Create events for single day packages"""
    events = []
    
    # Morning events
    if 'temple' in place_name or 'balaji' in place_name or 'srisailam' in place_name or 'bhadrachalam' in place_name or 'yadagirigutta' in place_name:
        events.append({
            'title': 'Temple Darshan & Pooja',
            'description': 'Early morning temple visit with special pooja and darshan. Experience the spiritual atmosphere and receive blessings.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 3.0,
            'includes_food': True,
            'food_description': 'Prasadam (temple food) and traditional breakfast',
            'day_number': 1
        })
    elif 'fort' in place_name or 'golconda' in place_name or 'gandikota' in place_name or 'warangal' in place_name:
        events.append({
            'title': 'Fort Exploration & History Tour',
            'description': 'Guided tour of the historic fort with detailed explanation of its architecture, history, and significance.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 3.0,
            'includes_food': True,
            'food_description': 'Traditional breakfast and refreshments',
            'day_number': 1
        })
    elif 'valley' in place_name or 'araku' in place_name:
        events.append({
            'title': 'Valley Sunrise & Coffee Plantation Tour',
            'description': 'Early morning visit to coffee plantations with sunrise views and coffee tasting session.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 3.0,
            'includes_food': True,
            'food_description': 'Fresh coffee, local breakfast, and plantation snacks',
            'day_number': 1
        })
    elif 'cave' in place_name or 'borra' in place_name or 'belum' in place_name:
        events.append({
            'title': 'Cave Exploration & Geological Tour',
            'description': 'Guided exploration of the caves with detailed explanation of geological formations and natural history.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 3.0,
            'includes_food': True,
            'food_description': 'Light breakfast and refreshments',
            'day_number': 1
        })
    else:
        events.append({
            'title': 'Morning Sightseeing Tour',
            'description': 'Comprehensive morning tour of the destination with local guide and historical insights.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 3.0,
            'includes_food': True,
            'food_description': 'Traditional breakfast and local delicacies',
            'day_number': 1
        })
    
    # Afternoon events
    events.append({
        'title': 'Local Culture & Shopping Experience',
        'description': 'Visit to local markets, handicraft centers, and cultural sites. Learn about local traditions and shop for souvenirs.',
        'time_slot': 'afternoon',
        'location': f'{package.place.name} Market Area',
        'duration_hours': 2.5,
        'includes_food': True,
        'food_description': 'Traditional lunch with local specialties',
        'day_number': 1
    })
    
    # Evening events
    if 'temple' in place_name or 'balaji' in place_name or 'srisailam' in place_name or 'bhadrachalam' in place_name or 'yadagirigutta' in place_name:
        events.append({
            'title': 'Evening Aarti & Spiritual Experience',
            'description': 'Attend the evening aarti ceremony and experience the divine atmosphere with traditional rituals.',
            'time_slot': 'evening',
            'location': package.place.name,
            'duration_hours': 2.0,
            'includes_food': True,
            'food_description': 'Evening prasadam and traditional sweets',
            'day_number': 1
        })
    elif 'fort' in place_name or 'golconda' in place_name or 'gandikota' in place_name or 'warangal' in place_name:
        events.append({
            'title': 'Sunset Photography & Light Show',
            'description': 'Capture beautiful sunset views from the fort and enjoy the evening light and sound show.',
            'time_slot': 'evening',
            'location': package.place.name,
            'duration_hours': 2.5,
            'includes_food': True,
            'food_description': 'Evening snacks and refreshments',
            'day_number': 1
        })
    else:
        events.append({
            'title': 'Sunset View & Cultural Performance',
            'description': 'Enjoy beautiful sunset views and traditional cultural performances showcasing local art and music.',
            'time_slot': 'evening',
            'location': package.place.name,
            'duration_hours': 2.0,
            'includes_food': True,
            'food_description': 'Evening snacks and traditional refreshments',
            'day_number': 1
        })
    
    return events

def create_two_day_events(package, place_name):
    """Create events for two day packages"""
    events = []
    
    # Day 1 - Morning
    if 'temple' in place_name or 'balaji' in place_name or 'srisailam' in place_name or 'bhadrachalam' in place_name or 'yadagirigutta' in place_name:
        events.append({
            'title': 'Temple Darshan & Spiritual Tour',
            'description': 'Early morning temple visit with detailed explanation of temple history, architecture, and spiritual significance.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 4.0,
            'includes_food': True,
            'food_description': 'Prasadam and traditional breakfast',
            'day_number': 1
        })
    elif 'valley' in place_name or 'araku' in place_name:
        events.append({
            'title': 'Valley Exploration & Nature Walk',
            'description': 'Morning nature walk through the valley with coffee plantation tour and scenic viewpoints.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 4.0,
            'includes_food': True,
            'food_description': 'Fresh coffee and plantation breakfast',
            'day_number': 1
        })
    else:
        events.append({
            'title': 'Comprehensive Morning Tour',
            'description': 'Detailed morning exploration of the destination with local guide and historical insights.',
            'time_slot': 'morning',
            'location': package.place.name,
            'duration_hours': 4.0,
            'includes_food': True,
            'food_description': 'Traditional breakfast and local delicacies',
            'day_number': 1
        })
    
    # Day 1 - Afternoon
    events.append({
        'title': 'Local Culture & Heritage Sites',
        'description': 'Visit to heritage sites, museums, and cultural centers. Learn about local history and traditions.',
        'time_slot': 'afternoon',
        'location': f'{package.place.name} Heritage Sites',
        'duration_hours': 3.0,
        'includes_food': True,
        'food_description': 'Traditional lunch with local specialties',
        'day_number': 1
    })
    
    # Day 1 - Evening
    events.append({
        'title': 'Evening Cultural Experience',
        'description': 'Evening cultural program with traditional music, dance, and local entertainment.',
        'time_slot': 'evening',
        'location': f'{package.place.name} Cultural Center',
        'duration_hours': 2.0,
        'includes_food': True,
        'food_description': 'Evening snacks and traditional refreshments',
        'day_number': 1
    })
    
    # Day 2 - Morning
    events.append({
        'title': 'Adventure & Outdoor Activities',
        'description': 'Morning adventure activities like trekking, boating, or other outdoor experiences based on the destination.',
        'time_slot': 'morning',
        'location': f'{package.place.name} Adventure Zone',
        'duration_hours': 3.0,
        'includes_food': True,
        'food_description': 'Adventure breakfast and energy snacks',
        'day_number': 2
    })
    
    # Day 2 - Afternoon
    events.append({
        'title': 'Shopping & Local Market Tour',
        'description': 'Visit to local markets, handicraft centers, and souvenir shops. Learn about local crafts and traditions.',
        'time_slot': 'afternoon',
        'location': f'{package.place.name} Market Area',
        'duration_hours': 2.5,
        'includes_food': True,
        'food_description': 'Traditional lunch and local delicacies',
        'day_number': 2
    })
    
    # Day 2 - Evening
    events.append({
        'title': 'Farewell Dinner & Cultural Show',
        'description': 'Special farewell dinner with cultural performances and traditional entertainment.',
        'time_slot': 'evening',
        'location': f'{package.place.name} Restaurant',
        'duration_hours': 2.5,
        'includes_food': True,
        'food_description': 'Traditional dinner with local specialties and desserts',
        'day_number': 2
    })
    
    return events

def create_three_day_events(package, place_name):
    """Create events for three day packages"""
    events = []
    
    # Day 1 - Morning
    events.append({
        'title': 'Welcome & Orientation Tour',
        'description': 'Welcome session with orientation about the destination, local customs, and itinerary overview.',
        'time_slot': 'morning',
        'location': f'{package.place.name} Welcome Center',
        'duration_hours': 2.0,
        'includes_food': True,
        'food_description': 'Welcome breakfast and refreshments',
        'day_number': 1
    })
    
    # Day 1 - Afternoon
    events.append({
        'title': 'Main Attraction Exploration',
        'description': 'Comprehensive exploration of the main attractions with detailed historical and cultural insights.',
        'time_slot': 'afternoon',
        'location': package.place.name,
        'duration_hours': 4.0,
        'includes_food': True,
        'food_description': 'Traditional lunch with local specialties',
        'day_number': 1
    })
    
    # Day 1 - Evening
    events.append({
        'title': 'Evening Cultural Immersion',
        'description': 'Evening cultural program with traditional performances and local entertainment.',
        'time_slot': 'evening',
        'location': f'{package.place.name} Cultural Center',
        'duration_hours': 2.0,
        'includes_food': True,
        'food_description': 'Evening snacks and traditional refreshments',
        'day_number': 1
    })
    
    # Day 2 - Morning
    events.append({
        'title': 'Adventure & Nature Activities',
        'description': 'Morning adventure activities and nature exploration based on the destination features.',
        'time_slot': 'morning',
        'location': f'{package.place.name} Adventure Zone',
        'duration_hours': 4.0,
        'includes_food': True,
        'food_description': 'Adventure breakfast and energy snacks',
        'day_number': 2
    })
    
    # Day 2 - Afternoon
    events.append({
        'title': 'Heritage & Historical Sites',
        'description': 'Visit to heritage sites, museums, and historical monuments with expert guides.',
        'time_slot': 'afternoon',
        'location': f'{package.place.name} Heritage Sites',
        'duration_hours': 3.0,
        'includes_food': True,
        'food_description': 'Traditional lunch and local delicacies',
        'day_number': 2
    })
    
    # Day 2 - Evening
    events.append({
        'title': 'Local Community Interaction',
        'description': 'Evening interaction with local communities, artisans, and cultural exchange programs.',
        'time_slot': 'evening',
        'location': f'{package.place.name} Local Community',
        'duration_hours': 2.5,
        'includes_food': True,
        'food_description': 'Community dinner with local families',
        'day_number': 2
    })
    
    # Day 3 - Morning
    events.append({
        'title': 'Spiritual & Wellness Experience',
        'description': 'Morning spiritual or wellness activities like meditation, yoga, or temple visits.',
        'time_slot': 'morning',
        'location': f'{package.place.name} Spiritual Center',
        'duration_hours': 3.0,
        'includes_food': True,
        'food_description': 'Healthy breakfast and wellness refreshments',
        'day_number': 3
    })
    
    # Day 3 - Afternoon
    events.append({
        'title': 'Shopping & Local Crafts',
        'description': 'Visit to local markets, handicraft centers, and souvenir shopping with local artisans.',
        'time_slot': 'afternoon',
        'location': f'{package.place.name} Market Area',
        'duration_hours': 2.5,
        'includes_food': True,
        'food_description': 'Traditional lunch and local delicacies',
        'day_number': 3
    })
    
    # Day 3 - Evening
    events.append({
        'title': 'Farewell Celebration',
        'description': 'Special farewell celebration with cultural performances, traditional dinner, and memorable experiences.',
        'time_slot': 'evening',
        'location': f'{package.place.name} Celebration Hall',
        'duration_hours': 3.0,
        'includes_food': True,
        'food_description': 'Grand farewell dinner with traditional specialties and desserts',
        'day_number': 3
    })
    
    return events

def main():
    """Main function to create events for all packages"""
    print("🚀 Starting creation of events for packages...")
    
    try:
        # Clear existing events
        Event.objects.all().delete()
        print("🗑️ Cleared existing events")
        
        # Create events for packages
        events = create_events_for_packages()
        
        print("\n🎉 Events creation completed successfully!")
        print(f"📊 Summary:")
        print(f"   - Events created: {len(events)}")
        print(f"   - Packages with events: {len(set(event.package for event in events))}")
        print(f"   - All packages now have detailed event schedules")
        
    except Exception as e:
        print(f"❌ Error during events creation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
