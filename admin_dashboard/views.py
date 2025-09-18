from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Avg, Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime, timedelta
import json

from accounts.models import User
from places.models import Place
from packages.models import Package
from bookings.models import Booking, BookingMember
from feedback.models import Feedback
from payments.models import Payment
from itinerary.models import Itinerary, TravelRecommendation

def admin_required(view_func):
    """Decorator to check if user is admin"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            messages.error(request, 'Access denied. Admin privileges required.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper

@admin_required
def dashboard(request):
    """Main admin dashboard with analytics"""
    
    # Date range for analytics
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    
    # User statistics
    total_users = User.objects.count()
    new_users_this_month = User.objects.filter(date_joined__gte=start_date).count()
    active_users = User.objects.filter(last_login__gte=start_date).count()
    
    # Booking statistics
    total_bookings = Booking.objects.count()
    bookings_this_month = Booking.objects.filter(created_at__gte=start_date).count()
    total_revenue = Booking.objects.filter(status='confirmed').aggregate(total=Sum('total_price'))['total'] or 0
    monthly_revenue = Booking.objects.filter(
        status='confirmed',
        created_at__gte=start_date
    ).aggregate(total=Sum('total_price'))['total'] or 0
    
    # Package statistics
    total_packages = Package.objects.count()
    active_packages = Package.objects.filter(is_active=True).count()
    avg_package_price = Package.objects.aggregate(avg=Avg('base_price'))['avg'] or 0
    
    # Place statistics
    total_places = Place.objects.count()
    featured_places = Place.objects.filter(is_featured=True).count()
    avg_place_rating = Place.objects.aggregate(avg=Avg('rating'))['avg'] or 0
    
    # Feedback statistics
    total_feedback = Feedback.objects.count()
    pending_feedback = Feedback.objects.filter(is_approved=False).count()
    avg_rating = Feedback.objects.aggregate(avg=Avg('rating'))['avg'] or 0
    
    # Payment statistics
    total_payments = Payment.objects.count()
    successful_payments = Payment.objects.filter(payment_status='completed').count()
    total_payment_amount = Payment.objects.filter(payment_status='completed').aggregate(total=Sum('amount'))['total'] or 0
    
    # Recent activities
    recent_bookings = Booking.objects.select_related('user', 'package').order_by('-created_at')[:5]
    recent_feedback = Feedback.objects.select_related('user', 'place').order_by('-created_at')[:5]
    recent_payments = Payment.objects.select_related('user', 'booking').order_by('-created_at')[:5]
    
    # Chart data
    chart_data = get_chart_data(start_date, end_date)
    
    context = {
        # Statistics
        'total_users': total_users,
        'new_users_this_month': new_users_this_month,
        'active_users': active_users,
        'total_bookings': total_bookings,
        'bookings_this_month': bookings_this_month,
        'total_revenue': total_revenue,
        'monthly_revenue': monthly_revenue,
        'total_packages': total_packages,
        'active_packages': active_packages,
        'avg_package_price': avg_package_price,
        'total_places': total_places,
        'featured_places': featured_places,
        'avg_place_rating': avg_place_rating,
        'total_feedback': total_feedback,
        'pending_feedback': pending_feedback,
        'avg_rating': avg_rating,
        'total_payments': total_payments,
        'successful_payments': successful_payments,
        'total_payment_amount': total_payment_amount,
        
        # Recent activities
        'recent_bookings': recent_bookings,
        'recent_feedback': recent_feedback,
        'recent_payments': recent_payments,
        
        # Chart data
        'chart_data': json.dumps(chart_data),
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)

def get_chart_data(start_date, end_date):
    """Generate chart data for analytics"""
    
    # Daily bookings for the last 30 days
    daily_bookings = []
    daily_revenue = []
    dates = []
    
    current_date = start_date.date()
    while current_date <= end_date.date():
        date_str = current_date.strftime('%Y-%m-%d')
        dates.append(date_str)
        
        # Bookings count
        bookings_count = Booking.objects.filter(
            created_at__date=current_date
        ).count()
        daily_bookings.append(bookings_count)
        
        # Revenue
        revenue = Booking.objects.filter(
            created_at__date=current_date,
            status='confirmed'
        ).aggregate(total=Sum('total_price'))['total'] or 0
        daily_revenue.append(float(revenue))
        
        current_date += timedelta(days=1)
    
    # Top packages by bookings
    top_packages = Package.objects.annotate(
        booking_count=Count('bookings')
    ).order_by('-booking_count')[:5]
    
    package_data = {
        'labels': [pkg.name for pkg in top_packages],
        'data': [pkg.booking_count for pkg in top_packages]
    }
    
    # Top places by rating
    top_places = Place.objects.filter(rating__gt=0).order_by('-rating')[:5]
    
    place_data = {
        'labels': [place.name for place in top_places],
        'data': [float(place.rating) for place in top_places]
    }
    
    # User registration trend
    user_registrations = []
    current_date = start_date.date()
    while current_date <= end_date.date():
        users_count = User.objects.filter(
            date_joined__date=current_date
        ).count()
        user_registrations.append(users_count)
        current_date += timedelta(days=1)
    
    return {
        'daily_bookings': {
            'labels': dates,
            'data': daily_bookings
        },
        'daily_revenue': {
            'labels': dates,
            'data': daily_revenue
        },
        'top_packages': package_data,
        'top_places': place_data,
        'user_registrations': {
            'labels': dates,
            'data': user_registrations
        }
    }

@admin_required
def user_management(request):
    """User management page"""
    users = User.objects.all()
    
    # Search and filtering
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    # Filter by role
    role_filter = request.GET.get('role', '')
    if role_filter == 'admin':
        users = users.filter(is_admin=True)
    elif role_filter == 'user':
        users = users.filter(is_admin=False)
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter == 'active':
        users = users.filter(is_active=True)
    elif status_filter == 'inactive':
        users = users.filter(is_active=False)
    
    # Pagination
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'users': page_obj,
        'search_query': search_query,
        'role_filter': role_filter,
        'status_filter': status_filter,
        'total_users': users.count(),
    }
    
    return render(request, 'admin_dashboard/user_management.html', context)

@admin_required
def place_management(request):
    """Place management page"""
    places = Place.objects.all()
    
    # Search and filtering
    search_query = request.GET.get('search', '')
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        places = places.filter(category=category_filter)
    
    # Filter by state
    state_filter = request.GET.get('state', '')
    if state_filter:
        places = places.filter(state=state_filter)
    
    # Filter by featured status
    featured_filter = request.GET.get('featured', '')
    if featured_filter == 'yes':
        places = places.filter(is_featured=True)
    elif featured_filter == 'no':
        places = places.filter(is_featured=False)
    
    # Sort options
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'rating':
        places = places.order_by('-rating')
    elif sort_by == 'reviews':
        places = places.order_by('-total_reviews')
    elif sort_by == 'created':
        places = places.order_by('-created_at')
    else:
        places = places.order_by('name')
    
    # Pagination
    paginator = Paginator(places, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'places': page_obj,
        'search_query': search_query,
        'category_filter': category_filter,
        'state_filter': state_filter,
        'featured_filter': featured_filter,
        'sort_by': sort_by,
        'categories': Place.CATEGORY_CHOICES,
        'states': Place.STATE_CHOICES,
        'total_places': places.count(),
    }
    
    return render(request, 'admin_dashboard/place_management.html', context)

@admin_required
def package_management(request):
    """Package management page"""
    packages = Package.objects.select_related('place').all()
    
    # Search and filtering
    search_query = request.GET.get('search', '')
    if search_query:
        packages = packages.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(place__name__icontains=search_query)
        )
    
    # Filter by place
    place_filter = request.GET.get('place', '')
    if place_filter:
        packages = packages.filter(place_id=place_filter)
    
    # Filter by featured status
    featured_filter = request.GET.get('featured', '')
    if featured_filter == 'yes':
        packages = packages.filter(is_featured=True)
    elif featured_filter == 'no':
        packages = packages.filter(is_featured=False)
    
    # Sort options
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_low':
        packages = packages.order_by('base_price')
    elif sort_by == 'price_high':
        packages = packages.order_by('-base_price')
    elif sort_by == 'duration':
        packages = packages.order_by('duration_days')
    elif sort_by == 'created':
        packages = packages.order_by('-created_at')
    else:
        packages = packages.order_by('name')
    
    # Pagination
    paginator = Paginator(packages, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'packages': page_obj,
        'search_query': search_query,
        'place_filter': place_filter,
        'featured_filter': featured_filter,
        'sort_by': sort_by,
        'places': Place.objects.all(),
        'total_packages': packages.count(),
    }
    
    return render(request, 'admin_dashboard/package_management.html', context)

@admin_required
def booking_management(request):
    """Booking management page"""
    bookings = Booking.objects.select_related('user', 'package').all()
    
    # Search and filtering
    search_query = request.GET.get('search', '')
    if search_query:
        bookings = bookings.filter(
            Q(user__username__icontains=search_query) |
            Q(package__name__icontains=search_query) |
            Q(booking_reference__icontains=search_query)
        )
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        bookings = bookings.filter(status=status_filter)
    
    # Filter by date range
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    
    if date_from:
        bookings = bookings.filter(booking_date__gte=date_from)
    if date_to:
        bookings = bookings.filter(booking_date__lte=date_to)
    
    # Sort options
    sort_by = request.GET.get('sort', 'created_at')
    if sort_by == 'booking_date':
        bookings = bookings.order_by('booking_date')
    elif sort_by == 'total_price':
        bookings = bookings.order_by('-total_price')
    elif sort_by == 'status':
        bookings = bookings.order_by('status')
    else:
        bookings = bookings.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(bookings, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Statistics
    total_bookings = Booking.objects.count()
    pending_count = Booking.objects.filter(status='pending').count()
    confirmed_count = Booking.objects.filter(status='confirmed').count()
    total_revenue = Booking.objects.filter(status='confirmed').aggregate(total=Sum('total_price'))['total'] or 0
    
    context = {
        'bookings': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'date_from': date_from,
        'date_to': date_to,
        'sort_by': sort_by,
        'status_choices': Booking.STATUS_CHOICES,
        'total_bookings': total_bookings,
        'pending_count': pending_count,
        'confirmed_count': confirmed_count,
        'total_revenue': total_revenue,
        'packages': Package.objects.all(),
    }
    
    return render(request, 'admin_dashboard/booking_management.html', context)

@admin_required
def feedback_management(request):
    """Feedback management page"""
    feedbacks = Feedback.objects.select_related('user', 'place').all()
    
    # Search and filtering
    search_query = request.GET.get('search', '')
    if search_query:
        feedbacks = feedbacks.filter(
            Q(user__username__icontains=search_query) |
            Q(place__name__icontains=search_query) |
            Q(comment__icontains=search_query)
        )
    
    # Filter by approval status
    approval_filter = request.GET.get('approval', '')
    if approval_filter == 'approved':
        feedbacks = feedbacks.filter(is_approved=True)
    elif approval_filter == 'pending':
        feedbacks = feedbacks.filter(is_approved=False)
    
    # Filter by rating
    rating_filter = request.GET.get('rating', '')
    if rating_filter:
        feedbacks = feedbacks.filter(rating=int(rating_filter))
    
    # Sort options
    sort_by = request.GET.get('sort', 'created_at')
    if sort_by == 'rating':
        feedbacks = feedbacks.order_by('-rating')
    elif sort_by == 'date':
        feedbacks = feedbacks.order_by('-created_at')
    elif sort_by == 'approval':
        feedbacks = feedbacks.order_by('is_approved')
    else:
        feedbacks = feedbacks.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(feedbacks, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'feedbacks': page_obj,
        'search_query': search_query,
        'approval_filter': approval_filter,
        'rating_filter': rating_filter,
        'sort_by': sort_by,
        'total_feedbacks': feedbacks.count(),
        'pending_feedbacks': Feedback.objects.filter(is_approved=False).count(),
    }
    
    return render(request, 'admin_dashboard/feedback_management.html', context)

@admin_required
def analytics(request):
    """Detailed analytics page"""
    
    # Date range
    period = request.GET.get('period', '30')
    end_date = timezone.now()
    start_date = end_date - timedelta(days=int(period))
    
    # Revenue analytics
    revenue_data = get_revenue_analytics(start_date, end_date)
    
    # Booking analytics
    booking_data = get_booking_analytics(start_date, end_date)
    
    # User analytics
    user_data = get_user_analytics(start_date, end_date)
    
    # Popular destinations
    popular_destinations = Place.objects.annotate(
        booking_count=Count('packages__bookings')
    ).order_by('-booking_count')[:10]
    
    # Top packages
    top_packages = Package.objects.annotate(
        booking_count=Count('bookings')
    ).order_by('-booking_count')[:10]
    
    context = {
        'period': period,
        'revenue_data': json.dumps(revenue_data),
        'booking_data': json.dumps(booking_data),
        'user_data': json.dumps(user_data),
        'popular_destinations': popular_destinations,
        'top_packages': top_packages,
    }
    
    return render(request, 'admin_dashboard/analytics.html', context)

def get_revenue_analytics(start_date, end_date):
    """Generate revenue analytics data"""
    daily_revenue = []
    dates = []
    
    current_date = start_date.date()
    while current_date <= end_date.date():
        revenue = Booking.objects.filter(
            created_at__date=current_date,
            status='confirmed'
        ).aggregate(total=Sum('total_price'))['total'] or 0
        
        daily_revenue.append(float(revenue))
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    
    return {
        'labels': dates,
        'data': daily_revenue
    }

def get_booking_analytics(start_date, end_date):
    """Generate booking analytics data"""
    daily_bookings = []
    dates = []
    
    current_date = start_date.date()
    while current_date <= end_date.date():
        bookings_count = Booking.objects.filter(
            created_at__date=current_date
        ).count()
        
        daily_bookings.append(bookings_count)
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    
    return {
        'labels': dates,
        'data': daily_bookings
    }

def get_user_analytics(start_date, end_date):
    """Generate user analytics data"""
    daily_users = []
    dates = []
    
    current_date = start_date.date()
    while current_date <= end_date.date():
        users_count = User.objects.filter(
            date_joined__date=current_date
        ).count()
        
        daily_users.append(users_count)
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    
    return {
        'labels': dates,
        'data': daily_users
    }

# AJAX endpoints for real-time updates
@admin_required
def get_dashboard_stats(request):
    """Get real-time dashboard statistics"""
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    
    stats = {
        'total_revenue': float(Booking.objects.filter(status='confirmed').aggregate(total=Sum('total_price'))['total'] or 0),
        'monthly_revenue': float(Booking.objects.filter(status='confirmed', created_at__gte=start_date).aggregate(total=Sum('total_price'))['total'] or 0),
        'total_bookings': Booking.objects.count(),
        'pending_bookings': Booking.objects.filter(status='pending').count(),
        'total_users': User.objects.count(),
        'new_users': User.objects.filter(date_joined__gte=start_date).count(),
    }
    
    return JsonResponse(stats)
