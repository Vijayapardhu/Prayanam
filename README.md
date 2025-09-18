# 🚀 Prayanam - Smart Travel & Booking Platform

A comprehensive travel booking platform built with Django, featuring live maps, weather forecasting, dynamic pricing, and an admin dashboard.

## ✨ Features

### 🔐 User Management
- **User Registration & Login** with role-based access (Tourist/Admin)
- **Profile Management** with customizable user information
- **Password Reset & Email Verification** via Gmail SMTP

### 🏠 Places & Destinations
- **Place Discovery** with search and filtering capabilities
- **Place Details** with rich information and images
- **Weather Integration** with 5-day forecasts
- **Interactive Maps** for location visualization

### 📦 Travel Packages
- **Package Browsing** with advanced search and filtering
- **Dynamic Pricing** based on seasons and group size
- **Package Details** with comprehensive information
- **Featured Packages** highlighting special offers

### 📅 Booking System
- **Package Booking** with member management
- **Booking Confirmation** via email
- **Booking History** and status tracking
- **Group Bookings** with multiple member support

### 🎯 Events & Activities
- **Event Scheduling** with day-wise itineraries
- **Activity Management** with time slots and locations
- **Food Information** for events that include meals
- **Event Booking** system integration

### 💬 Feedback & Reviews
- **User Feedback System** with ratings and comments
- **Review Management** with category-based organization
- **Helpful Feedback Marking** for better user experience
- **Admin Feedback Management** for quality control

### 👨‍💼 Admin Dashboard
- **Analytics Dashboard** with real-time statistics
- **User Management** with search and filtering
- **Package Management** with CRUD operations
- **Booking Oversight** with status management
- **System Settings** and configuration

## 🛠 Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Authentication**: Django Allauth with JWT
- **Email**: Gmail SMTP
- **Maps**: Google Maps API (mock implementation)
- **Weather**: OpenWeather API (mock implementation)

## 📁 Project Structure

```
prayanam/
├── accounts/                 # User management app
│   ├── models.py            # Custom User model
│   ├── views.py             # Authentication views
│   ├── forms.py             # User forms
│   └── urls.py              # User URLs
├── places/                   # Places & destinations app
│   ├── models.py            # Place model
│   ├── views.py             # Place views
│   └── urls.py              # Place URLs
├── packages/                 # Travel packages app
│   ├── models.py            # Package & DynamicPricing models
│   ├── views.py             # Package views
│   └── urls.py              # Package URLs
├── bookings/                 # Booking system app
│   ├── models.py            # Booking & BookingMember models
│   ├── views.py             # Booking views
│   ├── forms.py             # Booking forms
│   └── urls.py              # Booking URLs
├── events/                   # Events & activities app
│   ├── models.py            # Event model
│   ├── views.py             # Event views
│   ├── forms.py             # Event forms
│   └── urls.py              # Event URLs
├── feedback/                 # Feedback system app
│   ├── models.py            # Feedback model
│   ├── views.py             # Feedback views
│   ├── forms.py             # Feedback forms
│   └── urls.py              # Feedback URLs
├── admin_dashboard/          # Admin dashboard app
│   ├── views.py             # Admin views
│   └── urls.py              # Admin URLs
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   ├── accounts/            # User templates
│   ├── places/              # Place templates
│   ├── packages/            # Package templates
│   └── admin_dashboard/     # Admin templates
├── static/                   # Static files
├── media/                    # User uploaded files
├── travel_platform/          # Django project settings
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
└── manage.py                # Django management script
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 4.2.7
- SQLite (for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd prayanam
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main site: https://prayanam-91p7.onrender.com
   - Admin panel: https://prayanam-91p7.onrender.com/admin
   - Admin dashboard: https://prayanam-91p7.onrender.com/dashboard/

## 🔧 Configuration

### Email Settings
Update the email configuration in `travel_platform/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Database Settings
For production, update the database settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 API Endpoints

### Authentication
- `POST /accounts/login/` - User login
- `POST /accounts/register/` - User registration
- `GET /accounts/profile/` - User profile
- `POST /accounts/logout/` - User logout

### Places
- `GET /places/` - List all places
- `GET /places/{id}/` - Place details
- `GET /places/search/` - Search places
- `GET /places/{id}/weather/` - Place weather

### Packages
- `GET /packages/` - List all packages
- `GET /packages/{id}/` - Package details
- `GET /packages/featured/` - Featured packages
- `POST /packages/calculate-price/` - Price calculation

### Bookings
- `GET /bookings/` - User bookings
- `POST /bookings/create/{package_id}/` - Create booking
- `GET /bookings/{id}/` - Booking details
- `POST /bookings/{id}/cancel/` - Cancel booking

### Events
- `GET /events/` - List events
- `GET /events/package/{id}/` - Package events
- `POST /events/create/` - Create event (admin)

### Feedback
- `GET /feedback/` - List feedback
- `POST /feedback/create/` - Create feedback
- `GET /feedback/{id}/` - Feedback details

### Admin Dashboard
- `GET /dashboard/` - Main admin dashboard
- `GET /dashboard/users/` - User management
- `GET /dashboard/places/` - Place management
- `GET /dashboard/packages/` - Package management
- `GET /dashboard/bookings/` - Booking management
- `GET /dashboard/feedback/` - Feedback management
- `GET /dashboard/analytics/` - Analytics and reports

## 🎨 Customization

### Adding New Features
1. Create a new Django app: `python manage.py startapp your_app_name`
2. Add the app to `INSTALLED_APPS` in settings.py
3. Create models, views, and templates
4. Add URL patterns to the main URLs file

### Styling
The project uses Tailwind CSS for styling. To customize:
1. Modify the base template (`templates/base.html`)
2. Update component templates in their respective directories
3. Add custom CSS classes as needed

### Database Models
To add new models:
1. Create the model in the appropriate app's `models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`

## 🔒 Security Features

- **CSRF Protection** enabled by default
- **Password Hashing** using Django's built-in authentication
- **Input Validation** on all forms
- **Role-based Access Control** for admin functions
- **Secure File Uploads** with validation

## 📱 Responsive Design

The platform is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Configure production database
- [ ] Set up static file serving
- [ ] Configure email settings
- [ ] Set up SSL/HTTPS
- [ ] Configure logging
- [ ] Set up monitoring

### Recommended Hosting
- **Heroku** - Easy deployment with PostgreSQL
- **DigitalOcean** - VPS with full control
- **AWS** - Scalable cloud infrastructure
- **Railway** - Modern deployment platform

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

## 🔮 Future Enhancements

- **Real-time Chat Support**
- **Mobile App Development**
- **Payment Gateway Integration**
- **AI-powered Recommendations**
- **Social Media Integration**
- **Advanced Analytics**
- **Multi-language Support**
- **Offline Booking System**

---

**Built with ❤️ using Django and Tailwind CSS**

A comprehensive travel booking platform built with Django, featuring live maps, weather forecasting, dynamic pricing, and an admin dashboard.

## ✨ Features

### 🔐 User Management
- **User Registration & Login** with role-based access (Tourist/Admin)
- **Profile Management** with customizable user information
- **Password Reset & Email Verification** via Gmail SMTP

### 🏠 Places & Destinations
- **Place Discovery** with search and filtering capabilities
- **Place Details** with rich information and images
- **Weather Integration** with 5-day forecasts
- **Interactive Maps** for location visualization

### 📦 Travel Packages
- **Package Browsing** with advanced search and filtering
- **Dynamic Pricing** based on seasons and group size
- **Package Details** with comprehensive information
- **Featured Packages** highlighting special offers

### 📅 Booking System
- **Package Booking** with member management
- **Booking Confirmation** via email
- **Booking History** and status tracking
- **Group Bookings** with multiple member support

### 🎯 Events & Activities
- **Event Scheduling** with day-wise itineraries
- **Activity Management** with time slots and locations
- **Food Information** for events that include meals
- **Event Booking** system integration

### 💬 Feedback & Reviews
- **User Feedback System** with ratings and comments
- **Review Management** with category-based organization
- **Helpful Feedback Marking** for better user experience
- **Admin Feedback Management** for quality control

### 👨‍💼 Admin Dashboard
- **Analytics Dashboard** with real-time statistics
- **User Management** with search and filtering
- **Package Management** with CRUD operations
- **Booking Oversight** with status management
- **System Settings** and configuration

## 🛠 Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Authentication**: Django Allauth with JWT
- **Email**: Gmail SMTP
- **Maps**: Google Maps API (mock implementation)
- **Weather**: OpenWeather API (mock implementation)

## 📁 Project Structure

```
prayanam/
├── accounts/                 # User management app
│   ├── models.py            # Custom User model
│   ├── views.py             # Authentication views
│   ├── forms.py             # User forms
│   └── urls.py              # User URLs
├── places/                   # Places & destinations app
│   ├── models.py            # Place model
│   ├── views.py             # Place views
│   └── urls.py              # Place URLs
├── packages/                 # Travel packages app
│   ├── models.py            # Package & DynamicPricing models
│   ├── views.py             # Package views
│   └── urls.py              # Package URLs
├── bookings/                 # Booking system app
│   ├── models.py            # Booking & BookingMember models
│   ├── views.py             # Booking views
│   ├── forms.py             # Booking forms
│   └── urls.py              # Booking URLs
├── events/                   # Events & activities app
│   ├── models.py            # Event model
│   ├── views.py             # Event views
│   ├── forms.py             # Event forms
│   └── urls.py              # Event URLs
├── feedback/                 # Feedback system app
│   ├── models.py            # Feedback model
│   ├── views.py             # Feedback views
│   ├── forms.py             # Feedback forms
│   └── urls.py              # Feedback URLs
├── admin_dashboard/          # Admin dashboard app
│   ├── views.py             # Admin views
│   └── urls.py              # Admin URLs
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   ├── accounts/            # User templates
│   ├── places/              # Place templates
│   ├── packages/            # Package templates
│   └── admin_dashboard/     # Admin templates
├── static/                   # Static files
├── media/                    # User uploaded files
├── travel_platform/          # Django project settings
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
└── manage.py                # Django management script
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Django 4.2.7
- SQLite (for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd prayanam
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main site: https://prayanam-91p7.onrender.com
   - Admin panel: https://prayanam-91p7.onrender.com/admin
   - Admin dashboard: https://prayanam-91p7.onrender.com/dashboard/

## 🔧 Configuration

### Email Settings
Update the email configuration in `travel_platform/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Database Settings
For production, update the database settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 API Endpoints

### Authentication
- `POST /accounts/login/` - User login
- `POST /accounts/register/` - User registration
- `GET /accounts/profile/` - User profile
- `POST /accounts/logout/` - User logout

### Places
- `GET /places/` - List all places
- `GET /places/{id}/` - Place details
- `GET /places/search/` - Search places
- `GET /places/{id}/weather/` - Place weather

### Packages
- `GET /packages/` - List all packages
- `GET /packages/{id}/` - Package details
- `GET /packages/featured/` - Featured packages
- `POST /packages/calculate-price/` - Price calculation

### Bookings
- `GET /bookings/` - User bookings
- `POST /bookings/create/{package_id}/` - Create booking
- `GET /bookings/{id}/` - Booking details
- `POST /bookings/{id}/cancel/` - Cancel booking

### Events
- `GET /events/` - List events
- `GET /events/package/{id}/` - Package events
- `POST /events/create/` - Create event (admin)

### Feedback
- `GET /feedback/` - List feedback
- `POST /feedback/create/` - Create feedback
- `GET /feedback/{id}/` - Feedback details

### Admin Dashboard
- `GET /dashboard/` - Main admin dashboard
- `GET /dashboard/users/` - User management
- `GET /dashboard/places/` - Place management
- `GET /dashboard/packages/` - Package management
- `GET /dashboard/bookings/` - Booking management
- `GET /dashboard/feedback/` - Feedback management
- `GET /dashboard/analytics/` - Analytics and reports

## 🎨 Customization

### Adding New Features
1. Create a new Django app: `python manage.py startapp your_app_name`
2. Add the app to `INSTALLED_APPS` in settings.py
3. Create models, views, and templates
4. Add URL patterns to the main URLs file

### Styling
The project uses Tailwind CSS for styling. To customize:
1. Modify the base template (`templates/base.html`)
2. Update component templates in their respective directories
3. Add custom CSS classes as needed

### Database Models
To add new models:
1. Create the model in the appropriate app's `models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`

## 🔒 Security Features

- **CSRF Protection** enabled by default
- **Password Hashing** using Django's built-in authentication
- **Input Validation** on all forms
- **Role-based Access Control** for admin functions
- **Secure File Uploads** with validation

## 📱 Responsive Design

The platform is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Configure production database
- [ ] Set up static file serving
- [ ] Configure email settings
- [ ] Set up SSL/HTTPS
- [ ] Configure logging
- [ ] Set up monitoring

### Recommended Hosting
- **Heroku** - Easy deployment with PostgreSQL
- **DigitalOcean** - VPS with full control
- **AWS** - Scalable cloud infrastructure
- **Railway** - Modern deployment platform

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

## 🔮 Future Enhancements

- **Real-time Chat Support**
- **Mobile App Development**
- **Payment Gateway Integration**
- **AI-powered Recommendations**
- **Social Media Integration**
- **Advanced Analytics**
- **Multi-language Support**
- **Offline Booking System**

---

**Built with ❤️ using Django and Tailwind CSS**
