from django.db import models
from packages.models import Package

class Event(models.Model):
    TIME_SLOT_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]
    
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = models.TextField()
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES)
    location = models.CharField(max_length=200)
    duration_hours = models.DecimalField(max_digits=3, decimal_places=1, default=2.0)
    includes_food = models.BooleanField(default=False)
    food_description = models.TextField(blank=True, null=True)
    day_number = models.IntegerField(default=1)  # Which day of the package
    image = models.ImageField(upload_to='events/', blank=True, null=True, help_text="Event image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title} ({self.time_slot})"
    
    class Meta:
        ordering = ['day_number', 'time_slot']
        unique_together = ['package', 'day_number', 'time_slot']