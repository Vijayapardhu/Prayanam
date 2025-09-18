from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Test email functionality'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address to send test email to')

    def handle(self, *args, **options):
        email = options['email']
        
        try:
            self.stdout.write(f"🔄 Attempting to send test email to: {email}")
            
            subject = 'Test Email from Prayanam'
            message = 'This is a test email to verify email functionality is working correctly.'
            
            self.stdout.write(f"📧 Email details:")
            self.stdout.write(f"   Subject: {subject}")
            self.stdout.write(f"   To: {email}")
            self.stdout.write(f"   From: {settings.DEFAULT_FROM_EMAIL}")
            
            result = send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            if result:
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Test email sent successfully to {email}")
                )
                self.stdout.write("Please check your inbox (and spam folder)")
            else:
                self.stdout.write(
                    self.style.ERROR(f"❌ Email sending failed")
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error sending email: {str(e)}")
            )
            self.stdout.write("\nPossible issues:")
            self.stdout.write("1. Gmail app password is incorrect")
            self.stdout.write("2. Gmail account has 2FA enabled but no app password")
            self.stdout.write("3. Gmail account is not configured for SMTP")
            self.stdout.write("4. Network connectivity issues")
            self.stdout.write("5. Gmail account security settings")
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Test email functionality'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address to send test email to')

    def handle(self, *args, **options):
        email = options['email']
        
        try:
            self.stdout.write(f"🔄 Attempting to send test email to: {email}")
            
            subject = 'Test Email from Prayanam'
            message = 'This is a test email to verify email functionality is working correctly.'
            
            self.stdout.write(f"📧 Email details:")
            self.stdout.write(f"   Subject: {subject}")
            self.stdout.write(f"   To: {email}")
            self.stdout.write(f"   From: {settings.DEFAULT_FROM_EMAIL}")
            
            result = send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            if result:
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Test email sent successfully to {email}")
                )
                self.stdout.write("Please check your inbox (and spam folder)")
            else:
                self.stdout.write(
                    self.style.ERROR(f"❌ Email sending failed")
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error sending email: {str(e)}")
            )
            self.stdout.write("\nPossible issues:")
            self.stdout.write("1. Gmail app password is incorrect")
            self.stdout.write("2. Gmail account has 2FA enabled but no app password")
            self.stdout.write("3. Gmail account is not configured for SMTP")
            self.stdout.write("4. Network connectivity issues")
            self.stdout.write("5. Gmail account security settings")
