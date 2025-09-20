from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    AdminSettings, AdminNotification, AdminAuditLog, AdminRole, 
    AdminUserRole, SystemMaintenance, DataExport, BulkAction,
    AdminDashboardWidget, AdminReport
)

@admin.register(AdminSettings)
class AdminSettingsAdmin(admin.ModelAdmin):
    list_display = ['key', 'setting_type', 'value_preview', 'is_active', 'updated_at']
    list_filter = ['setting_type', 'is_active', 'created_at']
    search_fields = ['key', 'description']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    def value_preview(self, obj):
        return obj.value[:50] + '...' if len(obj.value) > 50 else obj.value
    value_preview.short_description = 'Value Preview'

@admin.register(AdminNotification)
class AdminNotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'notification_type', 'priority', 'is_read', 'is_global', 'created_at']
    list_filter = ['notification_type', 'priority', 'is_read', 'is_global', 'created_at']
    search_fields = ['title', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at', 'read_at']
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        for notification in queryset:
            notification.mark_as_read()
        self.message_user(request, f"{queryset.count()} notifications marked as read.")
    mark_as_read.short_description = "Mark selected notifications as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False, read_at=None)
        self.message_user(request, f"{queryset.count()} notifications marked as unread.")
    mark_as_unread.short_description = "Mark selected notifications as unread"

@admin.register(AdminAuditLog)
class AdminAuditLogAdmin(admin.ModelAdmin):
    list_display = ['admin_user', 'action', 'object_type', 'object_name', 'ip_address', 'created_at']
    list_filter = ['action', 'object_type', 'created_at', 'admin_user']
    search_fields = ['admin_user__username', 'object_name', 'description']
    readonly_fields = ['created_at', 'changes', 'ip_address', 'user_agent']
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(AdminRole)
class AdminRoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'permissions_count', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    filter_horizontal = []
    
    def permissions_count(self, obj):
        return len(obj.permissions)
    permissions_count.short_description = 'Permissions Count'

@admin.register(AdminUserRole)
class AdminUserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'assigned_by', 'assigned_at', 'is_active']
    list_filter = ['role', 'is_active', 'assigned_at']
    search_fields = ['user__username', 'role__name', 'assigned_by__username']
    list_editable = ['is_active']
    readonly_fields = ['assigned_at']

@admin.register(SystemMaintenance)
class SystemMaintenanceAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'scheduled_start', 'scheduled_end', 'is_public_notice', 'created_by']
    list_filter = ['status', 'is_public_notice', 'created_at', 'created_by']
    search_fields = ['title', 'description']
    list_editable = ['status', 'is_public_notice']
    readonly_fields = ['created_at']
    date_hierarchy = 'scheduled_start'

@admin.register(DataExport)
class DataExportAdmin(admin.ModelAdmin):
    list_display = ['export_type', 'status', 'requested_by', 'file_size_display', 'created_at']
    list_filter = ['export_type', 'status', 'created_at', 'requested_by']
    search_fields = ['export_id', 'requested_by__username']
    readonly_fields = ['export_id', 'created_at', 'completed_at', 'file_size']
    
    def file_size_display(self, obj):
        if obj.file_size:
            size_mb = obj.file_size / (1024 * 1024)
            return f"{size_mb:.2f} MB"
        return "N/A"
    file_size_display.short_description = 'File Size'

@admin.register(BulkAction)
class BulkActionAdmin(admin.ModelAdmin):
    list_display = ['action_type', 'object_type', 'status', 'progress_display', 'requested_by', 'created_at']
    list_filter = ['action_type', 'object_type', 'status', 'created_at', 'requested_by']
    search_fields = ['action_id', 'requested_by__username']
    readonly_fields = ['action_id', 'created_at', 'completed_at', 'progress', 'total_items', 'processed_items']
    
    def progress_display(self, obj):
        return f"{obj.progress}% ({obj.processed_items}/{obj.total_items})"
    progress_display.short_description = 'Progress'

@admin.register(AdminDashboardWidget)
class AdminDashboardWidgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'widget_type', 'position_display', 'is_active', 'created_by']
    list_filter = ['widget_type', 'is_active', 'created_at', 'created_by']
    search_fields = ['title', 'name', 'description']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    def position_display(self, obj):
        return f"({obj.position_x}, {obj.position_y}) - {obj.width}x{obj.height}"
    position_display.short_description = 'Position & Size'

@admin.register(AdminReport)
class AdminReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'report_type', 'is_scheduled', 'is_public', 'created_by', 'last_run']
    list_filter = ['report_type', 'is_scheduled', 'is_public', 'created_at', 'created_by']
    search_fields = ['name', 'description']
    list_editable = ['is_scheduled', 'is_public']
    readonly_fields = ['created_at', 'updated_at', 'last_run']
    filter_horizontal = []
