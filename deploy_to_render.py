#!/usr/bin/env python3
"""
Deployment script for Prayanam Admin Panel on Render
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main deployment function"""
    print("🚀 Starting deployment preparation for Prayanam Admin Panel...")
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Step 1: Install dependencies
    if not run_command('pip install -r requirements.txt', 'Installing dependencies'):
        sys.exit(1)
    
    # Step 2: Run migrations
    if not run_command('python manage.py makemigrations', 'Creating migrations'):
        sys.exit(1)
    
    if not run_command('python manage.py migrate', 'Running migrations'):
        sys.exit(1)
    
    # Step 3: Collect static files
    if not run_command('python manage.py collectstatic --noinput', 'Collecting static files'):
        sys.exit(1)
    
    # Step 4: Create superuser (optional)
    print("\n📝 Creating admin user...")
    try:
        from django.core.management import execute_from_command_line
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
        
        # Check if admin user already exists
        import django
        django.setup()
        from accounts.models import User
        
        if not User.objects.filter(role='admin').exists():
            print("Creating admin user...")
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@prayanam.com',
                password='admin123',
                role='admin',
                first_name='Admin',
                last_name='User'
            )
            print(f"✅ Admin user created: {admin_user.username}")
        else:
            print("✅ Admin user already exists")
            
    except Exception as e:
        print(f"⚠️  Warning: Could not create admin user: {e}")
        print("You can create one manually after deployment")
    
    # Step 5: Setup admin data
    if not run_command('python setup_admin_data.py', 'Setting up admin data'):
        print("⚠️  Warning: Could not setup admin data. You may need to do this manually.")
    
    print("\n🎉 Deployment preparation completed!")
    print("\n📋 Next steps:")
    print("1. Push your code to GitHub")
    print("2. Connect your GitHub repository to Render")
    print("3. Use the following settings in Render:")
    print("   - Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate")
    print("   - Start Command: gunicorn travel_platform.wsgi:application")
    print("   - Environment: Python")
    print("4. Set the following environment variables in Render:")
    print("   - DEBUG=False")
    print("   - SECRET_KEY=<generate a secure secret key>")
    print("   - ALLOWED_HOSTS=your-app-name.onrender.com")
    print("   - DATABASE_URL=<from your PostgreSQL service>")
    print("   - EMAIL_HOST_USER=<your email>")
    print("   - EMAIL_HOST_PASSWORD=<your email password>")
    print("\n🌐 Your admin panel will be available at: https://your-app-name.onrender.com/admin-dashboard/")
    print("👤 Login with: admin / admin123")

if __name__ == '__main__':
    main()
