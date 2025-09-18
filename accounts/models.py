from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid

class User(AbstractUser):
    ROLE_CHOICES = [
        ('tourist', 'Tourist'),
        ('admin', 'Admin'),
    ]
    
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('te', 'తెలుగు'),
        ('hi', 'हिन्दी'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tourist')
    language_preference = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    @property
    def is_tourist(self):
        return self.role == 'tourist'
    
    @property
    def is_admin(self):
        return self.role == 'admin'


class PasswordResetToken(models.Model):
    """Model to store password reset tokens"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Password reset token for {self.user.username}"
    
    def is_valid(self):
        """Check if the token is valid and not expired"""
        return not self.is_used and timezone.now() < self.expires_at
    
    def mark_as_used(self):
        """Mark the token as used"""
        self.is_used = True
        self.save()
    
    def save(self, *args, **kwargs):
        if not self.expires_at:
            # Token expires in 1 hour
            self.expires_at = timezone.now() + timezone.timedelta(hours=1)
        super().save(*args, **kwargs)
