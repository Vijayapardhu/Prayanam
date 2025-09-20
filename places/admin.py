from django.contrib import admin
from django.utils.html import format_html
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'state', 'category', 'is_featured', 'is_popular', 'rating', 'image_preview', 'created_at']
    list_filter = ['category', 'state', 'season', 'is_featured', 'is_popular', 'created_at']
    search_fields = ['name', 'location', 'description', 'district']
    list_editable = ['is_featured', 'is_popular', 'rating']
    readonly_fields = ['image_preview', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location', 'description', 'category', 'state', 'district', 'is_featured', 'is_popular')
        }),
        ('Location & Coordinates', {
            'fields': ('latitude', 'longitude')
        }),
        ('Media', {
            'fields': ('image', 'image_preview'),
            'description': 'Upload an image for this place. Recommended size: 800x600px'
        }),
        ('Details', {
            'fields': ('season', 'best_time_to_visit', 'average_temperature')
        }),
        ('Visitor Information', {
            'fields': ('entry_fee', 'opening_hours', 'rating', 'total_reviews')
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
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)