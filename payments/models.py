from django.db import models
from django.conf import settings
from bookings.models import Booking
from decimal import Decimal

class Payment(models.Model):
    """Payment records for bookings"""
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('razorpay', 'Razorpay'),
        ('paypal', 'PayPal'),
        ('stripe', 'Stripe'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('card', 'Credit/Debit Card'),
    ]
    
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Payment details
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='INR')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    # Transaction details
    transaction_id = models.CharField(max_length=100, unique=True, blank=True)
    gateway_transaction_id = models.CharField(max_length=100, blank=True)
    gateway_response = models.JSONField(default=dict)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Additional information
    description = models.TextField(blank=True)
    failure_reason = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Payment {self.transaction_id} - ₹{self.amount}"
    
    @property
    def is_successful(self):
        return self.payment_status == 'completed'
    
    @property
    def is_pending(self):
        return self.payment_status in ['pending', 'processing']
    
    @property
    def is_failed(self):
        return self.payment_status in ['failed', 'cancelled']

class PaymentGateway(models.Model):
    """Payment gateway configuration"""
    GATEWAY_CHOICES = [
        ('razorpay', 'Razorpay'),
        ('paypal', 'PayPal'),
        ('stripe', 'Stripe'),
        ('paytm', 'Paytm'),
        ('phonepe', 'PhonePe'),
    ]
    
    name = models.CharField(max_length=50, choices=GATEWAY_CHOICES)
    is_active = models.BooleanField(default=True)
    is_test_mode = models.BooleanField(default=True)
    
    # API credentials
    api_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
    webhook_secret = models.CharField(max_length=255, blank=True)
    
    # Configuration
    supported_currencies = models.JSONField(default=list)
    supported_payment_methods = models.JSONField(default=list)
    processing_fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    processing_fee_fixed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Additional settings
    settings = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Payment Gateways'
    
    def __str__(self):
        return f"{self.name} ({'Test' if self.is_test_mode else 'Live'})"
    
    def calculate_processing_fee(self, amount):
        """Calculate processing fee for a given amount"""
        percentage_fee = amount * (self.processing_fee_percentage / 100)
        return percentage_fee + self.processing_fee_fixed

class Refund(models.Model):
    """Refund records"""
    REFUND_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='refunds')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    refund_status = models.CharField(max_length=20, choices=REFUND_STATUS_CHOICES, default='pending')
    
    # Transaction details
    refund_id = models.CharField(max_length=100, unique=True, blank=True)
    gateway_refund_id = models.CharField(max_length=100, blank=True)
    gateway_response = models.JSONField(default=dict)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    
    # Additional information
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Refund {self.refund_id} - ₹{self.amount}"

class PaymentMethod(models.Model):
    """User's saved payment methods"""
    PAYMENT_TYPE_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('bank_account', 'Bank Account'),
        ('upi', 'UPI ID'),
        ('wallet', 'Digital Wallet'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payment_methods')
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    is_default = models.BooleanField(default=False)
    
    # Card details (encrypted)
    card_last4 = models.CharField(max_length=4, blank=True)
    card_brand = models.CharField(max_length=20, blank=True)
    card_expiry_month = models.IntegerField(null=True, blank=True)
    card_expiry_year = models.IntegerField(null=True, blank=True)
    
    # Bank account details (encrypted)
    bank_name = models.CharField(max_length=100, blank=True)
    account_last4 = models.CharField(max_length=4, blank=True)
    ifsc_code = models.CharField(max_length=11, blank=True)
    
    # UPI details
    upi_id = models.CharField(max_length=100, blank=True)
    
    # Wallet details
    wallet_name = models.CharField(max_length=50, blank=True)
    wallet_number = models.CharField(max_length=50, blank=True)
    
    # Gateway token
    gateway_token = models.CharField(max_length=255, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_default', '-created_at']
    
    def __str__(self):
        if self.payment_type == 'card':
            return f"{self.card_brand} ****{self.card_last4}"
        elif self.payment_type == 'bank_account':
            return f"{self.bank_name} ****{self.account_last4}"
        elif self.payment_type == 'upi':
            return f"UPI: {self.upi_id}"
        elif self.payment_type == 'wallet':
            return f"{self.wallet_name}: {self.wallet_number}"
        return f"{self.get_payment_type_display()}"

class PaymentTransaction(models.Model):
    """Detailed transaction logs"""
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='transactions')
    
    # Transaction details
    action = models.CharField(max_length=50)  # e.g., 'payment_initiated', 'payment_completed'
    status = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Gateway response
    gateway_response = models.JSONField(default=dict)
    error_message = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.action} - {self.payment.transaction_id}"
