pyh#!/usr/bin/env python
"""
Test script to verify email functionality
"""
import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
django.setup()

def test_email():
    """Test email sending functionality"""
    try:
        # Test email
        subject = 'Test Email from Prayanam'
        message = 'This is a test email to verify email functionality.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['your-email@gmail.com']  # Replace with your email
        
        print(f"Sending test email to: {recipient_list[0]}")
        print(f"From: {from_email}")
        print(f"Subject: {subject}")
        
        # Send email
        result = send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        
        if result:
            print("✅ Email sent successfully!")
            print("Please check your inbox (and spam folder)")
        else:
            print("❌ Email sending failed")
            
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        print("\nPossible issues:")
        print("1. Gmail app password is incorrect")
        print("2. Gmail account has 2FA enabled but no app password")
        print("3. Gmail account is not configured for SMTP")
        print("4. Network connectivity issues")

if __name__ == "__main__":
    test_email()
