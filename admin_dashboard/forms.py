from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
import json

from .models import (
    AdminSettings, AdminNotification, AdminRole, SystemMaintenance,
    DataExport, BulkAction, AdminDashboardWidget, AdminReport
)
from accounts.models import User
from places.models import Place
from packages.models import Package
from bookings.models import Booking
from feedback.models import Feedback
from payments.models import Payment

User = get_user_model()

class AdminSettingsForm(forms.ModelForm):
    class Meta:
        model = AdminSettings
        fields = ['key', 'value', 'setting_type', 'description', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'value': forms.Textarea(attrs={'rows': 4}),
        }

class AdminNotificationForm(forms.ModelForm):
    class Meta:
        model = AdminNotification
        fields = ['title', 'message', 'notification_type', 'priority', 'is_global', 'target_admin']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
            'target_admin': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target_admin'].queryset = User.objects.filter(is_admin=True)
        self.fields['target_admin'].required = False

class AdminRoleForm(forms.ModelForm):
    permissions = forms.MultipleChoiceField(
        choices=[
            ('view_dashboard', 'View Dashboard'),
            ('manage_users', 'Manage Users'),
            ('manage_places', 'Manage Places'),
            ('manage_packages', 'Manage Packages'),
            ('manage_bookings', 'Manage Bookings'),
            ('manage_feedback', 'Manage Feedback'),
            ('manage_payments', 'Manage Payments'),
            ('view_analytics', 'View Analytics'),
            ('manage_settings', 'Manage Settings'),
            ('manage_notifications', 'Manage Notifications'),
            ('export_data', 'Export Data'),
            ('bulk_actions', 'Bulk Actions'),
            ('view_audit_logs', 'View Audit Logs'),
            ('manage_roles', 'Manage Roles'),
            ('system_maintenance', 'System Maintenance'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = AdminRole
        fields = ['name', 'description', 'permissions', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class SystemMaintenanceForm(forms.ModelForm):
    class Meta:
        model = SystemMaintenance
        fields = ['title', 'description', 'scheduled_start', 'scheduled_end', 'is_public_notice', 'public_message']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'public_message': forms.Textarea(attrs={'rows': 3}),
            'scheduled_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'scheduled_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        scheduled_start = cleaned_data.get('scheduled_start')
        scheduled_end = cleaned_data.get('scheduled_end')
        
        if scheduled_start and scheduled_end:
            if scheduled_start >= scheduled_end:
                raise ValidationError('Scheduled end time must be after start time.')
            
            if scheduled_start <= timezone.now():
                raise ValidationError('Scheduled start time must be in the future.')
        
        return cleaned_data

class DataExportForm(forms.ModelForm):
    class Meta:
        model = DataExport
        fields = ['export_type', 'filters']
        widgets = {
            'filters': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter JSON filters'}),
        }

    def clean_filters(self):
        filters = self.cleaned_data.get('filters')
        if filters:
            try:
                json.loads(filters)
            except json.JSONDecodeError:
                raise ValidationError('Filters must be valid JSON.')
        return filters

class BulkActionForm(forms.ModelForm):
    object_ids = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter object IDs separated by commas'}),
        help_text='Enter object IDs separated by commas'
    )
    
    class Meta:
        model = BulkAction
        fields = ['action_type', 'object_type', 'object_ids', 'parameters']
        widgets = {
            'parameters': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter JSON parameters'}),
        }

    def clean_object_ids(self):
        object_ids = self.cleaned_data.get('object_ids')
        if object_ids:
            try:
                ids = [int(id.strip()) for id in object_ids.split(',') if id.strip()]
                return ids
            except ValueError:
                raise ValidationError('Object IDs must be valid integers separated by commas.')
        return []

    def clean_parameters(self):
        parameters = self.cleaned_data.get('parameters')
        if parameters:
            try:
                json.loads(parameters)
            except json.JSONDecodeError:
                raise ValidationError('Parameters must be valid JSON.')
        return parameters

class AdminDashboardWidgetForm(forms.ModelForm):
    class Meta:
        model = AdminDashboardWidget
        fields = ['name', 'widget_type', 'title', 'description', 'configuration', 'position_x', 'position_y', 'width', 'height', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'configuration': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Enter JSON configuration'}),
        }

    def clean_configuration(self):
        configuration = self.cleaned_data.get('configuration')
        if configuration:
            try:
                json.loads(configuration)
            except json.JSONDecodeError:
                raise ValidationError('Configuration must be valid JSON.')
        return configuration

class AdminReportForm(forms.ModelForm):
    class Meta:
        model = AdminReport
        fields = ['name', 'description', 'report_type', 'query', 'parameters', 'is_scheduled', 'schedule_cron', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'query': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Enter SQL query or configuration'}),
            'parameters': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter JSON parameters'}),
        }

    def clean_parameters(self):
        parameters = self.cleaned_data.get('parameters')
        if parameters:
            try:
                json.loads(parameters)
            except json.JSONDecodeError:
                raise ValidationError('Parameters must be valid JSON.')
        return parameters

class UserManagementForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'language_preference', 'phone', 'address', 'is_active']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class PlaceManagementForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'description', 'image', 'season', 'category', 'state', 'district', 
                 'latitude', 'longitude', 'average_temperature', 'best_time_to_visit', 'entry_fee', 
                 'opening_hours', 'rating', 'is_featured', 'is_popular']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class PackageManagementForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'place', 'description', 'base_price', 'duration_days', 'max_capacity', 
                 'is_featured', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class BookingManagementForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'package', 'booking_date', 'from_date', 'to_date', 'members_count', 
                 'total_price', 'status', 'food_preference', 'special_requests']
        widgets = {
            'special_requests': forms.Textarea(attrs={'rows': 3}),
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FeedbackManagementForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'place', 'package', 'rating', 'category', 'comment', 'is_helpful']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

class PaymentManagementForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'user', 'amount', 'currency', 'payment_method', 'payment_status', 
                 'transaction_id', 'gateway_transaction_id', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class BulkUserActionForm(forms.Form):
    ACTION_CHOICES = [
        ('activate', 'Activate Users'),
        ('deactivate', 'Deactivate Users'),
        ('delete', 'Delete Users'),
        ('export', 'Export Users'),
        ('send_email', 'Send Email'),
    ]
    
    action = forms.ChoiceField(choices=ACTION_CHOICES)
    user_ids = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter user IDs separated by commas'}),
        help_text='Enter user IDs separated by commas'
    )
    email_subject = forms.CharField(required=False, max_length=200)
    email_message = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4}))

class BulkPlaceActionForm(forms.Form):
    ACTION_CHOICES = [
        ('feature', 'Mark as Featured'),
        ('unfeature', 'Remove from Featured'),
        ('activate', 'Activate Places'),
        ('deactivate', 'Deactivate Places'),
        ('delete', 'Delete Places'),
        ('export', 'Export Places'),
    ]
    
    action = forms.ChoiceField(choices=ACTION_CHOICES)
    place_ids = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter place IDs separated by commas'}),
        help_text='Enter place IDs separated by commas'
    )

class BulkPackageActionForm(forms.Form):
    ACTION_CHOICES = [
        ('feature', 'Mark as Featured'),
        ('unfeature', 'Remove from Featured'),
        ('activate', 'Activate Packages'),
        ('deactivate', 'Deactivate Packages'),
        ('delete', 'Delete Packages'),
        ('export', 'Export Packages'),
    ]
    
    action = forms.ChoiceField(choices=ACTION_CHOICES)
    package_ids = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter package IDs separated by commas'}),
        help_text='Enter package IDs separated by commas'
    )

class BulkBookingActionForm(forms.Form):
    ACTION_CHOICES = [
        ('confirm', 'Confirm Bookings'),
        ('cancel', 'Cancel Bookings'),
        ('complete', 'Mark as Completed'),
        ('export', 'Export Bookings'),
    ]
    
    action = forms.ChoiceField(choices=ACTION_CHOICES)
    booking_ids = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter booking IDs separated by commas'}),
        help_text='Enter booking IDs separated by commas'
    )

class AnalyticsFilterForm(forms.Form):
    PERIOD_CHOICES = [
        ('7', 'Last 7 days'),
        ('30', 'Last 30 days'),
        ('90', 'Last 90 days'),
        ('365', 'Last year'),
        ('custom', 'Custom range'),
    ]
    
    period = forms.ChoiceField(choices=PERIOD_CHOICES, initial='30')
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean(self):
        cleaned_data = super().clean()
        period = cleaned_data.get('period')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if period == 'custom':
            if not start_date or not end_date:
                raise ValidationError('Start date and end date are required for custom period.')
            if start_date >= end_date:
                raise ValidationError('End date must be after start date.')
        
        return cleaned_data

class SearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search...', 'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
        
        if self.model:
            # Add model-specific filters
            if hasattr(self.model, 'CATEGORY_CHOICES'):
                self.fields['category'] = forms.ChoiceField(
                    choices=[('', 'All Categories')] + list(self.model.CATEGORY_CHOICES),
                    required=False
                )
            
            if hasattr(self.model, 'STATUS_CHOICES'):
                self.fields['status'] = forms.ChoiceField(
                    choices=[('', 'All Statuses')] + list(self.model.STATUS_CHOICES),
                    required=False
                )
