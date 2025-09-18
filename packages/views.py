from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Package, DynamicPricing
from places.models import Place
from datetime import datetime, timedelta
from decimal import Decimal

def package_list(request):
    """Display all available packages"""
    packages = Package.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        packages = packages.filter(name__icontains=search_query) | packages.filter(description__icontains=search_query)
    
    context = {
        'packages': packages,
        'search_query': search_query,
    }
    return render(request, 'packages/packages_list.html', context)

def package_detail(request, package_id):
    """Display detailed information about a specific package"""
    package = get_object_or_404(Package, id=package_id)
    
    # Get related packages
    related_packages = Package.objects.filter(place=package.place).exclude(id=package.id)[:3]
    
    context = {
        'package': package,
        'related_packages': related_packages,
    }
    return render(request, 'packages/package_detail.html', context)

def trip_details(request, package_id):
    """Display comprehensive trip details with pricing calculator"""
    package = get_object_or_404(Package, id=package_id)
    
    # Get today's date for minimum date validation
    today = datetime.now().date()
    
    context = {
        'package': package,
        'today': today,
    }
    return render(request, 'trip_details.html', context)

def calculate_price(request, package_id):
    """API endpoint for dynamic price calculation"""
    if request.method == 'POST':
        package = get_object_or_404(Package, id=package_id)
        
        # Get parameters from request
        season = request.POST.get('season', 'summer')
        members_count = int(request.POST.get('members_count', 1))
        food_preference = request.POST.get('food_preference', 'mixed')
        start_date = request.POST.get('start_date')
        
        # Calculate base price
        base_price = package.calculate_price(season, members_count)
        
        # Calculate food cost
        food_costs = {
            'veg': 500,
            'non_veg': 800,
            'mixed': 650
        }
        food_cost = food_costs.get(food_preference, 650)
        
        # Calculate seasonal adjustment
        if start_date:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            month = start.month
            
            if month >= 10 or month <= 2:  # Winter
                seasonal_multiplier = 1.2
            elif month >= 3 and month <= 5:  # Summer
                seasonal_multiplier = 0.8
            else:  # Monsoon
                seasonal_multiplier = 0.9
                
            seasonal_adjustment = base_price * (seasonal_multiplier - 1)
        else:
            seasonal_adjustment = 0
        
        # Calculate group discount
        if members_count >= 4:
            group_discount = 0.1
        elif members_count >= 2:
            group_discount = 0.05
        else:
            group_discount = 0
            
        group_discount_amount = base_price * group_discount
        
        # Calculate totals
        total_per_person = base_price + seasonal_adjustment - group_discount_amount + food_cost
        total_group = total_per_person * members_count
        
        return JsonResponse({
            'base_price': float(base_price),
            'seasonal_adjustment': float(seasonal_adjustment),
            'group_discount': float(group_discount_amount),
            'food_cost': food_cost,
            'total_per_person': float(total_per_person),
            'total_group': float(total_group),
            'seasonal_multiplier': seasonal_multiplier if start_date else 1.0,
            'group_discount_rate': group_discount
        })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
