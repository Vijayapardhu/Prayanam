from django.contrib import admin
from .models import Package
from places.models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'state', 'category', 'is_featured', 'is_popular', 'rating', 'created_at']
    list_filter = ['category', 'state', 'season', 'is_featured', 'is_popular', 'created_at']
    search_fields = ['name', 'location', 'description', 'district']
    list_editable = ['is_featured', 'is_popular', 'rating']
    prepopulated_fields = {'name': ('name',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location', 'description', 'category', 'state', 'district', 'is_featured', 'is_popular')
        }),
        ('Location & Coordinates', {
            'fields': ('latitude', 'longitude')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Details', {
            'fields': ('season', 'best_time_to_visit', 'average_temperature')
        }),
        ('Visitor Information', {
            'fields': ('entry_fee', 'opening_hours', 'rating', 'total_reviews')
        }),
    )

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'place', 'base_price', 'duration_days', 'max_capacity', 'is_featured', 'created_at']
    list_filter = ['place__state', 'place__category', 'is_featured', 'duration_days', 'created_at']
    search_fields = ['name', 'description', 'place__name']
    list_editable = ['is_featured', 'base_price']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'place', 'is_featured')
        }),
        ('Trip Details', {
            'fields': ('duration_days', 'base_price', 'max_capacity')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('place')
