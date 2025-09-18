#!/bin/bash

# Build script for Prayanam Travel Platform
echo "🚀 Building Prayanam Travel Platform..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Create superuser if needed
echo "👤 Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

# Create sample data if needed
echo "📊 Creating sample data..."
python manage.py shell -c "
from create_sample_data import create_sample_data
create_sample_data()
print('Sample data created successfully')
"

echo "✅ Build completed successfully!"
echo "🌐 Your app is ready at: https://prayanam-91p7.onrender.com"
