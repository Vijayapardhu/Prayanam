from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Place
from utils.weather_api import weather_api

def places_list(request):
    """Display all places with advanced search and filtering"""
    places = Place.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(district__icontains=search_query)
        )
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        places = places.filter(category=category_filter)
    
    # Filter by state
    state_filter = request.GET.get('state', '')
    if state_filter:
        places = places.filter(state=state_filter)
    
    # Filter by district
    district_filter = request.GET.get('district', '')
    if district_filter:
        places = places.filter(district__icontains=district_filter)
    
    # Filter by season
    season_filter = request.GET.get('season', '')
    if season_filter:
        places = places.filter(season=season_filter)
    
    # Filter by rating
    min_rating = request.GET.get('min_rating', '')
    if min_rating:
        places = places.filter(rating__gte=float(min_rating))
    
    # Filter by entry fee
    max_fee = request.GET.get('max_fee', '')
    if max_fee:
        places = places.filter(entry_fee__lte=float(max_fee))
    
    # Sort options
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'rating':
        places = places.order_by('-rating')
    elif sort_by == 'price_low':
        places = places.order_by('entry_fee')
    elif sort_by == 'price_high':
        places = places.order_by('-entry_fee')
    elif sort_by == 'popular':
        places = places.order_by('-total_reviews')
    else:
        places = places.order_by('name')
    
    # Pagination
    paginator = Paginator(places, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique values for filters
    categories = Place.objects.values_list('category', flat=True).distinct()
    states = Place.objects.values_list('state', flat=True).distinct()
    districts = Place.objects.values_list('district', flat=True).distinct()
    seasons = Place.SEASON_CHOICES
    
    context = {
        'places': page_obj,
        'search_query': search_query,
        'category_filter': category_filter,
        'state_filter': state_filter,
        'district_filter': district_filter,
        'season_filter': season_filter,
        'min_rating': min_rating,
        'max_fee': max_fee,
        'sort_by': sort_by,
        'categories': categories,
        'states': states,
        'districts': districts,
        'seasons': seasons,
        'total_places': places.count(),
    }
    
    return render(request, 'places/places_list.html', context)

def place_detail(request, place_id):
    """Display detailed information about a specific place"""
    place = get_object_or_404(Place, id=place_id)
    
    # Get weather data if coordinates are available
    weather_data = None
    forecast_data = None
    recommendations = []
    
    if place.coordinates:
        try:
            lat, lon = place.coordinates
            weather_data = weather_api.get_current_weather(lat, lon)
            forecast_data = weather_api.get_forecast(lat, lon)
            recommendations = weather_api.get_seasonal_recommendations(lat, lon)
        except (ValueError, TypeError) as e:
            print(f"Error unpacking coordinates for place {place.id}: {e}")
            weather_data = None
            forecast_data = None
            recommendations = []
    
    # Get related places
    related_places = Place.objects.filter(
        Q(category=place.category) | Q(state=place.state)
    ).exclude(id=place.id)[:6]
    
    context = {
        'place': place,
        'weather_data': weather_data,
        'forecast_data': forecast_data,
        'recommendations': recommendations,
        'related_places': related_places,
    }
    
    return render(request, 'places/place_detail.html', context)

def search_places(request):
    """AJAX endpoint for real-time search"""
    if request.method == 'GET':
        query = request.GET.get('q', '')
        category = request.GET.get('category', '')
        state = request.GET.get('state', '')
        
        places = Place.objects.all()
        
        if query:
            places = places.filter(
                Q(name__icontains=query) |
                Q(location__icontains=query) |
                Q(description__icontains=query)
            )
        
        if category:
            places = places.filter(category=category)
        
        if state:
            places = places.filter(state=state)
        
        places = places[:10]  # Limit results
        
        results = []
        for place in places:
            results.append({
                'id': place.id,
                'name': place.name,
                'location': place.location,
                'category': place.get_category_display(),
                'rating': float(place.rating),
                'image_url': place.image.url if place.image else None,
                'url': f'/places/{place.id}/'
            })
        
        return JsonResponse({'results': results})
    
    return JsonResponse({'error': 'Invalid request method'})

def get_weather_data(request, place_id):
    """AJAX endpoint for weather data"""
    place = get_object_or_404(Place, id=place_id)
    
    if not place.coordinates:
        return JsonResponse({'error': 'No coordinates available'})
    
    try:
        lat, lon = place.coordinates
    except (ValueError, TypeError) as e:
        return JsonResponse({'error': f'Invalid coordinates: {e}'})
    weather_data = weather_api.get_current_weather(lat, lon)
    forecast_data = weather_api.get_forecast(lat, lon)
    recommendations = weather_api.get_seasonal_recommendations(lat, lon)
    
    return JsonResponse({
        'weather': weather_data,
        'forecast': forecast_data,
        'recommendations': recommendations
    })

def popular_places(request):
    """Display popular places based on ratings and reviews"""
    places = Place.objects.filter(rating__gte=4.0).order_by('-rating', '-total_reviews')[:12]
    
    context = {
        'places': places,
        'title': 'Popular Places',
        'subtitle': 'Top-rated destinations based on traveler reviews'
    }
    
    return render(request, 'places/places_list.html', context)

def featured_places(request):
    """Display featured places"""
    places = Place.objects.filter(is_featured=True).order_by('name')
    
    context = {
        'places': places,
        'title': 'Featured Places',
        'subtitle': 'Handpicked destinations for your next adventure'
    }
    
    return render(request, 'places/places_list.html', context)

def places_by_category(request, category):
    """Display places filtered by category"""
    places = Place.objects.filter(category=category).order_by('name')
    
    category_name = dict(Place.CATEGORY_CHOICES).get(category, category.title())
    
    context = {
        'places': places,
        'title': f'{category_name} Places',
        'subtitle': f'Explore amazing {category_name.lower()} destinations',
        'category_filter': category
    }
    
    return render(request, 'places/places_list.html', context)

def places_by_state(request, state):
    """Display places filtered by state"""
    places = Place.objects.filter(state=state).order_by('name')
    
    state_name = dict(Place.STATE_CHOICES).get(state, state.title())
    
    context = {
        'places': places,
        'title': f'{state_name} Destinations',
        'subtitle': f'Discover the beauty of {state_name}',
        'state_filter': state
    }
    
    return render(request, 'places/places_list.html', context)
