from django.contrib import admin
from django.utils.html import format_html
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'package', 'day_number', 'time_slot', 'location', 'duration_hours', 'includes_food', 'image_preview', 'created_at']
    list_filter = ['package__place__state', 'time_slot', 'day_number', 'includes_food', 'created_at']
    search_fields = ['title', 'description', 'location', 'package__name', 'package__place__name']
    list_editable = ['includes_food', 'duration_hours']
    readonly_fields = ['image_preview', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('package', 'title', 'description', 'day_number', 'time_slot')
        }),
        ('Event Details', {
            'fields': ('location', 'duration_hours', 'includes_food', 'food_description')
        }),
        ('Media', {
            'fields': ('image', 'image_preview'),
            'description': 'Upload an image for this event. Recommended size: 800x600px'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="75" style="border-radius: 5px;" />',
                obj.image.url
            )
        return "No image"
    image_preview.short_description = "Image Preview"
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('package', 'package__place')
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)