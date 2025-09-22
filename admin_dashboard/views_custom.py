from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, Avg
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
import json

from accounts.models import User
from places.models import Place
from packages.models import Package
from events.models import Event
from bookings.models import Booking
from payments.models import Payment
from feedback.models import Feedback
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

def admin_required(view_func):
    """Decorator to check if user is admin"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            messages.error(request, 'Access denied. Admin privileges required.')
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

@admin_required
def custom_admin_dashboard(request):
    """Custom admin dashboard with comprehensive statistics"""
    
    # Calculate statistics
    stats = {
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
        'new_users_this_month': User.objects.filter(date_joined__gte=timezone.now().replace(day=1)).count(),
        'total_bookings': Booking.objects.count(),
        'pending_bookings': Booking.objects.filter(status='pending').count(),
        'confirmed_bookings': Booking.objects.filter(status='confirmed').count(),
        'total_revenue': Payment.objects.filter(status='completed').aggregate(Sum('amount'))['amount__sum'] or 0,
        'total_places': Place.objects.count(),
        'featured_places': Place.objects.filter(is_featured=True).count(),
        'popular_places': Place.objects.filter(is_popular=True).count(),
        'total_packages': Package.objects.count(),
        'featured_packages': Package.objects.filter(is_featured=True).count(),
        'active_packages': Package.objects.count(),
        'total_events': Event.objects.count(),
        'events_with_images': Event.objects.exclude(image__isnull=True).exclude(image='').count(),
        'upcoming_events': Event.objects.count(),  # All events are upcoming as they're part of packages
        'total_payments': Payment.objects.count(),
        'successful_payments': Payment.objects.filter(status='completed').count(),
        'pending_payments': Payment.objects.filter(status='pending').count(),
        'total_feedback': Feedback.objects.count(),
        'average_rating': Feedback.objects.aggregate(Avg('rating'))['rating__avg'] or 0,
        'recent_feedback': Feedback.objects.filter(created_at__gte=timezone.now() - timedelta(days=7)).count(),
        'database_size': 25.6,  # Mock database size
        'last_backup': timezone.now() - timedelta(days=1),
    }
    
    # Recent activities
    recent_activities = []
    
    # Recent bookings
    recent_bookings = Booking.objects.select_related('user', 'package').order_by('-created_at')[:5]
    for booking in recent_bookings:
        recent_activities.append({
            'icon': 'calendar-check',
            'description': f'New booking by {booking.user.get_full_name()} for {booking.package.name}',
            'timestamp': booking.created_at
        })
    
    # Recent users
    recent_users = User.objects.filter(date_joined__gte=timezone.now() - timedelta(days=7)).order_by('-date_joined')[:3]
    for user in recent_users:
        recent_activities.append({
            'icon': 'user-plus',
            'description': f'New user registered: {user.get_full_name()}',
            'timestamp': user.date_joined
        })
    
    # Recent feedback
    recent_feedback = Feedback.objects.select_related('user', 'place').order_by('-created_at')[:3]
    for feedback in recent_feedback:
        recent_activities.append({
            'icon': 'comment',
            'description': f'New review by {feedback.user.get_full_name()} for {feedback.place.name}',
            'timestamp': feedback.created_at
        })
    
    # Sort activities by timestamp
    recent_activities.sort(key=lambda x: x['timestamp'], reverse=True)
    recent_activities = recent_activities[:10]
    
    context = {
        'stats': stats,
        'recent_activities': recent_activities,
    }
    
    return render(request, 'admin_dashboard/custom_admin_dashboard.html', context)

@admin_required
def booking_management(request):
    """Manage all bookings"""
    
    # Get filter parameters
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    date_from = request.GET.get('date_from', '')
    
    # Build query
    bookings = Booking.objects.select_related('user', 'package', 'package__place').order_by('-created_at')
    
    if search:
        bookings = bookings.filter(
            Q(user__first_name__icontains=search) |
            Q(user__last_name__icontains=search) |
            Q(user__email__icontains=search) |
            Q(package__name__icontains=search) |
            Q(package__place__name__icontains=search)
        )
    
    if status:
        bookings = bookings.filter(status=status)
    
    if date_from:
        bookings = bookings.filter(from_date__gte=date_from)
    
    # Pagination
    paginator = Paginator(bookings, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'bookings': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'admin_dashboard/booking_management.html', context)

@admin_required
def booking_detail(request, booking_id):
    """View booking details"""
    booking = get_object_or_404(Booking, id=booking_id)
    
    context = {
        'booking': booking,
    }
    
    return render(request, 'admin_dashboard/booking_detail.html', context)

@admin_required
def edit_booking(request, booking_id):
    """Edit booking"""
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        # Handle booking update
        booking.status = request.POST.get('status', booking.status)
        booking.from_date = request.POST.get('from_date', booking.from_date)
        booking.to_date = request.POST.get('to_date', booking.to_date)
        booking.members_count = request.POST.get('members_count', booking.members_count)
        booking.total_amount = request.POST.get('total_amount', booking.total_amount)
        booking.save()
        
        messages.success(request, 'Booking updated successfully!')
        return redirect('admin_dashboard:booking_management')
    
    context = {
        'booking': booking,
    }
    
    return render(request, 'admin_dashboard/edit_booking.html', context)

@admin_required
def confirm_booking(request, booking_id):
    """Confirm booking via AJAX"""
    if request.method == 'POST':
        try:
            booking = get_object_or_404(Booking, id=booking_id)
            booking.status = 'confirmed'
            booking.save()
            
            return JsonResponse({'success': True, 'message': 'Booking confirmed successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@admin_required
def cancel_booking(request, booking_id):
    """Cancel booking via AJAX"""
    if request.method == 'POST':
        try:
            booking = get_object_or_404(Booking, id=booking_id)
            booking.status = 'cancelled'
            booking.save()
            
            return JsonResponse({'success': True, 'message': 'Booking cancelled successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@admin_required
def user_management(request):
    """Manage all users"""
    
    # Get filter parameters
    search = request.GET.get('search', '')
    role = request.GET.get('role', '')
    is_active = request.GET.get('is_active', '')
    
    # Build query
    users = User.objects.all().order_by('-date_joined')
    
    if search:
        users = users.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(username__icontains=search) |
            Q(email__icontains=search)
        )
    
    if role:
        users = users.filter(role=role)
    
    if is_active:
        users = users.filter(is_active=is_active == 'true')
    
    # Pagination
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'users': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'admin_dashboard/user_management.html', context)

@admin_required
def user_detail(request, user_id):
    """View user details"""
    user = get_object_or_404(User, id=user_id)
    
    # Get user's bookings
    bookings = Booking.objects.filter(user=user).order_by('-created_at')[:10]
    
    # Get user's feedback
    feedback = Feedback.objects.filter(user=user).order_by('-created_at')[:10]
    
    context = {
        'user': user,
        'bookings': bookings,
        'feedback': feedback,
    }
    
    return render(request, 'admin_dashboard/user_detail.html', context)

@admin_required
def activate_user(request, user_id):
    """Activate user via AJAX"""
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, id=user_id)
            user.is_active = True
            user.save()
            
            return JsonResponse({'success': True, 'message': 'User activated successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@admin_required
def deactivate_user(request, user_id):
    """Deactivate user via AJAX"""
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, id=user_id)
            user.is_active = False
            user.save()
            
            return JsonResponse({'success': True, 'message': 'User deactivated successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@admin_required
def delete_user(request, user_id):
    """Delete user via AJAX"""
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, id=user_id)
            if user.role == 'admin':
                return JsonResponse({'success': False, 'message': 'Cannot delete admin users'})
            
            user.delete()
            
            return JsonResponse({'success': True, 'message': 'User deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@admin_required
def place_management(request):
    """Manage all places"""
    
    # Get filter parameters
    search = request.GET.get('search', '')
    state = request.GET.get('state', '')
    category = request.GET.get('category', '')
    is_featured = request.GET.get('is_featured', '')
    
    # Build query
    places = Place.objects.all().order_by('-created_at')
    
    if search:
        places = places.filter(
            Q(name__icontains=search) |
            Q(location__icontains=search) |
            Q(description__icontains=search)
        )
    
    if state:
        places = places.filter(state=state)
    
    if category:
        places = places.filter(category=category)
    
    if is_featured:
        places = places.filter(is_featured=is_featured == 'true')
    
    # Pagination
    paginator = Paginator(places, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'places': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'admin_dashboard/place_management.html', context)

@admin_required
def place_detail(request, place_id):
    """View place details"""
    place = get_object_or_404(Place, id=place_id)
    
    # Get packages for this place
    packages = Package.objects.filter(place=place).order_by('-created_at')
    
    # Get events for this place's packages
    events = Event.objects.filter(package__place=place).order_by('day_number', 'time_slot')
    
    context = {
        'place': place,
        'packages': packages,
        'events': events,
    }
    
    return render(request, 'admin_dashboard/place_detail.html', context)

@admin_required
def edit_place(request, place_id):
    """Edit place"""
    place = get_object_or_404(Place, id=place_id)
    
    if request.method == 'POST':
        # Handle place update
        place.name = request.POST.get('name', place.name)
        place.location = request.POST.get('location', place.location)
        place.description = request.POST.get('description', place.description)
        place.category = request.POST.get('category', place.category)
        place.state = request.POST.get('state', place.state)
        place.district = request.POST.get('district', place.district)
        place.latitude = request.POST.get('latitude', place.latitude)
        place.longitude = request.POST.get('longitude', place.longitude)
        place.entry_fee = request.POST.get('entry_fee', place.entry_fee)
        place.opening_hours = request.POST.get('opening_hours', place.opening_hours)
        place.rating = request.POST.get('rating', place.rating)
        place.is_featured = request.POST.get('is_featured') == 'on'
        place.is_popular = request.POST.get('is_popular') == 'on'
        place.save()
        
        messages.success(request, 'Place updated successfully!')
        return redirect('admin_dashboard:place_management')
    
    context = {
        'place': place,
    }
    
    return render(request, 'admin_dashboard/edit_place.html', context)

@admin_required
def create_place(request):
    """Create new place"""
    if request.method == 'POST':
        # Handle place creation
        place = Place.objects.create(
            name=request.POST.get('name'),
            location=request.POST.get('location'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            state=request.POST.get('state'),
            district=request.POST.get('district'),
            latitude=request.POST.get('latitude', 0),
            longitude=request.POST.get('longitude', 0),
            entry_fee=request.POST.get('entry_fee', 0),
            opening_hours=request.POST.get('opening_hours'),
            rating=request.POST.get('rating', 0),
            is_featured=request.POST.get('is_featured') == 'on',
            is_popular=request.POST.get('is_popular') == 'on',
        )
        
        messages.success(request, 'Place created successfully!')
        return redirect('admin_dashboard:place_management')
    
    return render(request, 'admin_dashboard/create_place.html')

@admin_required
def toggle_featured_place(request, place_id):
    """Toggle featured status of place via AJAX"""
    if request.method == 'POST':
        try:
            place = get_object_or_404(Place, id=place_id)
            place.is_featured = not place.is_featured
            place.save()
            
            return JsonResponse({'success': True, 'message': f'Place {"featured" if place.is_featured else "unfeatured"} successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@admin_required
def delete_place(request, place_id):
    """Delete place via AJAX"""
    if request.method == 'POST':
        try:
            place = get_object_or_404(Place, id=place_id)
            place.delete()
            
            return JsonResponse({'success': True, 'message': 'Place deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@admin_required
def package_management(request):
    """Manage all packages"""
    
    # Get filter parameters
    search = request.GET.get('search', '')
    place_state = request.GET.get('place_state', '')
    is_featured = request.GET.get('is_featured', '')
    
    # Build query
    packages = Package.objects.select_related('place').all().order_by('-created_at')
    
    if search:
        packages = packages.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(place__name__icontains=search)
        )
    
    if place_state:
        packages = packages.filter(place__state=place_state)
    
    if is_featured:
        packages = packages.filter(is_featured=is_featured == 'true')
    
    # Pagination
    paginator = Paginator(packages, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'packages': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'admin_dashboard/package_management.html', context)

@admin_required
def event_management(request):
    """Manage all events"""
    
    # Get filter parameters
    search = request.GET.get('search', '')
    time_slot = request.GET.get('time_slot', '')
    day_number = request.GET.get('day_number', '')
    
    # Build query
    events = Event.objects.select_related('package', 'package__place').all().order_by('day_number', 'time_slot')
    
    if search:
        events = events.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(location__icontains=search) |
            Q(package__name__icontains=search) |
            Q(package__place__name__icontains=search)
        )
    
    if time_slot:
        events = events.filter(time_slot=time_slot)
    
    if day_number:
        events = events.filter(day_number=day_number)
    
    # Pagination
    paginator = Paginator(events, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'events': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'admin_dashboard/event_management.html', context)

@admin_required
def payment_management(request):
    """Manage all payments"""
    
    # Get filter parameters
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    payment_method = request.GET.get('payment_method', '')
    
    # Build query
    payments = Payment.objects.select_related('booking', 'booking__user').all().order_by('-created_at')
    
    if search:
        payments = payments.filter(
            Q(booking__user__first_name__icontains=search) |
            Q(booking__user__last_name__icontains=search) |
            Q(booking__user__email__icontains=search) |
            Q(transaction_id__icontains=search)
        )
    
    if status:
        payments = payments.filter(status=status)
    
    if payment_method:
        payments = payments.filter(payment_method=payment_method)
    
    # Pagination
    paginator = Paginator(payments, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'payments': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'admin_dashboard/payment_management.html', context)

@admin_required
def feedback_management(request):
    """Manage all feedback"""
    
    # Get filter parameters
    search = request.GET.get('search', '')
    rating = request.GET.get('rating', '')
    place = request.GET.get('place', '')
    
    # Build query
    feedback = Feedback.objects.select_related('user', 'place').all().order_by('-created_at')
    
    if search:
        feedback = feedback.filter(
            Q(user__first_name__icontains=search) |
            Q(user__last_name__icontains=search) |
            Q(user__email__icontains=search) |
            Q(place__name__icontains=search) |
            Q(comment__icontains=search)
        )
    
    if rating:
        feedback = feedback.filter(rating=rating)
    
    if place:
        feedback = feedback.filter(place_id=place)
    
    # Pagination
    paginator = Paginator(feedback, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'feedback': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'admin_dashboard/feedback_management.html', context)

# Thin CRUD wrappers delegating to admin_dashboard.views to keep URL resolution stable
from . import views as core_views

@admin_required
def create_package(request):
    return core_views.create_package(request)

@admin_required
def package_detail(request, package_id):
    return core_views.package_detail(request, package_id)

@admin_required
def edit_package(request, package_id):
    return core_views.edit_package(request, package_id)

@admin_required
def delete_package(request, package_id):
    return core_views.delete_package(request, package_id)

@admin_required
def create_event(request):
    return core_views.create_event(request)

@admin_required
def event_detail(request, event_id):
    return core_views.event_detail(request, event_id)

@admin_required
def edit_event(request, event_id):
    return core_views.edit_event(request, event_id)

@admin_required
def delete_event(request, event_id):
    return core_views.delete_event(request, event_id)

@admin_required
def payment_detail(request, payment_id):
    return core_views.payment_detail(request, payment_id)

@admin_required
def edit_payment(request, payment_id):
    return core_views.edit_payment(request, payment_id)

@admin_required
def delete_payment(request, payment_id):
    return core_views.delete_payment(request, payment_id)

@admin_required
def feedback_detail(request, feedback_id):
    return core_views.feedback_detail(request, feedback_id)

@admin_required
def edit_feedback(request, feedback_id):
    return core_views.edit_feedback(request, feedback_id)

@admin_required
def delete_feedback(request, feedback_id):
    return core_views.delete_feedback(request, feedback_id)
