from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

User = get_user_model()

class AdminSettings(models.Model):
    """System-wide admin settings"""
    SETTING_TYPES = [
        ('general', 'General'),
        ('booking', 'Booking'),
        ('payment', 'Payment'),
        ('email', 'Email'),
        ('notification', 'Notification'),
        ('security', 'Security'),
        ('api', 'API'),
    ]
    
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    setting_type = models.CharField(max_length=20, choices=SETTING_TYPES, default='general')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['setting_type', 'key']
        verbose_name = 'Admin Setting'
        verbose_name_plural = 'Admin Settings'
    
    def __str__(self):
        return f"{self.key} ({self.setting_type})"

class AdminNotification(models.Model):
    """Admin notification system"""
    NOTIFICATION_TYPES = [
        ('booking', 'New Booking'),
        ('payment', 'Payment Update'),
        ('feedback', 'New Feedback'),
        ('user', 'User Activity'),
        ('system', 'System Alert'),
        ('maintenance', 'Maintenance'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_read = models.BooleanField(default=False)
    is_global = models.BooleanField(default=False)  # Show to all admins
    target_admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    related_object_id = models.PositiveIntegerField(null=True, blank=True)
    related_object_type = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.get_priority_display()}"
    
    def mark_as_read(self):
        self.is_read = True
        self.read_at = timezone.now()
        self.save()

class AdminAuditLog(models.Model):
    """Audit log for admin actions"""
    ACTION_TYPES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('view', 'View'),
        ('export', 'Export'),
        ('import', 'Import'),
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('settings', 'Settings Change'),
    ]
    
    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20, choices=ACTION_TYPES)
    object_type = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_name = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    changes = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['admin_user', 'created_at']),
            models.Index(fields=['action', 'created_at']),
            models.Index(fields=['object_type', 'object_id']),
        ]
    
    def __str__(self):
        return f"{self.admin_user} - {self.action} {self.object_type}"

class AdminRole(models.Model):
    """Admin roles and permissions"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    permissions = models.JSONField(default=list)  # List of permission codes
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class AdminUserRole(models.Model):
    """Link users to admin roles"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(AdminRole, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_roles')
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['user', 'role']
    
    def __str__(self):
        return f"{self.user.username} - {self.role.name}"

class SystemMaintenance(models.Model):
    """System maintenance scheduling"""
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    scheduled_start = models.DateTimeField()
    scheduled_end = models.DateTimeField()
    actual_start = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    is_public_notice = models.BooleanField(default=True)
    public_message = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-scheduled_start']
    
    def __str__(self):
        return f"{self.title} - {self.scheduled_start}"

class DataExport(models.Model):
    """Data export tracking"""
    EXPORT_TYPES = [
        ('users', 'Users'),
        ('bookings', 'Bookings'),
        ('packages', 'Packages'),
        ('places', 'Places'),
        ('feedback', 'Feedback'),
        ('payments', 'Payments'),
        ('all', 'All Data'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    export_id = models.UUIDField(default=uuid.uuid4, unique=True)
    export_type = models.CharField(max_length=20, choices=EXPORT_TYPES)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    file_path = models.CharField(max_length=500, blank=True)
    file_size = models.BigIntegerField(null=True, blank=True)
    filters = models.JSONField(default=dict, blank=True)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.export_type} - {self.status}"

class BulkAction(models.Model):
    """Bulk action tracking"""
    ACTION_TYPES = [
        ('activate', 'Activate'),
        ('deactivate', 'Deactivate'),
        ('delete', 'Delete'),
        ('export', 'Export'),
        ('update_status', 'Update Status'),
        ('send_email', 'Send Email'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    action_id = models.UUIDField(default=uuid.uuid4, unique=True)
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES)
    object_type = models.CharField(max_length=50)
    object_ids = models.JSONField(default=list)
    parameters = models.JSONField(default=dict, blank=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    total_items = models.IntegerField(default=0)
    processed_items = models.IntegerField(default=0)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.action_type} {self.object_type} - {self.status}"

class AdminDashboardWidget(models.Model):
    """Customizable dashboard widgets"""
    WIDGET_TYPES = [
        ('chart', 'Chart'),
        ('table', 'Table'),
        ('metric', 'Metric'),
        ('list', 'List'),
        ('map', 'Map'),
    ]
    
    name = models.CharField(max_length=100)
    widget_type = models.CharField(max_length=20, choices=WIDGET_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    configuration = models.JSONField(default=dict)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
    width = models.IntegerField(default=4)
    height = models.IntegerField(default=3)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['position_y', 'position_x']
    
    def __str__(self):
        return f"{self.title} ({self.widget_type})"

class AdminReport(models.Model):
    """Custom admin reports"""
    REPORT_TYPES = [
        ('financial', 'Financial'),
        ('user_activity', 'User Activity'),
        ('booking_analytics', 'Booking Analytics'),
        ('performance', 'Performance'),
        ('custom', 'Custom'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    query = models.TextField()  # SQL query or configuration
    parameters = models.JSONField(default=dict, blank=True)
    is_scheduled = models.BooleanField(default=False)
    schedule_cron = models.CharField(max_length=100, blank=True)
    is_public = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_run = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.report_type})"
