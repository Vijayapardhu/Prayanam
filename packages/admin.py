from django.contrib import admin
from django.utils.html import format_html
from .models import Package, DynamicPricing

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'place', 'base_price', 'duration_days', 'max_capacity', 'is_featured', 'image_preview', 'created_at']
    list_filter = ['place__state', 'place__category', 'is_featured', 'duration_days', 'created_at']
    search_fields = ['name', 'description', 'place__name']
    list_editable = ['is_featured', 'base_price']
    readonly_fields = ['image_preview', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'place', 'is_featured')
        }),
        ('Trip Details', {
            'fields': ('duration_days', 'base_price', 'max_capacity')
        }),
        ('Media', {
            'fields': ('image', 'image_preview'),
            'description': 'Upload an image for this package. Recommended size: 800x600px'
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
        return super().get_queryset(request).select_related('place')

@admin.register(DynamicPricing)
class DynamicPricingAdmin(admin.ModelAdmin):
    list_display = ['package', 'season', 'min_members', 'max_members', 'price_factor', 'created_at']
    list_filter = ['package__place__state', 'season', 'created_at']
    search_fields = ['package__name', 'package__place__name']
    list_editable = ['price_factor', 'min_members', 'max_members']
    
    fieldsets = (
        ('Pricing Information', {
            'fields': ('package', 'season', 'min_members', 'max_members', 'price_factor')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at']