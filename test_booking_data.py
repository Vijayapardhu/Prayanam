#!/usr/bin/env python
"""
Test script to check booking data structure
"""
import os
import django
from django.contrib.auth import get_user_model
from bookings.models import Booking
from payments.models import Payment

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

def test_booking_data():
    """Test booking data structure"""
    User = get_user_model()
    
    # Get the first user
    try:
        user = User.objects.first()
        if not user:
            print("❌ No users found in database")
            return
            
        print(f"👤 Testing with user: {user.username} ({user.email})")
        
        # Get user's bookings
        bookings = Booking.objects.filter(user=user)
        print(f"📋 Found {bookings.count()} bookings for user")
        
        for booking in bookings:
            print(f"\n🔍 Booking ID: {booking.id}")
            print(f"   Package: {booking.package.name if booking.package else 'None'}")
            print(f"   From Date: {booking.from_date}")
            print(f"   To Date: {booking.to_date}")
            print(f"   Members Count: {booking.members_count}")
            print(f"   Total Price: ₹{booking.total_price}")
            print(f"   Status: {booking.status}")
            print(f"   Food Preference: {booking.food_preference}")
            
            # Check related payments
            payments = Payment.objects.filter(booking=booking)
            print(f"   Payments: {payments.count()}")
            for payment in payments:
                print(f"     - Payment ID: {payment.id}, Amount: ₹{payment.amount}, Status: {payment.payment_status}")
        
        # Get user's payments
        payments = Payment.objects.filter(user=user)
        print(f"\n💰 Found {payments.count()} payments for user")
        
        for payment in payments:
            print(f"\n💳 Payment ID: {payment.id}")
            print(f"   Amount: ₹{payment.amount}")
            print(f"   Method: {payment.payment_method}")
            print(f"   Status: {payment.payment_status}")
            print(f"   Booking ID: {payment.booking.id if payment.booking else 'None'}")
            print(f"   Transaction ID: {payment.transaction_id}")
            print(f"   Completed At: {payment.completed_at}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_booking_data()
