from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from packages.models import Package
from .forms import EventForm

def events_list(request):
    """Display all events"""
    events = Event.objects.select_related('package').all()
    return render(request, 'events/events_list.html', {'events': events})

def package_events(request, package_id):
    """Display events for a specific package"""
    package = get_object_or_404(Package, id=package_id)
    events = package.events.all().order_by('day_number', 'time_slot')
    
    context = {
        'package': package,
        'events': events,
    }
    return render(request, 'events/package_events.html', context)

@login_required
def create_event(request):
    """Create a new event (admin only)"""
    if not request.user.is_admin:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('home')
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    
    return render(request, 'events/create_event.html', {'form': form})

def event_detail(request, event_id):
    """Display event details"""
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def edit_event(request, event_id):
    """Edit an event (admin only)"""
    if not request.user.is_admin:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('home')
    
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    """Delete an event (admin only)"""
    if not request.user.is_admin:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('home')
    
    event = get_object_or_404(Event, id=event_id)
    package_id = event.package.id
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('package_events', package_id=package_id)
    
    return render(request, 'events/delete_event.html', {'event': event})

from packages.models import Package
from .forms import EventForm

def events_list(request):
    """Display all events"""
    events = Event.objects.select_related('package').all()
    return render(request, 'events/events_list.html', {'events': events})

def package_events(request, package_id):
    """Display events for a specific package"""
    package = get_object_or_404(Package, id=package_id)
    events = package.events.all().order_by('day_number', 'time_slot')
    
    context = {
        'package': package,
        'events': events,
    }
    return render(request, 'events/package_events.html', context)

@login_required
def create_event(request):
    """Create a new event (admin only)"""
    if not request.user.is_admin:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('home')
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    
    return render(request, 'events/create_event.html', {'form': form})

def event_detail(request, event_id):
    """Display event details"""
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def edit_event(request, event_id):
    """Edit an event (admin only)"""
    if not request.user.is_admin:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('home')
    
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    """Delete an event (admin only)"""
    if not request.user.is_admin:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('home')
    
    event = get_object_or_404(Event, id=event_id)
    package_id = event.package.id
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('package_events', package_id=package_id)
    
    return render(request, 'events/delete_event.html', {'event': event})
