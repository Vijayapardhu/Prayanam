from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feedback
from places.models import Place
from packages.models import Package
from .forms import FeedbackForm

def feedback_list(request):
    """Display all feedback"""
    feedback = Feedback.objects.select_related('user', 'place', 'package').all()
    return render(request, 'feedback/feedback_list.html', {'feedback': feedback})

@login_required
def create_feedback(request):
    """Create new feedback"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('feedback_detail', feedback_id=feedback.id)
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/create_feedback.html', {'form': form})

def feedback_detail(request, feedback_id):
    """Display feedback details"""
    feedback = get_object_or_404(Feedback, id=feedback_id)
    return render(request, 'feedback/feedback_detail.html', {'feedback': feedback})

@login_required
def edit_feedback(request, feedback_id):
    """Edit feedback (only by the author)"""
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback updated successfully!')
            return redirect('feedback_detail', feedback_id=feedback.id)
    else:
        form = FeedbackForm(instance=feedback)
    
    return render(request, 'feedback/edit_feedback.html', {'form': form, 'feedback': feedback})

@login_required
def delete_feedback(request, feedback_id):
    """Delete feedback (only by the author)"""
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    
    if request.method == 'POST':
        feedback.delete()
        messages.success(request, 'Feedback deleted successfully!')
        return redirect('feedback_list')
    
    return render(request, 'feedback/delete_feedback.html', {'feedback': feedback})

def place_feedback(request, place_id):
    """Display feedback for a specific place"""
    place = get_object_or_404(Place, id=place_id)
    feedback = place.feedbacks.all()
    
    context = {
        'place': place,
        'feedback': feedback,
    }
    return render(request, 'feedback/place_feedback.html', context)

def package_feedback(request, package_id):
    """Display feedback for a specific package"""
    package = get_object_or_404(Package, id=package_id)
    feedback = package.feedbacks.all()
    
    context = {
        'package': package,
        'feedback': feedback,
    }
    return render(request, 'feedback/package_feedback.html', context)

from places.models import Place
from packages.models import Package
from .forms import FeedbackForm

def feedback_list(request):
    """Display all feedback"""
    feedback = Feedback.objects.select_related('user', 'place', 'package').all()
    return render(request, 'feedback/feedback_list.html', {'feedback': feedback})

@login_required
def create_feedback(request):
    """Create new feedback"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('feedback_detail', feedback_id=feedback.id)
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/create_feedback.html', {'form': form})

def feedback_detail(request, feedback_id):
    """Display feedback details"""
    feedback = get_object_or_404(Feedback, id=feedback_id)
    return render(request, 'feedback/feedback_detail.html', {'feedback': feedback})

@login_required
def edit_feedback(request, feedback_id):
    """Edit feedback (only by the author)"""
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback updated successfully!')
            return redirect('feedback_detail', feedback_id=feedback.id)
    else:
        form = FeedbackForm(instance=feedback)
    
    return render(request, 'feedback/edit_feedback.html', {'form': form, 'feedback': feedback})

@login_required
def delete_feedback(request, feedback_id):
    """Delete feedback (only by the author)"""
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    
    if request.method == 'POST':
        feedback.delete()
        messages.success(request, 'Feedback deleted successfully!')
        return redirect('feedback_list')
    
    return render(request, 'feedback/delete_feedback.html', {'feedback': feedback})

def place_feedback(request, place_id):
    """Display feedback for a specific place"""
    place = get_object_or_404(Place, id=place_id)
    feedback = place.feedbacks.all()
    
    context = {
        'place': place,
        'feedback': feedback,
    }
    return render(request, 'feedback/place_feedback.html', context)

def package_feedback(request, package_id):
    """Display feedback for a specific package"""
    package = get_object_or_404(Package, id=package_id)
    feedback = package.feedbacks.all()
    
    context = {
        'package': package,
        'feedback': feedback,
    }
    return render(request, 'feedback/package_feedback.html', context)
