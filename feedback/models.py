from django.db import models
from accounts.models import User
from places.models import Place
from packages.models import Package

class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ('service', 'Service Quality'),
        ('location', 'Location'),
        ('price', 'Price Value'),
        ('experience', 'Overall Experience'),
        ('food', 'Food Quality'),
        ('accommodation', 'Accommodation'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='feedbacks', blank=True, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='feedbacks', blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='experience')
    comment = models.TextField()
    is_helpful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.place:
            return f"{self.user.username} - {self.place.name} ({self.rating}/5)"
        elif self.package:
            return f"{self.user.username} - {self.package.name} ({self.rating}/5)"
        return f"{self.user.username} - Feedback ({self.rating}/5)"
    
    class Meta:
        ordering = ['-created_at']
        # Ensure user can only give one feedback per place/package
        unique_together = ['user', 'place', 'package']


class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ('service', 'Service Quality'),
        ('location', 'Location'),
        ('price', 'Price Value'),
        ('experience', 'Overall Experience'),
        ('food', 'Food Quality'),
        ('accommodation', 'Accommodation'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='feedbacks', blank=True, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='feedbacks', blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='experience')
    comment = models.TextField()
    is_helpful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.place:
            return f"{self.user.username} - {self.place.name} ({self.rating}/5)"
        elif self.package:
            return f"{self.user.username} - {self.package.name} ({self.rating}/5)"
        return f"{self.user.username} - Feedback ({self.rating}/5)"
    
    class Meta:
        ordering = ['-created_at']
        # Ensure user can only give one feedback per place/package
        unique_together = ['user', 'place', 'package']
