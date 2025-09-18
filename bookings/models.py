from django.db import models
from accounts.models import User
from packages.models import Package

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    FOOD_CHOICES = [
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('mixed', 'Mixed (Veg & Non-Veg)'),
        ('none', 'No Food Required'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    from_date = models.DateField(help_text="Start date of the trip", null=True, blank=True)
    to_date = models.DateField(help_text="End date of the trip", null=True, blank=True)
    members_count = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    food_preference = models.CharField(max_length=20, choices=FOOD_CHOICES, default='mixed')
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.package.name} ({self.from_date} to {self.to_date})"
    
    @property
    def duration_days(self):
        """Calculate the duration of the trip in days"""
        if self.from_date and self.to_date:
            return (self.to_date - self.from_date).days + 1
        return self.package.duration_days
    
    class Meta:
        ordering = ['-created_at']

class BookingMember(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    food_preference = models.CharField(max_length=20, choices=Booking.FOOD_CHOICES, default='mixed')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.booking.package.name}"
