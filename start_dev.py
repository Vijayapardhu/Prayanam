#!/usr/bin/env python
"""
Development startup script for Prayanam Travel Platform
"""
import os
import sys
import subprocess
import time

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🚀 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main function to start the development environment"""
    print("🌟 Welcome to Prayanam Travel Platform!")
    print("=" * 50)
    
    # Check if Django is installed
    try:
        import django
        print("✅ Django is installed")
    except ImportError:
        print("❌ Django is not installed. Installing...")
        if not run_command("pip install django", "Installing Django"):
            print("❌ Failed to install Django. Please install it manually.")
            return
    
    # Check if migrations are needed
    print("\n📋 Checking database migrations...")
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        print("⚠️  Migration creation failed, but continuing...")
    
    if not run_command("python manage.py migrate", "Applying migrations"):
        print("❌ Migration failed. Please check your database configuration.")
        return
    
    # Check if admin user exists
    print("\n👤 Checking admin user...")
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
        django.setup()
        
        from accounts.models import User
        admin_user = User.objects.filter(username='admin').first()
        
        if admin_user:
            print("✅ Admin user exists")
        else:
            print("⚠️  Admin user not found. Creating...")
            if not run_command("python manage.py createsuperuser --username admin --email admin@example.com --noinput", "Creating admin user"):
                print("❌ Failed to create admin user.")
                return
            
            # Set up admin password
            if not run_command("python setup_admin.py", "Setting up admin password"):
                print("❌ Failed to set admin password.")
                return
    except Exception as e:
        print(f"❌ Error checking admin user: {e}")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Quick Start Guide:")
    print("1. Start the development server: python manage.py runserver")
    print("2. Open your browser and go to: https://prayanam-app.onrender.com")
    print("3. Admin panel: https://prayanam-app.onrender.com/admin")
    print("4. Admin dashboard: https://prayanam-app.onrender.com/dashboard/")
    print("\n🔑 Admin Login:")
    print("Username: admin")
    print("Password: admin123")
    
    print("\n🚀 Starting development server...")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Start the development server
    try:
        subprocess.run("python manage.py runserver", shell=True)
    except KeyboardInterrupt:
        print("\n👋 Development server stopped. Goodbye!")

if __name__ == '__main__':
    main()
"""
Development startup script for Prayanam Travel Platform
"""
import os
import sys
import subprocess
import time

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🚀 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main function to start the development environment"""
    print("🌟 Welcome to Prayanam Travel Platform!")
    print("=" * 50)
    
    # Check if Django is installed
    try:
        import django
        print("✅ Django is installed")
    except ImportError:
        print("❌ Django is not installed. Installing...")
        if not run_command("pip install django", "Installing Django"):
            print("❌ Failed to install Django. Please install it manually.")
            return
    
    # Check if migrations are needed
    print("\n📋 Checking database migrations...")
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        print("⚠️  Migration creation failed, but continuing...")
    
    if not run_command("python manage.py migrate", "Applying migrations"):
        print("❌ Migration failed. Please check your database configuration.")
        return
    
    # Check if admin user exists
    print("\n👤 Checking admin user...")
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_platform.settings')
        django.setup()
        
        from accounts.models import User
        admin_user = User.objects.filter(username='admin').first()
        
        if admin_user:
            print("✅ Admin user exists")
        else:
            print("⚠️  Admin user not found. Creating...")
            if not run_command("python manage.py createsuperuser --username admin --email admin@example.com --noinput", "Creating admin user"):
                print("❌ Failed to create admin user.")
                return
            
            # Set up admin password
            if not run_command("python setup_admin.py", "Setting up admin password"):
                print("❌ Failed to set admin password.")
                return
    except Exception as e:
        print(f"❌ Error checking admin user: {e}")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Quick Start Guide:")
    print("1. Start the development server: python manage.py runserver")
    print("2. Open your browser and go to: https://prayanam-app.onrender.com")
    print("3. Admin panel: https://prayanam-app.onrender.com/admin")
    print("4. Admin dashboard: https://prayanam-app.onrender.com/dashboard/")
    print("\n🔑 Admin Login:")
    print("Username: admin")
    print("Password: admin123")
    
    print("\n🚀 Starting development server...")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Start the development server
    try:
        subprocess.run("python manage.py runserver", shell=True)
    except KeyboardInterrupt:
        print("\n👋 Development server stopped. Goodbye!")

if __name__ == '__main__':
    main()
