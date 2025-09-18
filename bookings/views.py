from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Booking, BookingMember
from packages.models import Package
from .forms import BookingForm, BookingMemberForm

@login_required
def bookings_list(request):
    """Display user's booking history"""
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/bookings_list.html', {'bookings': bookings})

@login_required
def create_booking(request, package_id):
    """Create a new booking for a package"""
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.package = package
            
            # Calculate total price
            season = request.POST.get('season', 'summer')
            members_count = form.cleaned_data['members_count']
            booking.total_price = package.calculate_price(season, members_count)
            
            # Set from_date and to_date based on package duration
            from_date = form.cleaned_data['from_date']
            booking.from_date = from_date
            
            # Calculate to_date based on package duration
            from datetime import timedelta
            booking.to_date = from_date + timedelta(days=package.duration_days - 1)
            
            booking.save()
            
            messages.success(request, f'Booking created successfully for {package.name}!')
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm()
    
    context = {
        'form': form,
        'package': package,
    }
    return render(request, 'bookings/create_booking.html', context)

@login_required
def booking_detail(request, booking_id):
    """Display booking details"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    members = booking.members.all()
    
    context = {
        'booking': booking,
        'members': members,
    }
    return render(request, 'bookings/booking_detail.html', context)

@login_required
def cancel_booking(request, booking_id):
    """Cancel a booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.error(request, 'Cannot cancel this booking.')
    
    return redirect('booking_detail', booking_id=booking.id)

@login_required
def add_member(request, booking_id):
    """Add a member to a booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        form = BookingMemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.booking = booking
            member.save()
            
            messages.success(request, 'Member added successfully.')
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingMemberForm()
    
    context = {
        'form': form,
        'booking': booking,
    }
    return render(request, 'bookings/add_member.html', context)
