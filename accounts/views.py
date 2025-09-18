from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.utils import timezone
from django.urls import reverse
from .models import User, PasswordResetToken
from .forms import UserRegistrationForm, UserProfileForm, ForgotPasswordForm, PasswordResetForm
from packages.models import Package
from places.models import Place
from bookings.models import Booking
import json

def home(request):
    """Home page with featured places and packages"""
    featured_places = Place.objects.filter(is_featured=True)[:6]
    featured_packages = Package.objects.filter(is_featured=True)[:6]
    
    context = {
        'featured_places': featured_places,
        'featured_packages': featured_packages,
    }
    return render(request, 'accounts/home.html', context)

def register_view(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            
            # Send welcome email
            try:
                from utils.email_service import EmailService
                EmailService.send_welcome_email(user)
            except Exception as e:
                print(f"Failed to send welcome email: {e}")
            
            messages.success(request, 'Registration successful! Welcome to Prayanam.')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Send login alert email
            try:
                from utils.email_service import EmailService
                EmailService.send_login_alert(user, request)
            except Exception as e:
                print(f"Failed to send login alert email: {e}")
            
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile_view(request):
    """User profile view"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def user_dashboard(request):
    """User dashboard with booking history and preferences"""
    user_bookings = Booking.objects.filter(user=request.user).order_by('-created_at')[:5]
    recent_packages = Package.objects.all()[:3]
    
    context = {
        'user_bookings': user_bookings,
        'recent_packages': recent_packages,
    }
    return render(request, 'accounts/dashboard.html', context)

def contact_us(request):
    """Contact Us page"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            
            # In a real application, this would send an email or save to database
            # For now, we'll just return a success response
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! We will get back to you soon.'
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid form data'
            })
    
    return render(request, 'accounts/contact_us.html')

def faq(request):
    """FAQ page"""
    faqs = [
        {
            'question': 'How do I book a travel package?',
            'answer': 'You can browse our packages, select your preferred dates and group size, and proceed to book. You\'ll need to create an account or log in to complete your booking.'
        },
        {
            'question': 'What payment methods do you accept?',
            'answer': 'We accept credit cards, debit cards, UPI, net banking, and digital wallets like Paytm, PhonePe, and Google Pay.'
        },
        {
            'question': 'Can I cancel my booking?',
            'answer': 'Yes, you can cancel your booking up to 48 hours before the trip start date. Cancellation fees may apply based on the package terms.'
        },
        {
            'question': 'Do you provide travel insurance?',
            'answer': 'Yes, we offer comprehensive travel insurance for all our packages. You can opt for additional coverage during the booking process.'
        },
        {
            'question': 'What if there are changes to my itinerary?',
            'answer': 'We will notify you immediately of any changes to your itinerary. In case of significant changes, you may be eligible for a refund or alternative arrangements.'
        },
        {
            'question': 'How do I contact customer support?',
            'answer': 'You can reach our customer support team through the Contact Us page, email us at support@prayanam.com, or call us at +91 1800-123-4567.'
        },
        {
            'question': 'Are meals included in the package?',
            'answer': 'Meal inclusions vary by package. You can check the detailed itinerary for each package to see what meals are included.'
        },
        {
            'question': 'What documents do I need for booking?',
            'answer': 'You\'ll need a valid government ID (Aadhar, PAN, or Passport) for booking. For international packages, you\'ll also need a valid passport and visa.'
        }
    ]
    
    context = {
        'faqs': faqs
    }
    return render(request, 'accounts/faq.html', context)

def help_center(request):
    """Help Center page"""
    help_categories = [
        {
            'title': 'Booking & Reservations',
            'icon': 'fas fa-calendar-check',
            'topics': [
                'How to book a package',
                'Modifying your booking',
                'Cancellation policies',
                'Payment options'
            ]
        },
        {
            'title': 'Travel Information',
            'icon': 'fas fa-plane',
            'topics': [
                'Travel documents required',
                'Baggage allowances',
                'Travel insurance',
                'Visa requirements'
            ]
        },
        {
            'title': 'Account & Profile',
            'icon': 'fas fa-user',
            'topics': [
                'Creating an account',
                'Updating profile information',
                'Password reset',
                'Account security'
            ]
        },
        {
            'title': 'Payment & Billing',
            'icon': 'fas fa-credit-card',
            'topics': [
                'Payment methods',
                'Billing information',
                'Refund process',
                'Payment security'
            ]
        },
        {
            'title': 'Customer Support',
            'icon': 'fas fa-headset',
            'topics': [
                'Contact information',
                'Live chat support',
                'Email support',
                'Phone support'
            ]
        },
        {
            'title': 'Technical Issues',
            'icon': 'fas fa-tools',
            'topics': [
                'Website navigation',
                'Mobile app support',
                'Browser compatibility',
                'Error troubleshooting'
            ]
        }
    ]
    
    context = {
        'help_categories': help_categories
    }
    return render(request, 'accounts/help_center.html', context)

def change_language(request):
    """Change user language preference"""
    if request.method == 'POST':
        language = request.POST.get('language')
        if language in ['en', 'te', 'hi']:
            # Set language in session
            request.session['django_language'] = language
            # Set language in user profile if logged in
            if request.user.is_authenticated:
                request.user.language_preference = language
                request.user.save()
            messages.success(request, f'Language changed to {language.upper()}')
        else:
            messages.error(request, 'Invalid language selection')
    
    # Redirect back to the previous page
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def set_language_from_url(request, language_code):
    """Set language from URL parameter"""
    if language_code in ['en', 'te', 'hi']:
        request.session['django_language'] = language_code
        if request.user.is_authenticated:
            request.user.language_preference = language_code
            request.user.save()
        messages.success(request, f'Language set to {language_code.upper()}')
    
    return redirect('home')

def language_demo(request):
    """Language switcher demo page"""
    return render(request, 'accounts/language_demo.html')


def forgot_password(request):
    """Handle forgot password request"""
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                
                # Create password reset token
                reset_token = PasswordResetToken.objects.create(user=user)
                
                # Generate reset URL
                reset_url = request.build_absolute_uri(
                    reverse('password_reset_confirm', kwargs={'token': str(reset_token.token)})
                )
                
                # Send password reset email
                try:
                    from utils.email_service import EmailService
                    EmailService.send_password_reset_email(user, reset_url)
                    messages.success(request, 'Password reset instructions have been sent to your email address.')
                except Exception as e:
                    print(f"Failed to send password reset email: {e}")
                    messages.error(request, 'Failed to send password reset email. Please try again.')
                
                return redirect('forgot_password')
                
            except User.DoesNotExist:
                # Don't reveal if email exists or not for security
                messages.success(request, 'If an account with this email exists, password reset instructions have been sent.')
                return redirect('forgot_password')
    else:
        form = ForgotPasswordForm()
    
    return render(request, 'accounts/forgot_password.html', {'form': form})


def password_reset_confirm(request, token):
    """Handle password reset confirmation"""
    try:
        reset_token = get_object_or_404(PasswordResetToken, token=token)
        
        if not reset_token.is_valid():
            messages.error(request, 'This password reset link has expired or is invalid.')
            return redirect('forgot_password')
        
        if request.method == 'POST':
            form = PasswordResetForm(user=reset_token.user, data=request.POST)
            if form.is_valid():
                form.save()
                reset_token.mark_as_used()
                messages.success(request, 'Your password has been reset successfully. You can now log in with your new password.')
                return redirect('login')
        else:
            form = PasswordResetForm(user=reset_token.user)
        
        return render(request, 'accounts/password_reset_confirm.html', {
            'form': form,
            'token': token
        })
        
    except Exception as e:
        messages.error(request, 'Invalid password reset link.')
        return redirect('forgot_password')


def profile_view(request):
    """User profile view"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form})
