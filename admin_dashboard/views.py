from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Avg, Q, F
from django.http import JsonResponse, HttpResponse, Http404
from django.core.paginator import Paginator
from django.utils import timezone
from django.core.files.storage import default_storage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
from datetime import datetime, timedelta
from django.contrib.auth import login as auth_login
import os
import json
import csv
import io
import uuid
from django.db import transaction

from accounts.models import User
from places.models import Place
from packages.models import Package
from bookings.models import Booking, BookingMember
from feedback.models import Feedback
from payments.models import Payment
from events.models import Event
from itinerary.models import Itinerary, TravelRecommendation
from .models import (
    AdminSettings, AdminNotification, AdminAuditLog, AdminRole,
    AdminUserRole, SystemMaintenance, DataExport, BulkAction,
    AdminDashboardWidget, AdminReport
)
from .forms import (
    AdminSettingsForm, AdminNotificationForm, AdminRoleForm,
    SystemMaintenanceForm, DataExportForm, BulkActionForm,
    AdminDashboardWidgetForm, AdminReportForm, UserManagementForm,
    PlaceManagementForm, PackageManagementForm, BookingManagementForm,
    FeedbackManagementForm, PaymentManagementForm, BulkUserActionForm,
    BulkPlaceActionForm, BulkPackageActionForm, BulkBookingActionForm,
    AnalyticsFilterForm, SearchForm
)

def admin_required(view_func):
    """Decorator to check if user is admin"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            messages.error(request, 'Access denied. Admin privileges required.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper

def log_admin_action(admin_user, action, object_type, object_id=None, object_name='', description='', changes=None):
    """Log admin actions for audit trail"""
    try:
        AdminAuditLog.objects.create(
            admin_user=admin_user,
            action=action,
            object_type=object_type,
            object_id=object_id,
            object_name=object_name,
            description=description,
            ip_address=admin_user.last_login_ip if hasattr(admin_user, 'last_login_ip') else '127.0.0.1',
            user_agent=admin_user.user_agent if hasattr(admin_user, 'user_agent') else '',
            changes=changes or {}
        )
    except Exception as e:
        print(f"Failed to log admin action: {e}")

def create_admin_notification(title, message, notification_type, priority='medium', target_admin=None, is_global=False, related_object_id=None, related_object_type=''):
    """Create admin notification"""
    try:
        AdminNotification.objects.create(
            title=title,
            message=message,
            notification_type=notification_type,
            priority=priority,
            target_admin=target_admin,
            is_global=is_global,
            related_object_id=related_object_id,
            related_object_type=related_object_type
        )
    except Exception as e:
        print(f"Failed to create notification: {e}")

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

# ==================== SYSTEM MANAGEMENT VIEWS ====================

@admin_required
def system_settings(request):
    """System settings management"""
    settings_objects = AdminSettings.objects.all()
    
    if request.method == 'POST':
        form = AdminSettingsForm(request.POST)
        if form.is_valid():
            setting = form.save()
            log_admin_action(request.user, 'create', 'AdminSetting', setting.id, setting.key, f'Created setting: {setting.key}')
            messages.success(request, 'Setting created successfully.')
            return redirect('admin_dashboard:system_settings')
    else:
        form = AdminSettingsForm()
    
    context = {
        'settings': settings_objects,
        'form': form,
        'setting_types': AdminSettings.SETTING_TYPES,
    }
    return render(request, 'admin_dashboard/system_settings.html', context)

@admin_required
def edit_setting(request, setting_id):
    """Edit system setting"""
    setting = get_object_or_404(AdminSettings, id=setting_id)
    
    if request.method == 'POST':
        form = AdminSettingsForm(request.POST, instance=setting)
        if form.is_valid():
            old_value = setting.value
            setting = form.save()
            log_admin_action(request.user, 'update', 'AdminSetting', setting.id, setting.key, 
                           f'Updated setting: {setting.key}', {'old_value': old_value, 'new_value': setting.value})
            messages.success(request, 'Setting updated successfully.')
            return redirect('admin_dashboard:system_settings')
    else:
        form = AdminSettingsForm(instance=setting)
    
    context = {
        'setting': setting,
        'form': form,
    }
    return render(request, 'admin_dashboard/edit_setting.html', context)

@admin_required
def notifications(request):
    """Admin notifications management"""
    notifications = AdminNotification.objects.all()
    
    # Mark notifications as read
    if request.method == 'POST' and 'mark_read' in request.POST:
        notification_ids = request.POST.getlist('notification_ids')
        AdminNotification.objects.filter(id__in=notification_ids).update(is_read=True, read_at=timezone.now())
        messages.success(request, f'{len(notification_ids)} notifications marked as read.')
        return redirect('admin_dashboard:notifications')
    
    # Create new notification
    if request.method == 'POST' and 'create_notification' in request.POST:
        form = AdminNotificationForm(request.POST)
        if form.is_valid():
            notification = form.save()
            log_admin_action(request.user, 'create', 'AdminNotification', notification.id, notification.title)
            messages.success(request, 'Notification created successfully.')
            return redirect('admin_dashboard:notifications')
    else:
        form = AdminNotificationForm()
    
    context = {
        'notifications': notifications,
        'form': form,
        'unread_count': notifications.filter(is_read=False).count(),
    }
    return render(request, 'admin_dashboard/notifications.html', context)

@admin_required
def audit_logs(request):
    """Admin audit logs"""
    logs = AdminAuditLog.objects.all()
    
    # Filtering
    action_filter = request.GET.get('action', '')
    object_type_filter = request.GET.get('object_type', '')
    admin_filter = request.GET.get('admin', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    
    if action_filter:
        logs = logs.filter(action=action_filter)
    if object_type_filter:
        logs = logs.filter(object_type=object_type_filter)
    if admin_filter:
        logs = logs.filter(admin_user__username__icontains=admin_filter)
    if date_from:
        logs = logs.filter(created_at__date__gte=date_from)
    if date_to:
        logs = logs.filter(created_at__date__lte=date_to)
    
    # Pagination
    paginator = Paginator(logs, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'logs': page_obj,
        'action_choices': AdminAuditLog.ACTION_TYPES,
        'filters': {
            'action': action_filter,
            'object_type': object_type_filter,
            'admin': admin_filter,
            'date_from': date_from,
            'date_to': date_to,
        }
    }
    return render(request, 'admin_dashboard/audit_logs.html', context)

# ==================== USER MANAGEMENT VIEWS ====================

@admin_required
def user_management(request):
    """Enhanced user management with CRUD operations"""
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
def create_user(request):
    """Create new user"""
    if request.method == 'POST':
        form = UserManagementForm(request.POST)
        if form.is_valid():
            user = form.save()
            log_admin_action(request.user, 'create', 'User', user.id, user.username, f'Created user: {user.username}')
            create_admin_notification(
                f'New User Created: {user.username}',
                f'Admin {request.user.username} created a new user account for {user.username}',
                'user',
                'medium',
                related_object_id=user.id,
                related_object_type='User'
            )
            messages.success(request, 'User created successfully.')
            return redirect('admin_dashboard:user_management')
    else:
        form = UserManagementForm()
    
    context = {'form': form}
    return render(request, 'admin_dashboard/create_user.html', context)

@admin_required
def edit_user(request, user_id):
    """Edit user"""
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserManagementForm(request.POST, instance=user)
        if form.is_valid():
            old_data = {
                'username': user.username,
                'email': user.email,
                'is_active': user.is_active,
                'role': user.role,
            }
            user = form.save()
            new_data = {
                'username': user.username,
                'email': user.email,
                'is_active': user.is_active,
                'role': user.role,
            }
            changes = {k: {'old': old_data[k], 'new': new_data[k]} for k in old_data if old_data[k] != new_data[k]}
            log_admin_action(request.user, 'update', 'User', user.id, user.username, f'Updated user: {user.username}', changes)
            messages.success(request, 'User updated successfully.')
            return redirect('admin_dashboard:user_management')
    else:
        form = UserManagementForm(instance=user)
    
    context = {'user': user, 'form': form}
    return render(request, 'admin_dashboard/edit_user.html', context)

@admin_required
def delete_user(request, user_id):
    """Delete user"""
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        log_admin_action(request.user, 'delete', 'User', user_id, username, f'Deleted user: {username}')
        messages.success(request, 'User deleted successfully.')
        return redirect('admin_dashboard:user_management')
    
    context = {'user': user}
    return render(request, 'admin_dashboard/delete_user.html', context)

# ==================== BULK OPERATIONS ====================

@admin_required
def bulk_operations(request):
    """Bulk operations management"""
    if request.method == 'POST':
        action_type = request.POST.get('action_type')
        
        if action_type == 'users':
            form = BulkUserActionForm(request.POST)
            if form.is_valid():
                user_ids = form.cleaned_data['user_ids']
                action = form.cleaned_data['action']
                
                # Create bulk action record
                bulk_action = BulkAction.objects.create(
                    action_type=action,
                    object_type='User',
                    object_ids=user_ids,
                    requested_by=request.user,
                    total_items=len(user_ids)
                )
                
                # Process bulk action
                process_bulk_user_action(bulk_action, form.cleaned_data)
                
                messages.success(request, f'Bulk action "{action}" initiated for {len(user_ids)} users.')
                return redirect('admin_dashboard:bulk_operations')
        
        elif action_type == 'places':
            form = BulkPlaceActionForm(request.POST)
            if form.is_valid():
                place_ids = form.cleaned_data['place_ids']
                action = form.cleaned_data['action']
                
                bulk_action = BulkAction.objects.create(
                    action_type=action,
                    object_type='Place',
                    object_ids=place_ids,
                    requested_by=request.user,
                    total_items=len(place_ids)
                )
                
                process_bulk_place_action(bulk_action)
                messages.success(request, f'Bulk action "{action}" initiated for {len(place_ids)} places.')
                return redirect('admin_dashboard:bulk_operations')
        
        elif action_type == 'packages':
            form = BulkPackageActionForm(request.POST)
            if form.is_valid():
                package_ids = form.cleaned_data['package_ids']
                action = form.cleaned_data['action']
                
                bulk_action = BulkAction.objects.create(
                    action_type=action,
                    object_type='Package',
                    object_ids=package_ids,
                    requested_by=request.user,
                    total_items=len(package_ids)
                )
                
                process_bulk_package_action(bulk_action)
                messages.success(request, f'Bulk action "{action}" initiated for {len(package_ids)} packages.')
                return redirect('admin_dashboard:bulk_operations')
        
        elif action_type == 'bookings':
            form = BulkBookingActionForm(request.POST)
            if form.is_valid():
                booking_ids = form.cleaned_data['booking_ids']
                action = form.cleaned_data['action']
                
                bulk_action = BulkAction.objects.create(
                    action_type=action,
                    object_type='Booking',
                    object_ids=booking_ids,
                    requested_by=request.user,
                    total_items=len(booking_ids)
                )
                
                process_bulk_booking_action(bulk_action)
                messages.success(request, f'Bulk action "{action}" initiated for {len(booking_ids)} bookings.')
                return redirect('admin_dashboard:bulk_operations')
    
    # Get recent bulk actions
    recent_actions = BulkAction.objects.all()[:10]
    
    context = {
        'recent_actions': recent_actions,
        'user_form': BulkUserActionForm(),
        'place_form': BulkPlaceActionForm(),
        'package_form': BulkPackageActionForm(),
        'booking_form': BulkBookingActionForm(),
    }
    return render(request, 'admin_dashboard/bulk_operations.html', context)

def process_bulk_user_action(bulk_action, form_data):
    """Process bulk user actions"""
    try:
        bulk_action.status = 'processing'
        bulk_action.save()
        
        user_ids = bulk_action.object_ids
        action = bulk_action.action_type
        
        for user_id in user_ids:
            try:
                user = User.objects.get(id=user_id)
                
                if action == 'activate':
                    user.is_active = True
                    user.save()
                elif action == 'deactivate':
                    user.is_active = False
                    user.save()
                elif action == 'delete':
                    user.delete()
                elif action == 'send_email':
                    # Send email logic here
                    pass
                
                bulk_action.processed_items += 1
                bulk_action.progress = int((bulk_action.processed_items / bulk_action.total_items) * 100)
                bulk_action.save()
                
            except User.DoesNotExist:
                continue
        
        bulk_action.status = 'completed'
        bulk_action.completed_at = timezone.now()
        bulk_action.save()
        
    except Exception as e:
        bulk_action.status = 'failed'
        bulk_action.error_message = str(e)
        bulk_action.save()

def process_bulk_place_action(bulk_action):
    """Process bulk place actions"""
    try:
        bulk_action.status = 'processing'
        bulk_action.save()
        
        place_ids = bulk_action.object_ids
        action = bulk_action.action_type
        
        for place_id in place_ids:
            try:
                place = Place.objects.get(id=place_id)
                
                if action == 'feature':
                    place.is_featured = True
                    place.save()
                elif action == 'unfeature':
                    place.is_featured = False
                    place.save()
                elif action == 'activate':
                    place.is_active = True
                    place.save()
                elif action == 'deactivate':
                    place.is_active = False
                    place.save()
                elif action == 'delete':
                    place.delete()
                
                bulk_action.processed_items += 1
                bulk_action.progress = int((bulk_action.processed_items / bulk_action.total_items) * 100)
                bulk_action.save()
                
            except Place.DoesNotExist:
                continue
        
        bulk_action.status = 'completed'
        bulk_action.completed_at = timezone.now()
        bulk_action.save()
        
    except Exception as e:
        bulk_action.status = 'failed'
        bulk_action.error_message = str(e)
        bulk_action.save()

def process_bulk_package_action(bulk_action):
    """Process bulk package actions"""
    try:
        bulk_action.status = 'processing'
        bulk_action.save()
        
        package_ids = bulk_action.object_ids
        action = bulk_action.action_type
        
        for package_id in package_ids:
            try:
                package = Package.objects.get(id=package_id)
                
                if action == 'feature':
                    package.is_featured = True
                    package.save()
                elif action == 'unfeature':
                    package.is_featured = False
                    package.save()
                elif action == 'activate':
                    package.is_active = True
                    package.save()
                elif action == 'deactivate':
                    package.is_active = False
                    package.save()
                elif action == 'delete':
                    package.delete()
                
                bulk_action.processed_items += 1
                bulk_action.progress = int((bulk_action.processed_items / bulk_action.total_items) * 100)
                bulk_action.save()
                
            except Package.DoesNotExist:
                continue
        
        bulk_action.status = 'completed'
        bulk_action.completed_at = timezone.now()
        bulk_action.save()
        
    except Exception as e:
        bulk_action.status = 'failed'
        bulk_action.error_message = str(e)
        bulk_action.save()

def process_bulk_booking_action(bulk_action):
    """Process bulk booking actions"""
    try:
        bulk_action.status = 'processing'
        bulk_action.save()
        
        booking_ids = bulk_action.object_ids
        action = bulk_action.action_type
        
        for booking_id in booking_ids:
            try:
                booking = Booking.objects.get(id=booking_id)
                
                if action == 'confirm':
                    booking.status = 'confirmed'
                    booking.save()
                elif action == 'cancel':
                    booking.status = 'cancelled'
                    booking.save()
                elif action == 'complete':
                    booking.status = 'completed'
                    booking.save()
                
                bulk_action.processed_items += 1
                bulk_action.progress = int((bulk_action.processed_items / bulk_action.total_items) * 100)
                bulk_action.save()
                
            except Booking.DoesNotExist:
                continue
        
        bulk_action.status = 'completed'
        bulk_action.completed_at = timezone.now()
        bulk_action.save()
        
    except Exception as e:
        bulk_action.status = 'failed'
        bulk_action.error_message = str(e)
        bulk_action.save()

# ==================== DATA EXPORT/IMPORT ====================

@admin_required
def data_export(request):
    """Data export management"""
    if request.method == 'POST':
        form = DataExportForm(request.POST)
        if form.is_valid():
            export_type = form.cleaned_data['export_type']
            filters = form.cleaned_data['filters']
            
            # Create export record
            export = DataExport.objects.create(
                export_type=export_type,
                requested_by=request.user,
                filters=filters
            )
            
            # Process export
            process_data_export(export)
            
            messages.success(request, 'Export initiated successfully.')
            return redirect('admin_dashboard:data_export')
    else:
        form = DataExportForm()
    
    # Get recent exports
    recent_exports = DataExport.objects.all()[:10]
    
    context = {
        'form': form,
        'recent_exports': recent_exports,
    }
    return render(request, 'admin_dashboard/data_export.html', context)

def process_data_export(export):
    """Process data export"""
    try:
        export.status = 'processing'
        export.save()
        
        # Generate CSV data based on export type
        if export.export_type == 'users':
            data = export_users_data(export.filters)
        elif export.export_type == 'bookings':
            data = export_bookings_data(export.filters)
        elif export.export_type == 'packages':
            data = export_packages_data(export.filters)
        elif export.export_type == 'places':
            data = export_places_data(export.filters)
        elif export.export_type == 'feedback':
            data = export_feedback_data(export.filters)
        elif export.export_type == 'payments':
            data = export_payments_data(export.filters)
        else:
            data = export_all_data(export.filters)
        
        # Save file
        filename = f"{export.export_type}_{export.export_id}.csv"
        file_path = default_storage.save(f'exports/{filename}', data)
        
        export.file_path = file_path
        export.file_size = data.size
        export.status = 'completed'
        export.completed_at = timezone.now()
        export.save()
        
    except Exception as e:
        export.status = 'failed'
        export.error_message = str(e)
        export.save()

def export_users_data(filters):
    """Export users data to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'Username', 'Email', 'First Name', 'Last Name', 'Role', 'Is Active', 'Date Joined'])
    
    # Get users
    users = User.objects.all()
    if filters:
        # Apply filters if any
        pass
    
    # Write data
    for user in users:
        writer.writerow([
            user.id,
            user.username,
            user.email,
            user.first_name,
            user.last_name,
            user.role,
            user.is_active,
            user.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

def export_bookings_data(filters):
    """Export bookings data to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'User', 'Package', 'Booking Date', 'From Date', 'To Date', 'Members Count', 'Total Price', 'Status'])
    
    # Get bookings
    bookings = Booking.objects.select_related('user', 'package').all()
    if filters:
        # Apply filters if any
        pass
    
    # Write data
    for booking in bookings:
        writer.writerow([
            booking.id,
            booking.user.username,
            booking.package.name,
            booking.booking_date.strftime('%Y-%m-%d'),
            booking.from_date.strftime('%Y-%m-%d') if booking.from_date else '',
            booking.to_date.strftime('%Y-%m-%d') if booking.to_date else '',
            booking.members_count,
            booking.total_price,
            booking.status
        ])
    
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

def export_packages_data(filters):
    """Export packages data to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'Name', 'Place', 'Description', 'Base Price', 'Duration Days', 'Max Capacity', 'Is Featured'])
    
    # Get packages
    packages = Package.objects.select_related('place').all()
    if filters:
        # Apply filters if any
        pass
    
    # Write data
    for package in packages:
        writer.writerow([
            package.id,
            package.name,
            package.place.name,
            package.description,
            package.base_price,
            package.duration_days,
            package.max_capacity,
            package.is_featured
        ])
    
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

def export_places_data(filters):
    """Export places data to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'Name', 'Location', 'Category', 'State', 'Rating', 'Is Featured', 'Created At'])
    
    # Get places
    places = Place.objects.all()
    if filters:
        # Apply filters if any
        pass
    
    # Write data
    for place in places:
        writer.writerow([
            place.id,
            place.name,
            place.location,
            place.category,
            place.state,
            place.rating,
            place.is_featured,
            place.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

def export_feedback_data(filters):
    """Export feedback data to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'User', 'Place', 'Package', 'Rating', 'Category', 'Comment', 'Is Helpful', 'Created At'])
    
    # Get feedback
    feedbacks = Feedback.objects.select_related('user', 'place', 'package').all()
    if filters:
        # Apply filters if any
        pass
    
    # Write data
    for feedback in feedbacks:
        writer.writerow([
            feedback.id,
            feedback.user.username,
            feedback.place.name if feedback.place else '',
            feedback.package.name if feedback.package else '',
            feedback.rating,
            feedback.category,
            feedback.comment,
            feedback.is_helpful,
            feedback.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

def export_payments_data(filters):
    """Export payments data to CSV"""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'User', 'Booking', 'Amount', 'Currency', 'Payment Method', 'Status', 'Transaction ID', 'Created At'])
    
    # Get payments
    payments = Payment.objects.select_related('user', 'booking').all()
    if filters:
        # Apply filters if any
        pass
    
    # Write data
    for payment in payments:
        writer.writerow([
            payment.id,
            payment.user.username,
            payment.booking.id if payment.booking else '',
            payment.amount,
            payment.currency,
            payment.payment_method,
            payment.payment_status,
            payment.transaction_id,
            payment.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

def export_all_data(filters):
    """Export all data to CSV"""
    # This would combine all the above exports
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['Data Type', 'ID', 'Details'])
    
    # Export each type
    for user in User.objects.all()[:100]:  # Limit for performance
        writer.writerow(['User', user.id, f"{user.username} - {user.email}"])
    
    for booking in Booking.objects.all()[:100]:
        writer.writerow(['Booking', booking.id, f"{booking.user.username} - {booking.package.name}"])
    
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

@admin_required
def download_export(request, export_id):
    """Download exported data"""
    export = get_object_or_404(DataExport, id=export_id)
    
    if export.status != 'completed' or not export.file_path:
        raise Http404("Export not available")
    
    try:
        file_path = export.file_path
        if default_storage.exists(file_path):
            response = HttpResponse(default_storage.open(file_path).read(), content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{export.export_type}_{export.export_id}.csv"'
            return response
        else:
            raise Http404("File not found")
    except Exception as e:
        raise Http404("Error downloading file")

# ==================== AJAX ENDPOINTS ====================

@admin_required
@require_http_methods(["POST"])
def mark_notification_read(request, notification_id):
    """Mark notification as read"""
    notification = get_object_or_404(AdminNotification, id=notification_id)
    notification.mark_as_read()
    return JsonResponse({'status': 'success'})

@admin_required
@require_http_methods(["POST"])
def get_bulk_action_progress(request, action_id):
    """Get bulk action progress"""
    try:
        bulk_action = BulkAction.objects.get(action_id=action_id)
        return JsonResponse({
            'status': bulk_action.status,
            'progress': bulk_action.progress,
            'processed_items': bulk_action.processed_items,
            'total_items': bulk_action.total_items,
            'error_message': bulk_action.error_message
        })
    except BulkAction.DoesNotExist:
        return JsonResponse({'error': 'Action not found'}, status=404)

@admin_required
@require_http_methods(["GET"])
def get_notification_count(request):
    """Get unread notification count"""
    count = AdminNotification.objects.filter(is_read=False).count()
    return JsonResponse({'count': count})

@admin_required
@require_http_methods(["GET"])
def get_recent_activities(request):
    """Get recent activities for dashboard"""
    recent_bookings = Booking.objects.select_related('user', 'package').order_by('-created_at')[:5]
    recent_feedback = Feedback.objects.select_related('user', 'place').order_by('-created_at')[:5]
    recent_users = User.objects.order_by('-date_joined')[:5]
    
    activities = []
    
    for booking in recent_bookings:
        activities.append({
            'type': 'booking',
            'message': f'New booking by {booking.user.username} for {booking.package.name}',
            'time': booking.created_at,
            'url': f'/admin/bookings/{booking.id}/'
        })
    
    for feedback in recent_feedback:
        activities.append({
            'type': 'feedback',
            'message': f'New feedback by {feedback.user.username} for {feedback.place.name if feedback.place else feedback.package.name}',
            'time': feedback.created_at,
            'url': f'/admin/feedback/{feedback.id}/'
        })
    
    for user in recent_users:
        activities.append({
            'type': 'user',
            'message': f'New user registered: {user.username}',
            'time': user.date_joined,
            'url': f'/admin/users/{user.id}/'
        })
    
    # Sort by time
    activities.sort(key=lambda x: x['time'], reverse=True)
    
    return JsonResponse({'activities': activities[:10]})

@admin_required
@require_http_methods(["GET"])
def get_recent_bookings(request):
    """Get recent bookings for dashboard"""
    try:
        # Get recent bookings
        bookings = Booking.objects.select_related('user', 'package').order_by('-created_at')[:10]
        
        bookings_data = []
        for booking in bookings:
            bookings_data.append({
                'id': booking.id,
                'user_name': booking.user.get_full_name() or booking.user.username,
                'package_name': booking.package.name,
                'amount': float(getattr(booking, 'total_price', 0) or 0),
                'status': booking.status,
                'date': booking.created_at.strftime('%b %d, %Y'),
                'created_at': booking.created_at.isoformat(),
            })
        
        return JsonResponse({
            'success': True,
            'bookings': bookings_data
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })

# ==================== PACKAGE MANAGEMENT (CRUD ENDPOINTS) ====================

@admin_required
def create_package(request):
    """Create a new package and redirect to package management.
    Note: Uses minimal fields if present to avoid model coupling issues."""
    if request.method == 'POST':
        try:
            data = request.POST
            package = Package()
            if hasattr(package, 'name'):
                package.name = data.get('name', getattr(package, 'name', ''))
            if hasattr(package, 'description'):
                package.description = data.get('description', getattr(package, 'description', ''))
            if hasattr(package, 'base_price'):
                package.base_price = data.get('base_price') or getattr(package, 'base_price', 0)
            if hasattr(package, 'duration_days'):
                package.duration_days = data.get('duration_days') or getattr(package, 'duration_days', 0)
            place_id = data.get('place_id') or data.get('place')
            if place_id:
                try:
                    place = Place.objects.get(id=place_id)
                    if hasattr(package, 'place'):
                        package.place = place
                except Place.DoesNotExist:
                    pass
            if hasattr(package, 'is_active'):
                package.is_active = (data.get('is_active') == 'on') if 'is_active' in data else getattr(package, 'is_active', True)
            if hasattr(package, 'is_featured'):
                package.is_featured = (data.get('is_featured') == 'on') if 'is_featured' in data else getattr(package, 'is_featured', False)
            package.save()
            log_admin_action(request.user, 'create', 'Package', package.id, getattr(package, 'name', str(package.id)))
            messages.success(request, 'Package created successfully.')
        except Exception as e:
            messages.error(request, f'Failed to create package: {e}')
    return redirect('admin_dashboard:package_management')

@admin_required
def package_detail(request, package_id):
    pkg = get_object_or_404(Package, id=package_id)
    return HttpResponse(f"Package #{pkg.id}: {getattr(pkg, 'name', '')}")

@admin_required
def edit_package(request, package_id):
    pkg = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        try:
            data = request.POST
            before = {
                'name': getattr(pkg, 'name', None),
                'is_active': getattr(pkg, 'is_active', None),
                'is_featured': getattr(pkg, 'is_featured', None),
            }
            if hasattr(pkg, 'name') and 'name' in data:
                pkg.name = data.get('name')
            if hasattr(pkg, 'description') and 'description' in data:
                pkg.description = data.get('description')
            if hasattr(pkg, 'base_price') and 'base_price' in data:
                pkg.base_price = data.get('base_price')
            if hasattr(pkg, 'duration_days') and 'duration_days' in data:
                pkg.duration_days = data.get('duration_days')
            if hasattr(pkg, 'is_active'):
                pkg.is_active = data.get('is_active') == 'on' if 'is_active' in data else pkg.is_active
            if hasattr(pkg, 'is_featured'):
                pkg.is_featured = data.get('is_featured') == 'on' if 'is_featured' in data else pkg.is_featured
            place_id = data.get('place_id') or data.get('place')
            if place_id and hasattr(pkg, 'place'):
                try:
                    pkg.place = Place.objects.get(id=place_id)
                except Place.DoesNotExist:
                    pass
            pkg.save()
            after = {
                'name': getattr(pkg, 'name', None),
                'is_active': getattr(pkg, 'is_active', None),
                'is_featured': getattr(pkg, 'is_featured', None),
            }
            changes = {k: {'old': before[k], 'new': after[k]} for k in before if before[k] != after[k]}
            log_admin_action(request.user, 'update', 'Package', pkg.id, getattr(pkg, 'name', str(pkg.id)), changes=changes)
            messages.success(request, 'Package updated successfully.')
        except Exception as e:
            messages.error(request, f'Failed to update package: {e}')
    return redirect('admin_dashboard:package_management')

@admin_required
def delete_package(request, package_id):
    pkg = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        name = getattr(pkg, 'name', str(pkg.id))
        pkg.delete()
        log_admin_action(request.user, 'delete', 'Package', package_id, name)
        messages.success(request, 'Package deleted successfully.')
    else:
        messages.error(request, 'Invalid request method for delete.')
    return redirect('admin_dashboard:package_management')

# ==================== EVENT MANAGEMENT (CRUD ENDPOINTS) ====================

@admin_required
def create_event(request):
    if request.method == 'POST':
        try:
            data = request.POST
            event = Event()
            for field in ['title', 'description', 'location']:
                if hasattr(event, field) and field in data:
                    setattr(event, field, data.get(field))
            if hasattr(event, 'day_number') and 'day_number' in data:
                try:
                    event.day_number = int(data.get('day_number'))
                except Exception:
                    pass
            if hasattr(event, 'time_slot') and 'time_slot' in data:
                event.time_slot = data.get('time_slot')
            package_id = data.get('package_id') or data.get('package')
            if package_id and hasattr(event, 'package'):
                try:
                    event.package = Package.objects.get(id=package_id)
                except Package.DoesNotExist:
                    pass
            event.save()
            log_admin_action(request.user, 'create', 'Event', event.id, getattr(event, 'title', str(event.id)))
            messages.success(request, 'Event created successfully.')
        except Exception as e:
            messages.error(request, f'Failed to create event: {e}')
    return redirect('admin_dashboard:event_management')

@admin_required
def event_detail(request, event_id):
    ev = get_object_or_404(Event, id=event_id)
    return HttpResponse(f"Event #{ev.id}: {getattr(ev, 'title', '')}")

@admin_required
def edit_event(request, event_id):
    ev = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        try:
            data = request.POST
            before = {k: getattr(ev, k, None) for k in ['title', 'location', 'time_slot'] if hasattr(ev, k)}
            for field in ['title', 'description', 'location', 'time_slot']:
                if hasattr(ev, field) and field in data:
                    setattr(ev, field, data.get(field))
            if hasattr(ev, 'day_number') and 'day_number' in data:
                try:
                    ev.day_number = int(data.get('day_number'))
                except Exception:
                    pass
            package_id = data.get('package_id') or data.get('package')
            if package_id and hasattr(ev, 'package'):
                try:
                    ev.package = Package.objects.get(id=package_id)
                except Package.DoesNotExist:
                    pass
            ev.save()
            after = {k: getattr(ev, k, None) for k in ['title', 'location', 'time_slot'] if hasattr(ev, k)}
            changes = {k: {'old': before[k], 'new': after[k]} for k in before if before[k] != after[k]}
            log_admin_action(request.user, 'update', 'Event', ev.id, getattr(ev, 'title', str(ev.id)), changes=changes)
            messages.success(request, 'Event updated successfully.')
        except Exception as e:
            messages.error(request, f'Failed to update event: {e}')
    return redirect('admin_dashboard:event_management')

@admin_required
def delete_event(request, event_id):
    ev = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        title = getattr(ev, 'title', str(ev.id))
        ev.delete()
        log_admin_action(request.user, 'delete', 'Event', event_id, title)
        messages.success(request, 'Event deleted successfully.')
    else:
        messages.error(request, 'Invalid request method for delete.')
    return redirect('admin_dashboard:event_management')

# ==================== PAYMENT MANAGEMENT (CRUD ENDPOINTS) ====================

@admin_required
def payment_detail(request, payment_id):
    pay = get_object_or_404(Payment, id=payment_id)
    return HttpResponse(f"Payment #{pay.id}: {float(getattr(pay, 'amount', 0))}")

@admin_required
def edit_payment(request, payment_id):
    pay = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        try:
            data = request.POST
            if 'status' in data and hasattr(pay, 'status'):
                pay.status = data.get('status')
            if 'payment_status' in data and hasattr(pay, 'payment_status'):
                pay.payment_status = data.get('payment_status')
            if 'amount' in data and hasattr(pay, 'amount'):
                try:
                    pay.amount = float(data.get('amount'))
                except Exception:
                    pass
            if 'payment_method' in data and hasattr(pay, 'payment_method'):
                pay.payment_method = data.get('payment_method')
            if 'currency' in data and hasattr(pay, 'currency'):
                pay.currency = data.get('currency')
            pay.save()
            log_admin_action(request.user, 'update', 'Payment', pay.id, str(pay.id))
            messages.success(request, 'Payment updated successfully.')
        except Exception as e:
            messages.error(request, f'Failed to update payment: {e}')
    return redirect('admin_dashboard:payment_management')

@admin_required
def delete_payment(request, payment_id):
    pay = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        pay.delete()
        log_admin_action(request.user, 'delete', 'Payment', payment_id, str(payment_id))
        messages.success(request, 'Payment deleted successfully.')
    else:
        messages.error(request, 'Invalid request method for delete.')
    return redirect('admin_dashboard:payment_management')

# ==================== FEEDBACK MANAGEMENT (CRUD ENDPOINTS) ====================

@admin_required
def feedback_detail(request, feedback_id):
    fb = get_object_or_404(Feedback, id=feedback_id)
    return HttpResponse(f"Feedback #{fb.id}: rating {getattr(fb, 'rating', '-')}")

@admin_required
def edit_feedback(request, feedback_id):
    fb = get_object_or_404(Feedback, id=feedback_id)
    if request.method == 'POST':
        try:
            data = request.POST
            if 'rating' in data and hasattr(fb, 'rating'):
                try:
                    fb.rating = int(data.get('rating'))
                except Exception:
                    pass
            if 'comment' in data and hasattr(fb, 'comment'):
                fb.comment = data.get('comment')
            if hasattr(fb, 'is_approved'):
                if 'is_approved' in data:
                    fb.is_approved = data.get('is_approved') == 'on'
            fb.save()
            log_admin_action(request.user, 'update', 'Feedback', fb.id, str(fb.id))
            messages.success(request, 'Feedback updated successfully.')
        except Exception as e:
            messages.error(request, f'Failed to update feedback: {e}')
    return redirect('admin_dashboard:feedback_management')

@admin_required
def delete_feedback(request, feedback_id):
    fb = get_object_or_404(Feedback, id=feedback_id)
    if request.method == 'POST':
        fb.delete()
        log_admin_action(request.user, 'delete', 'Feedback', feedback_id, str(feedback_id))
        messages.success(request, 'Feedback deleted successfully.')
    else:
        messages.error(request, 'Invalid request method for delete.')
    return redirect('admin_dashboard:feedback_management')

# ==================== RENDER AUTO-LOGIN (SECURE, TOKEN-GATED) ====================

@require_http_methods(["GET"])
def auto_login_admin(request):
    """Render-only: auto-login an admin using a secret token.

    Security:
    - Enabled only when ADMIN_AUTO_LOGIN_ENABLED=true
    - Requires token match with ADMIN_AUTO_LOGIN_TOKEN
    - Creates admin if missing (username/password pulled from env)
    - Intended for deployment bootstrap; disable after first use
    """
    enabled = os.environ.get('ADMIN_AUTO_LOGIN_ENABLED', 'false').lower() == 'true'
    token = request.GET.get('token', '')
    expected = os.environ.get('ADMIN_AUTO_LOGIN_TOKEN', '')

    if not enabled or not expected or token != expected:
        raise Http404("Not found")

    # Ensure admin user exists
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    password = os.environ.get('ADMIN_PASSWORD', 'admin123')

    user, created = User.objects.get_or_create(username=username, defaults={
        'email': os.environ.get('ADMIN_EMAIL', 'admin@example.com'),
        'is_active': True,
    })

    # Elevate privileges for custom User model
    if hasattr(user, 'is_staff'):
        user.is_staff = True
    if hasattr(user, 'is_superuser'):
        user.is_superuser = True
    if hasattr(user, 'is_admin'):
        user.is_admin = True
    # Reset password if created
    if created:
        user.set_password(password)
    user.save()

    # Log the user in via ModelBackend
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth_login(request, user)

    messages.success(request, 'Logged in as admin.')
    return redirect('admin_dashboard:dashboard')

@admin_required
@require_http_methods(["GET"])
def get_system_status(request):
    """Get system status for dashboard"""
    try:
        # Check various system components
        status = {
            'database': 'online',
            'email': 'online',
            'payment': 'online',
            'storage': 'online'
        }
        
        # Check database connection
        try:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        except Exception:
            status['database'] = 'offline'
        
        # Check email settings
        try:
            from django.core.mail import get_connection
            connection = get_connection()
            connection.open()
            connection.close()
        except Exception:
            status['email'] = 'offline'
        
        # Check file storage
        try:
            from django.core.files.storage import default_storage
            default_storage.exists('test')
        except Exception:
            status['storage'] = 'offline'
        
        return JsonResponse({
            'success': True,
            'status': status
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })
