from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from bookings.models import Booking
from payments.models import Payment

class Command(BaseCommand):
    help = 'Test booking data structure'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get the first user
        try:
            user = User.objects.first()
            if not user:
                self.stdout.write(
                    self.style.ERROR("❌ No users found in database")
                )
                return
                
            self.stdout.write(f"👤 Testing with user: {user.username} ({user.email})")
            
            # Get user's bookings
            bookings = Booking.objects.filter(user=user)
            self.stdout.write(f"📋 Found {bookings.count()} bookings for user")
            
            for booking in bookings:
                self.stdout.write(f"\n🔍 Booking ID: {booking.id}")
                self.stdout.write(f"   Package: {booking.package.name if booking.package else 'None'}")
                self.stdout.write(f"   From Date: {booking.from_date}")
                self.stdout.write(f"   To Date: {booking.to_date}")
                self.stdout.write(f"   Members Count: {booking.members_count}")
                self.stdout.write(f"   Total Price: ₹{booking.total_price}")
                self.stdout.write(f"   Status: {booking.status}")
                self.stdout.write(f"   Food Preference: {booking.food_preference}")
                
                # Check related payments
                payments = Payment.objects.filter(booking=booking)
                self.stdout.write(f"   Payments: {payments.count()}")
                for payment in payments:
                    self.stdout.write(f"     - Payment ID: {payment.id}, Amount: ₹{payment.amount}, Status: {payment.payment_status}")
            
            # Get user's payments
            payments = Payment.objects.filter(user=user)
            self.stdout.write(f"\n💰 Found {payments.count()} payments for user")
            
            for payment in payments:
                self.stdout.write(f"\n💳 Payment ID: {payment.id}")
                self.stdout.write(f"   Amount: ₹{payment.amount}")
                self.stdout.write(f"   Method: {payment.payment_method}")
                self.stdout.write(f"   Status: {payment.payment_status}")
                self.stdout.write(f"   Booking ID: {payment.booking.id if payment.booking else 'None'}")
                self.stdout.write(f"   Transaction ID: {payment.transaction_id}")
                self.stdout.write(f"   Completed At: {payment.completed_at}")
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error: {e}")
            )
from django.contrib.auth import get_user_model
from bookings.models import Booking
from payments.models import Payment

class Command(BaseCommand):
    help = 'Test booking data structure'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get the first user
        try:
            user = User.objects.first()
            if not user:
                self.stdout.write(
                    self.style.ERROR("❌ No users found in database")
                )
                return
                
            self.stdout.write(f"👤 Testing with user: {user.username} ({user.email})")
            
            # Get user's bookings
            bookings = Booking.objects.filter(user=user)
            self.stdout.write(f"📋 Found {bookings.count()} bookings for user")
            
            for booking in bookings:
                self.stdout.write(f"\n🔍 Booking ID: {booking.id}")
                self.stdout.write(f"   Package: {booking.package.name if booking.package else 'None'}")
                self.stdout.write(f"   From Date: {booking.from_date}")
                self.stdout.write(f"   To Date: {booking.to_date}")
                self.stdout.write(f"   Members Count: {booking.members_count}")
                self.stdout.write(f"   Total Price: ₹{booking.total_price}")
                self.stdout.write(f"   Status: {booking.status}")
                self.stdout.write(f"   Food Preference: {booking.food_preference}")
                
                # Check related payments
                payments = Payment.objects.filter(booking=booking)
                self.stdout.write(f"   Payments: {payments.count()}")
                for payment in payments:
                    self.stdout.write(f"     - Payment ID: {payment.id}, Amount: ₹{payment.amount}, Status: {payment.payment_status}")
            
            # Get user's payments
            payments = Payment.objects.filter(user=user)
            self.stdout.write(f"\n💰 Found {payments.count()} payments for user")
            
            for payment in payments:
                self.stdout.write(f"\n💳 Payment ID: {payment.id}")
                self.stdout.write(f"   Amount: ₹{payment.amount}")
                self.stdout.write(f"   Method: {payment.payment_method}")
                self.stdout.write(f"   Status: {payment.payment_status}")
                self.stdout.write(f"   Booking ID: {payment.booking.id if payment.booking else 'None'}")
                self.stdout.write(f"   Transaction ID: {payment.transaction_id}")
                self.stdout.write(f"   Completed At: {payment.completed_at}")
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error: {e}")
            )
