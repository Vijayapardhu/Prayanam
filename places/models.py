from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Place(models.Model):
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('autumn', 'Autumn'),
        ('winter', 'Winter'),
    ]
    
    CATEGORY_CHOICES = [
        ('heritage', 'Heritage'),
        ('beaches', 'Beaches'),
        ('temples', 'Temples'),
        ('adventure', 'Adventure'),
        ('hills', 'Hills'),
        ('wildlife', 'Wildlife'),
        ('cultural', 'Cultural'),
    ]
    
    STATE_CHOICES = [
        ('ap', 'Andhra Pradesh'),
        ('telangana', 'Telangana'),
    ]
    
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='places/', null=True, blank=True)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, default='summer')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='cultural')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='ap')
    district = models.CharField(max_length=100, blank=True)
    
    # Map coordinates
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Weather and climate
    average_temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    best_time_to_visit = models.CharField(max_length=100, blank=True)
    
    # Entry fees and timings
    entry_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    opening_hours = models.CharField(max_length=100, default="6:00 AM - 6:00 PM")
    
    # Popularity and ratings
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    total_reviews = models.IntegerField(default=0)
    
    # Additional information
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', '-rating', 'name']
    
    def __str__(self):
        return f"{self.name}, {self.location}"
    
    @property
    def coordinates(self):
        """Return coordinates as a tuple for map integration"""
        if self.latitude and self.longitude:
            return (float(self.latitude), float(self.longitude))
        return None
    
    @property
    def map_url(self):
        """Generate Google Maps URL"""
        if self.coordinates:
            lat, lng = self.coordinates
            return f"https://www.google.com/maps?q={lat},{lng}"
        return f"https://www.google.com/maps/search/{self.name}+{self.location}"
    
    def get_weather_data(self):
        """Get weather data for this location (to be implemented with API)"""
        # This would integrate with OpenWeatherMap API
        return {
            'temperature': self.average_temperature,
            'condition': 'Sunny',
            'humidity': 65,
            'wind_speed': 10
        }
