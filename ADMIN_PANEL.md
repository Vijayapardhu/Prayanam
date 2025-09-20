# 🛡️ Admin Panel Documentation

## Overview

The Prayanam Admin Panel is a comprehensive management system that provides administrators with complete control over the travel booking platform. It features a modern, responsive interface with advanced analytics, user management, content management, and system administration capabilities.

## 🚀 Features

### 📊 Dashboard & Analytics
- **Real-time Statistics**: Live updates of key metrics including users, bookings, revenue, and packages
- **Interactive Charts**: Visual representation of data trends using Chart.js
- **Customizable Widgets**: Drag-and-drop dashboard widgets for personalized views
- **Performance Metrics**: System performance monitoring and reporting

### 👥 User Management
- **User CRUD Operations**: Create, read, update, and delete user accounts
- **Role-based Access Control**: Assign different permission levels to users
- **User Analytics**: Track user activity, registration trends, and engagement
- **Bulk User Operations**: Perform actions on multiple users simultaneously

### 🏞️ Content Management
- **Places Management**: Add, edit, and manage tourist destinations
- **Package Management**: Create and manage travel packages
- **Booking Management**: Oversee all bookings and their status
- **Feedback Management**: Moderate user feedback and reviews

### ⚙️ System Administration
- **Settings Management**: Configure system-wide settings
- **Notification System**: Send and manage admin notifications
- **Audit Logging**: Track all admin actions for security and compliance
- **Bulk Operations**: Perform mass operations on various data types

### 📈 Data Management
- **Data Export**: Export data in CSV format with filtering options
- **Data Import**: Import data from external sources
- **Backup Management**: Schedule and manage system backups
- **Report Generation**: Generate custom reports and analytics

## 🏗️ Architecture

### Models
- **AdminSettings**: System configuration settings
- **AdminNotification**: Notification management
- **AdminAuditLog**: Action tracking and logging
- **AdminRole**: Role-based permissions
- **SystemMaintenance**: Maintenance scheduling
- **DataExport**: Export tracking
- **BulkAction**: Bulk operation management
- **AdminDashboardWidget**: Customizable dashboard widgets

### Views
- **Dashboard**: Main admin dashboard with analytics
- **User Management**: Complete user CRUD operations
- **Content Management**: Places, packages, bookings, feedback
- **System Management**: Settings, notifications, audit logs
- **Bulk Operations**: Mass data operations
- **Data Export/Import**: Data management tools

### Templates
- **Modern UI**: Responsive design with Tailwind CSS
- **Interactive Components**: JavaScript-powered interactions
- **Real-time Updates**: AJAX-powered live data updates
- **Mobile Responsive**: Optimized for all device sizes

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- Django 4.2+
- PostgreSQL (recommended) or SQLite

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```

4. **Setup Admin Data**
   ```bash
   python setup_admin_data.py
   ```

5. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access Admin Panel**
   - URL: `http://localhost:8000/admin-dashboard/`
   - Login with your admin credentials

## 📱 Usage Guide

### Dashboard
- **Overview**: Get a quick overview of system statistics
- **Charts**: View data trends and patterns
- **Recent Activity**: Monitor latest system activities
- **Quick Actions**: Access frequently used features

### User Management
1. Navigate to **Users** in the sidebar
2. Use search and filters to find specific users
3. Click **Create User** to add new users
4. Use bulk actions for multiple users
5. View user details and activity history

### Content Management
1. **Places**: Manage tourist destinations
2. **Packages**: Create and manage travel packages
3. **Bookings**: Oversee all booking requests
4. **Feedback**: Moderate user reviews and ratings

### System Settings
1. Navigate to **Settings** in the sidebar
2. Configure system-wide settings
3. Manage email, payment, and API settings
4. Set up maintenance schedules

### Bulk Operations
1. Go to **Bulk Operations**
2. Select the data type (users, places, packages, bookings)
3. Choose the action to perform
4. Enter the IDs of records to process
5. Execute the operation

### Data Export
1. Navigate to **Data Export**
2. Select the data type to export
3. Apply filters if needed
4. Start the export process
5. Download the generated CSV file

## 🔐 Security Features

### Authentication & Authorization
- **Role-based Access**: Different permission levels for different admin types
- **Session Management**: Secure session handling
- **Password Security**: Strong password requirements

### Audit Logging
- **Action Tracking**: All admin actions are logged
- **IP Tracking**: Monitor admin access locations
- **Change History**: Track all data modifications
- **Compliance**: Meet regulatory requirements

### Data Protection
- **Input Validation**: All inputs are validated and sanitized
- **SQL Injection Prevention**: Parameterized queries
- **XSS Protection**: Cross-site scripting prevention
- **CSRF Protection**: Cross-site request forgery protection

## 📊 Analytics & Reporting

### Key Metrics
- **User Statistics**: Registration trends, active users, user engagement
- **Booking Analytics**: Booking trends, conversion rates, revenue
- **Content Performance**: Popular places, package performance
- **System Health**: Performance metrics, error rates

### Reports
- **Financial Reports**: Revenue analysis, payment trends
- **User Activity Reports**: User behavior, engagement metrics
- **Content Reports**: Popular destinations, package performance
- **System Reports**: Performance, errors, maintenance

## 🔧 Configuration

### Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/prayanam

# Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Security
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Admin Settings
Configure system settings through the admin panel:
- **General Settings**: Site name, description, contact info
- **Booking Settings**: Booking limits, cancellation policies
- **Email Settings**: SMTP configuration, notification preferences
- **Payment Settings**: Payment gateways, currency settings
- **API Settings**: Rate limits, API keys

## 🚀 Deployment

### Production Setup
1. **Database**: Use PostgreSQL for production
2. **Static Files**: Configure static file serving
3. **Media Files**: Set up media file storage
4. **Security**: Enable HTTPS, secure headers
5. **Monitoring**: Set up error tracking and performance monitoring

### Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Environment Configuration
```bash
# Production settings
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@db:5432/prayanam
SECRET_KEY=your-production-secret-key
```

## 🐛 Troubleshooting

### Common Issues

1. **Permission Denied**
   - Ensure user has admin role
   - Check role permissions
   - Verify user is active

2. **Data Export Issues**
   - Check file permissions
   - Verify export directory exists
   - Ensure sufficient disk space

3. **Notification Issues**
   - Verify email settings
   - Check SMTP configuration
   - Test email connectivity

4. **Performance Issues**
   - Monitor database queries
   - Check server resources
   - Optimize database indexes

### Debug Mode
Enable debug mode for development:
```python
DEBUG = True
```

### Logging
Configure logging for troubleshooting:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'admin_dashboard': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

## 📚 API Reference

### Admin API Endpoints
- `GET /admin-dashboard/api/stats/` - Get dashboard statistics
- `GET /admin-dashboard/api/notifications/count/` - Get notification count
- `POST /admin-dashboard/api/notifications/{id}/mark-read/` - Mark notification as read
- `GET /admin-dashboard/api/recent-activities/` - Get recent activities
- `POST /admin-dashboard/api/bulk-actions/{id}/progress/` - Get bulk action progress

### Authentication
All API endpoints require admin authentication:
```python
# Example API call
headers = {
    'Authorization': 'Bearer your-token',
    'Content-Type': 'application/json'
}
```

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write comprehensive docstrings
- Add unit tests

### Testing
```bash
# Run tests
python manage.py test admin_dashboard

# Run with coverage
coverage run --source='.' manage.py test admin_dashboard
coverage report
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- **Documentation**: Check this README and inline code comments
- **Issues**: Report bugs and feature requests on GitHub
- **Email**: Contact the development team
- **Community**: Join our community forum

## 🔄 Updates & Maintenance

### Regular Maintenance
- **Database Cleanup**: Remove old audit logs and temporary data
- **Backup Verification**: Ensure backups are working correctly
- **Security Updates**: Keep dependencies updated
- **Performance Monitoring**: Monitor system performance

### Version Updates
- **Backup Data**: Always backup before updates
- **Test Environment**: Test updates in staging first
- **Documentation**: Update documentation with changes
- **User Communication**: Notify users of significant changes

---

**Built with ❤️ for the Prayanam Travel Platform**

*Last updated: September 2024*
