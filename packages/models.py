from django.db import models
from decimal import Decimal
from places.models import Place

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='packages')
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(default=1)
    max_capacity = models.IntegerField(default=10)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def calculate_price(self, season, members_count):
        """Calculate dynamic price based on season and group size"""
        season_factors = {
            'spring': Decimal('1.1'),
            'summer': Decimal('1.3'),
            'autumn': Decimal('1.0'),
            'winter': Decimal('0.8'),
        }
        
        member_factors = {
            1: Decimal('1.0'),
            2: Decimal('0.95'),
            3: Decimal('0.90'),
            4: Decimal('0.85'),
            5: Decimal('0.80'),
        }
        
        season_factor = season_factors.get(season, Decimal('1.0'))
        member_factor = member_factors.get(min(members_count, 5), Decimal('0.75'))
        
        return self.base_price * season_factor * member_factor
    
    class Meta:
        ordering = ['-created_at']

class DynamicPricing(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='pricing_rules')
    season = models.CharField(max_length=10, choices=Place.SEASON_CHOICES)
    min_members = models.IntegerField(default=1)
    max_members = models.IntegerField(default=10)
    price_factor = models.DecimalField(max_digits=4, decimal_places=2, default=1.00)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.package.name} - {self.season} ({self.min_members}-{self.max_members} members)"
    
    class Meta:
        unique_together = ['package', 'season', 'min_members', 'max_members']

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='packages')
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(default=1)
    max_capacity = models.IntegerField(default=10)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def calculate_price(self, season, members_count):
        """Calculate dynamic price based on season and group size"""
        season_factors = {
            'spring': Decimal('1.1'),
            'summer': Decimal('1.3'),
            'autumn': Decimal('1.0'),
            'winter': Decimal('0.8'),
        }
        
        member_factors = {
            1: Decimal('1.0'),
            2: Decimal('0.95'),
            3: Decimal('0.90'),
            4: Decimal('0.85'),
            5: Decimal('0.80'),
        }
        
        season_factor = season_factors.get(season, Decimal('1.0'))
        member_factor = member_factors.get(min(members_count, 5), Decimal('0.75'))
        
        return self.base_price * season_factor * member_factor
    
    class Meta:
        ordering = ['-created_at']

class DynamicPricing(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='pricing_rules')
    season = models.CharField(max_length=10, choices=Place.SEASON_CHOICES)
    min_members = models.IntegerField(default=1)
    max_members = models.IntegerField(default=10)
    price_factor = models.DecimalField(max_digits=4, decimal_places=2, default=1.00)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.package.name} - {self.season} ({self.min_members}-{self.max_members} members)"
    
    class Meta:
        unique_together = ['package', 'season', 'min_members', 'max_members']
