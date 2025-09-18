# 🚀 Prayanam Travel Platform - Deployment Guide

## 🌐 Production Domain
**Live URL**: https://prayanam-91p7.onrender.com

## 📋 Pre-deployment Checklist

### ✅ Admin Features Added
- **Package Management**: Admin can add, edit, and manage travel packages
- **Destination Management**: Admin can add, edit, and manage destinations
- **User Management**: Admin can manage users and their bookings
- **Booking Management**: Admin can view and manage all bookings
- **Payment Management**: Admin can track payments and transactions
- **Analytics Dashboard**: Admin can view platform analytics

### ✅ URL Updates Completed
- All hardcoded URLs updated to: `https://prayanam-91p7.onrender.com`
- Email templates updated with new domain
- Meta tags and SEO optimized for production
- CSRF trusted origins configured

### ✅ Email System Configured
- Gmail SMTP configured with app password
- OTP emails for payment verification
- Welcome emails for new users
- Login alert emails for security
- Payment confirmation emails

## 🛠️ Deployment Steps

### 1. Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DJANGO_SETTINGS_MODULE=travel_platform.settings_production
export DEBUG=False
```

### 2. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Create sample data (optional)
python manage.py shell -c "from create_sample_data import create_sample_data; create_sample_data()"
```

### 3. Static Files
```bash
# Collect static files
python manage.py collectstatic --noinput
```

### 4. Production Server
```bash
# Using Gunicorn
gunicorn travel_platform.wsgi:application --bind 0.0.0.0:8000

# Or using Django development server (not recommended for production)
python manage.py runserver 0.0.0.0:8000
```

## 🔧 Admin Panel Access

### Admin Login
- **URL**: https://prayanam-91p7.onrender.com/admin/
- **Username**: admin
- **Password**: admin123

### Admin Features Available
1. **Packages Management**
   - Add new travel packages
   - Edit existing packages
   - Set pricing and inclusions
   - Upload package images

2. **Destinations Management**
   - Add new destinations
   - Set location coordinates
   - Add attractions and details
   - Upload destination images

3. **User Management**
   - View all registered users
   - Manage user permissions
   - View user bookings

4. **Booking Management**
   - View all bookings
   - Update booking status
   - Manage booking details

5. **Payment Tracking**
   - View payment transactions
   - Track payment status
   - Manage refunds

## 📧 Email Configuration

### Gmail SMTP Settings
- **Host**: smtp.gmail.com
- **Port**: 587
- **Username**: team.prayanam@gmail.com
- **Password**: App password (configured)

### Email Types
1. **Welcome Email**: Sent to new users
2. **OTP Email**: Sent for payment verification
3. **Login Alert**: Sent for new login detection
4. **Payment Confirmation**: Sent after successful payment

## 🔒 Security Features

### Production Security
- HTTPS enforced
- CSRF protection enabled
- XSS protection enabled
- HSTS headers configured
- Secure cookies enabled

### Admin Security
- Admin panel protected
- User authentication required
- Session timeout configured
- Login alerts enabled

## 📊 Monitoring & Analytics

### Admin Dashboard Features
- User registration analytics
- Booking statistics
- Revenue tracking
- Popular destinations
- Payment success rates

### Logging
- Application logs stored in `/logs/django.log`
- Error tracking enabled
- Performance monitoring

## 🚀 Quick Start Commands

```bash
# Clone repository
git clone <repository-url>
cd prayanam

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Run server
python manage.py runserver

# Or use production settings
export DJANGO_SETTINGS_MODULE=travel_platform.settings_production
gunicorn travel_platform.wsgi:application --bind 0.0.0.0:8000
```

## 📞 Support

### Contact Information
- **Website**: https://prayanam-91p7.onrender.com
- **Email**: team.prayanam@gmail.com
- **Phone**: +91 1800-123-4567

### Admin Support
- Admin panel: https://prayanam-91p7.onrender.com/admin/
- Dashboard: https://prayanam-91p7.onrender.com/admin-dashboard/

## 🔄 Updates & Maintenance

### Regular Tasks
1. **Database Backups**: Regular backups of SQLite database
2. **Log Monitoring**: Check application logs for errors
3. **Email Monitoring**: Ensure email delivery is working
4. **Security Updates**: Keep dependencies updated

### Adding New Features
1. Create new models in appropriate apps
2. Run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Update admin.py to register new models
4. Test thoroughly before deployment

---

**🎉 Your Prayanam Travel Platform is now ready for production!**

## 🌐 Production Domain
**Live URL**: https://prayanam-91p7.onrender.com

## 📋 Pre-deployment Checklist

### ✅ Admin Features Added
- **Package Management**: Admin can add, edit, and manage travel packages
- **Destination Management**: Admin can add, edit, and manage destinations
- **User Management**: Admin can manage users and their bookings
- **Booking Management**: Admin can view and manage all bookings
- **Payment Management**: Admin can track payments and transactions
- **Analytics Dashboard**: Admin can view platform analytics

### ✅ URL Updates Completed
- All hardcoded URLs updated to: `https://prayanam-91p7.onrender.com`
- Email templates updated with new domain
- Meta tags and SEO optimized for production
- CSRF trusted origins configured

### ✅ Email System Configured
- Gmail SMTP configured with app password
- OTP emails for payment verification
- Welcome emails for new users
- Login alert emails for security
- Payment confirmation emails

## 🛠️ Deployment Steps

### 1. Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DJANGO_SETTINGS_MODULE=travel_platform.settings_production
export DEBUG=False
```

### 2. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Create sample data (optional)
python manage.py shell -c "from create_sample_data import create_sample_data; create_sample_data()"
```

### 3. Static Files
```bash
# Collect static files
python manage.py collectstatic --noinput
```

### 4. Production Server
```bash
# Using Gunicorn
gunicorn travel_platform.wsgi:application --bind 0.0.0.0:8000

# Or using Django development server (not recommended for production)
python manage.py runserver 0.0.0.0:8000
```

## 🔧 Admin Panel Access

### Admin Login
- **URL**: https://prayanam-91p7.onrender.com/admin/
- **Username**: admin
- **Password**: admin123

### Admin Features Available
1. **Packages Management**
   - Add new travel packages
   - Edit existing packages
   - Set pricing and inclusions
   - Upload package images

2. **Destinations Management**
   - Add new destinations
   - Set location coordinates
   - Add attractions and details
   - Upload destination images

3. **User Management**
   - View all registered users
   - Manage user permissions
   - View user bookings

4. **Booking Management**
   - View all bookings
   - Update booking status
   - Manage booking details

5. **Payment Tracking**
   - View payment transactions
   - Track payment status
   - Manage refunds

## 📧 Email Configuration

### Gmail SMTP Settings
- **Host**: smtp.gmail.com
- **Port**: 587
- **Username**: team.prayanam@gmail.com
- **Password**: App password (configured)

### Email Types
1. **Welcome Email**: Sent to new users
2. **OTP Email**: Sent for payment verification
3. **Login Alert**: Sent for new login detection
4. **Payment Confirmation**: Sent after successful payment

## 🔒 Security Features

### Production Security
- HTTPS enforced
- CSRF protection enabled
- XSS protection enabled
- HSTS headers configured
- Secure cookies enabled

### Admin Security
- Admin panel protected
- User authentication required
- Session timeout configured
- Login alerts enabled

## 📊 Monitoring & Analytics

### Admin Dashboard Features
- User registration analytics
- Booking statistics
- Revenue tracking
- Popular destinations
- Payment success rates

### Logging
- Application logs stored in `/logs/django.log`
- Error tracking enabled
- Performance monitoring

## 🚀 Quick Start Commands

```bash
# Clone repository
git clone <repository-url>
cd prayanam

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Run server
python manage.py runserver

# Or use production settings
export DJANGO_SETTINGS_MODULE=travel_platform.settings_production
gunicorn travel_platform.wsgi:application --bind 0.0.0.0:8000
```

## 📞 Support

### Contact Information
- **Website**: https://prayanam-91p7.onrender.com
- **Email**: team.prayanam@gmail.com
- **Phone**: +91 1800-123-4567

### Admin Support
- Admin panel: https://prayanam-91p7.onrender.com/admin/
- Dashboard: https://prayanam-91p7.onrender.com/admin-dashboard/

## 🔄 Updates & Maintenance

### Regular Tasks
1. **Database Backups**: Regular backups of SQLite database
2. **Log Monitoring**: Check application logs for errors
3. **Email Monitoring**: Ensure email delivery is working
4. **Security Updates**: Keep dependencies updated

### Adding New Features
1. Create new models in appropriate apps
2. Run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Update admin.py to register new models
4. Test thoroughly before deployment

---

**🎉 Your Prayanam Travel Platform is now ready for production!**
