from django.db import models
from django.conf import settings
from places.models import Place
from packages.models import Package
from datetime import date, time

class Itinerary(models.Model):
    """User's personal itinerary"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Itineraries'
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    @property
    def duration_days(self):
        return (self.end_date - self.start_date).days + 1
    
    @property
    def total_cost(self):
        return sum(item.estimated_cost for item in self.items.all())

class ItineraryItem(models.Model):
    """Individual item in an itinerary"""
    ITEM_TYPES = [
        ('place', 'Place Visit'),
        ('activity', 'Activity'),
        ('transport', 'Transportation'),
        ('accommodation', 'Accommodation'),
        ('meal', 'Meal'),
        ('custom', 'Custom Event'),
    ]
    
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='items')
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, default='place')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    # Location/Place reference
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Date and time
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    
    # Cost and booking
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_booked = models.BooleanField(default=False)
    booking_reference = models.CharField(max_length=100, blank=True)
    
    # Priority and status
    priority = models.IntegerField(default=1, help_text="1=Low, 2=Medium, 3=High")
    is_completed = models.BooleanField(default=False)
    
    # Notes and reminders
    notes = models.TextField(blank=True)
    reminder_time = models.DateTimeField(null=True, blank=True)
    
    # Ordering
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['date', 'start_time', 'order']
    
    def __str__(self):
        return f"{self.title} - {self.date}"
    
    @property
    def duration_hours(self):
        if self.start_time and self.end_time:
            start = self.start_time
            end = self.end_time
            return (end.hour - start.hour) + (end.minute - start.minute) / 60
        return 0

class ItineraryTemplate(models.Model):
    """Pre-defined itinerary templates"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    destination = models.CharField(max_length=200)
    duration_days = models.IntegerField()
    difficulty_level = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
    ], default='moderate')
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_featured', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.duration_days} days"

class TemplateItem(models.Model):
    """Items in itinerary templates"""
    template = models.ForeignKey(ItineraryTemplate, on_delete=models.CASCADE, related_name='items')
    day_number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['day_number', 'order']
    
    def __str__(self):
        return f"Day {self.day_number}: {self.title}"

class TravelRecommendation(models.Model):
    """AI-powered travel recommendations"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    recommendation_type = models.CharField(max_length=50, choices=[
        ('weather', 'Weather-based'),
        ('popularity', 'Popularity-based'),
        ('similar', 'Similar to visited'),
        ('seasonal', 'Seasonal'),
        ('budget', 'Budget-friendly'),
    ])
    confidence_score = models.DecimalField(max_digits=3, decimal_places=2, default=0.5)
    reason = models.TextField()
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-confidence_score', '-created_at']
    
    def __str__(self):
        return f"{self.place.name} - {self.recommendation_type}"

class TravelPreference(models.Model):
    """User travel preferences for recommendations"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Budget preferences
    budget_range = models.CharField(max_length=20, choices=[
        ('budget', 'Budget (< ₹5000)'),
        ('moderate', 'Moderate (₹5000-15000)'),
        ('luxury', 'Luxury (> ₹15000)'),
    ], default='moderate')
    
    # Travel style
    travel_style = models.CharField(max_length=20, choices=[
        ('adventure', 'Adventure'),
        ('relaxation', 'Relaxation'),
        ('culture', 'Cultural'),
        ('nature', 'Nature'),
        ('luxury', 'Luxury'),
        ('budget', 'Budget'),
    ], default='culture')
    
    # Preferred activities
    preferred_activities = models.JSONField(default=list)
    
    # Preferred destinations
    preferred_destinations = models.ManyToManyField(Place, blank=True)
    
    # Travel constraints
    max_travel_days = models.IntegerField(default=7)
    group_size = models.IntegerField(default=2)
    
    # Dietary preferences
    dietary_restrictions = models.JSONField(default=list)
    
    # Accessibility needs
    accessibility_needs = models.JSONField(default=list)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Preferences for {self.user.username}"
