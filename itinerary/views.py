from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Itinerary, ItineraryItem, ItineraryTemplate, TravelRecommendation, TravelPreference
from places.models import Place
from packages.models import Package
from datetime import datetime, timedelta
import json

@login_required
def itinerary_list(request):
    """Display user's itineraries"""
    itineraries = Itinerary.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'itineraries': itineraries,
    }
    return render(request, 'itinerary/itinerary_list.html', context)

@login_required
def itinerary_detail(request, itinerary_id):
    """Display detailed itinerary"""
    itinerary = get_object_or_404(Itinerary, id=itinerary_id, user=request.user)
    
    context = {
        'itinerary': itinerary,
    }
    return render(request, 'itinerary/itinerary_detail.html', context)

@login_required
def create_itinerary(request):
    """Create a new itinerary"""
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        description = data.get('description', '')
        
        if name and start_date and end_date:
            itinerary = Itinerary.objects.create(
                user=request.user,
                name=name,
                start_date=start_date,
                end_date=end_date,
                description=description
            )
            return JsonResponse({'success': True, 'itinerary_id': itinerary.id})
        else:
            return JsonResponse({'success': False, 'error': 'Missing required fields'})
    
    return render(request, 'itinerary/create_itinerary.html')

@login_required
def edit_itinerary(request, itinerary_id):
    """Edit an existing itinerary"""
    itinerary = get_object_or_404(Itinerary, id=itinerary_id, user=request.user)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        itinerary.name = data.get('name', itinerary.name)
        itinerary.start_date = data.get('start_date', itinerary.start_date)
        itinerary.end_date = data.get('end_date', itinerary.end_date)
        itinerary.description = data.get('description', itinerary.description)
        itinerary.save()
        return JsonResponse({'success': True})
    
    context = {
        'itinerary': itinerary,
    }
    return render(request, 'itinerary/edit_itinerary.html', context)

@login_required
def delete_itinerary(request, itinerary_id):
    """Delete an itinerary"""
    itinerary = get_object_or_404(Itinerary, id=itinerary_id, user=request.user)
    
    if request.method == 'POST':
        itinerary.delete()
        messages.success(request, 'Itinerary deleted successfully.')
        return redirect('itinerary_list')
    
    context = {
        'itinerary': itinerary,
    }
    return render(request, 'itinerary/delete_itinerary.html', context)

@login_required
def add_item(request, itinerary_id):
    """Add an item to itinerary"""
    itinerary = get_object_or_404(Itinerary, id=itinerary_id, user=request.user)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        day_number = data.get('day_number')
        place_id = data.get('place_id')
        package_id = data.get('package_id')
        activity_type = data.get('activity_type')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        notes = data.get('notes', '')
        
        if day_number and (place_id or package_id):
            item = ItineraryItem.objects.create(
                itinerary=itinerary,
                day_number=day_number,
                place_id=place_id,
                package_id=package_id,
                activity_type=activity_type,
                start_time=start_time,
                end_time=end_time,
                notes=notes
            )
            return JsonResponse({'success': True, 'item_id': item.id})
        else:
            return JsonResponse({'success': False, 'error': 'Missing required fields'})
    
    places = Place.objects.all()
    packages = Package.objects.all()
    
    context = {
        'itinerary': itinerary,
        'places': places,
        'packages': packages,
    }
    return render(request, 'itinerary/add_item.html', context)

@login_required
def remove_item(request, itinerary_id, item_id):
    """Remove an item from itinerary"""
    itinerary = get_object_or_404(Itinerary, id=itinerary_id, user=request.user)
    item = get_object_or_404(ItineraryItem, id=item_id, itinerary=itinerary)
    
    if request.method == 'POST':
        item.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def template_list(request):
    """Display available itinerary templates"""
    templates = ItineraryTemplate.objects.all()
    
    context = {
        'templates': templates,
    }
    return render(request, 'itinerary/template_list.html', context)

@login_required
def use_template(request, template_id):
    """Use a template to create an itinerary"""
    template = get_object_or_404(ItineraryTemplate, id=template_id)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        start_date = data.get('start_date')
        
        if start_date:
            # Create new itinerary from template
            itinerary = Itinerary.objects.create(
                user=request.user,
                name=f"{template.name} - {start_date}",
                start_date=start_date,
                end_date=start_date + timedelta(days=template.duration_days - 1),
                description=template.description
            )
            
            # Copy template items
            for template_item in template.templateitem_set.all():
                ItineraryItem.objects.create(
                    itinerary=itinerary,
                    day_number=template_item.day_number,
                    place=template_item.place,
                    package=template_item.package,
                    activity_type=template_item.activity_type,
                    start_time=template_item.start_time,
                    end_time=template_item.end_time,
                    notes=template_item.notes
                )
            
            return JsonResponse({'success': True, 'itinerary_id': itinerary.id})
        else:
            return JsonResponse({'success': False, 'error': 'Start date is required'})
    
    context = {
        'template': template,
    }
    return render(request, 'itinerary/use_template.html', context)

@login_required
def recommendations(request):
    """Get personalized travel recommendations"""
    try:
        preference = TravelPreference.objects.get(user=request.user)
    except TravelPreference.DoesNotExist:
        preference = None
    
    recommendations = TravelRecommendation.objects.filter(
        Q(user=request.user) | Q(is_general=True)
    ).order_by('-created_at')[:10]
    
    context = {
        'preference': preference,
        'recommendations': recommendations,
    }
    return render(request, 'itinerary/recommendations.html', context)

@login_required
def set_preferences(request):
    """Set user travel preferences"""
    try:
        preference = TravelPreference.objects.get(user=request.user)
    except TravelPreference.DoesNotExist:
        preference = None
    
    if request.method == 'POST':
        data = json.loads(request.body)
        
        if preference:
            preference.budget_range = data.get('budget_range', preference.budget_range)
            preference.preferred_destinations = data.get('preferred_destinations', preference.preferred_destinations)
            preference.travel_style = data.get('travel_style', preference.travel_style)
            preference.group_size = data.get('group_size', preference.group_size)
            preference.duration_preference = data.get('duration_preference', preference.duration_preference)
        else:
            preference = TravelPreference.objects.create(
                user=request.user,
                budget_range=data.get('budget_range'),
                preferred_destinations=data.get('preferred_destinations'),
                travel_style=data.get('travel_style'),
                group_size=data.get('group_size'),
                duration_preference=data.get('duration_preference')
            )
        
        preference.save()
        return JsonResponse({'success': True})
    
    context = {
        'preference': preference,
    }
    return render(request, 'itinerary/set_preferences.html', context)
