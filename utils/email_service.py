from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import get_user_model
from bookings.models import Booking
from payments.models import Payment
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class EmailService:
    """Service class for sending various types of emails"""
    
    @staticmethod
    def send_welcome_email(user):
        """Send welcome email to new user"""
        try:
            subject = 'Welcome to Prayanam - Your Smart Travel Platform'
            html_message = render_to_string('emails/welcome.html', {
                'user': user,
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Welcome email sent to {user.email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send welcome email to {user.email}: {str(e)}")
            return False
    
    @staticmethod
    def send_login_alert(user, request):
        """Send login alert email to user"""
        try:
            # Get client IP and user agent
            client_ip = request.META.get('REMOTE_ADDR', 'Unknown')
            user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
            
            subject = 'New Login Alert - Prayanam'
            html_message = render_to_string('emails/login_alert.html', {
                'user': user,
                'client_ip': client_ip,
                'user_agent': user_agent,
                'login_time': request.session.get('login_time'),
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Login alert email sent to {user.email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send login alert email to {user.email}: {str(e)}")
            return False
    
    @staticmethod
    def send_booking_confirmation(booking):
        """Send booking confirmation email"""
        try:
            subject = f'Booking Confirmation - {booking.package.name}'
            html_message = render_to_string('emails/booking_confirmation.html', {
                'booking': booking,
                'user': booking.user,
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Booking confirmation email sent to {booking.user.email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send booking confirmation email: {str(e)}")
            return False
    
    @staticmethod
    def send_payment_confirmation(payment):
        """Send payment confirmation email"""
        try:
            subject = f'Payment Confirmation - ₹{payment.amount}'
            html_message = render_to_string('emails/payment_confirmation.html', {
                'payment': payment,
                'user': payment.user,
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[payment.user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Payment confirmation email sent to {payment.user.email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send payment confirmation email: {str(e)}")
            return False
    
    @staticmethod
    def send_booking_reminder(booking):
        """Send booking reminder email"""
        try:
            subject = f'Upcoming Trip Reminder - {booking.package.name}'
            html_message = render_to_string('emails/booking_reminder.html', {
                'booking': booking,
                'user': booking.user,
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Booking reminder email sent to {booking.user.email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send booking reminder email: {str(e)}")
            return False
    
    @staticmethod
    def send_otp_email(email, otp, booking, payment_method_type=None):
        """Send OTP email for payment verification"""
        try:
            print(f"🔄 Attempting to send OTP email to: {email}")
            
            subject = 'Payment OTP - Prayanam'
            
            # Get payment method display name
            payment_method_names = {
                'test_credit_card': 'Credit Card',
                'test_debit_card': 'Debit Card', 
                'test_upi': 'UPI Payment',
                'test_net_banking': 'Net Banking',
                'test_wallet': 'Digital Wallet'
            }
            payment_method_name = payment_method_names.get(payment_method_type, 'Payment Method')
            
            html_message = render_to_string('emails/otp_email.html', {
                'otp': otp,
                'booking': booking,
                'payment_method_name': payment_method_name,
                'amount': booking.total_price,
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)

            print(f"📧 Email details:")
            print(f"   Subject: {subject}")
            print(f"   To: {email}")
            print(f"   From: {settings.DEFAULT_FROM_EMAIL}")
            print(f"   OTP: {otp}")

            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                html_message=html_message,
                fail_silently=False,
            )
            
            print(f"✅ OTP email sent successfully to {email}")
            logger.info(f"OTP email sent to {email}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to send OTP email to {email}: {str(e)}")
            logger.error(f"Failed to send OTP email to {email}: {str(e)}")
            return False
    
    @staticmethod
    def send_password_reset_email(user, reset_url):
        """Send password reset email"""
        try:
            subject = 'Password Reset Request - Prayanam'
            html_message = render_to_string('emails/password_reset.html', {
                'user': user,
                'reset_url': reset_url,
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Password reset email sent to {user.email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send password reset email: {str(e)}")
            return False
    
    @staticmethod
    def send_admin_notification(subject, message, admin_emails=None):
        """Send notification to admin users"""
        try:
            if admin_emails is None:
                admin_emails = User.objects.filter(is_admin=True).values_list('email', flat=True)
            
            html_message = render_to_string('emails/admin_notification.html', {
                'subject': subject,
                'message': message,
                'site_name': 'Prayanam'
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=f'Admin Notification: {subject}',
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=list(admin_emails),
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Admin notification sent: {subject}")
            return True
        except Exception as e:
            logger.error(f"Failed to send admin notification: {str(e)}")
            return False
    
    @staticmethod
    def send_custom_email(to_email, subject, template_name, context):
        """Send custom email using a template"""
        try:
            html_message = render_to_string(f'emails/{template_name}.html', context)
            plain_message = strip_tags(html_message)
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[to_email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Custom email sent to {to_email}: {subject}")
            return True
        except Exception as e:
            logger.error(f"Failed to send custom email: {str(e)}")
            return False
