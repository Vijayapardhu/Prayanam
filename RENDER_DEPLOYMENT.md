# 🚀 Render Deployment Guide for Prayanam Admin Panel

This guide will help you deploy the Prayanam Admin Panel to Render, a modern cloud platform for web services.

## 📋 Prerequisites

- GitHub account
- Render account (free tier available)
- Python 3.8+ installed locally
- Git installed locally

## 🛠️ Step 1: Prepare Your Code

### 1.1 Run the Deployment Script
```bash
python deploy_to_render.py
```

This script will:
- Install all dependencies
- Run database migrations
- Collect static files
- Create an admin user
- Set up initial admin data

### 1.2 Commit and Push to GitHub
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

## 🌐 Step 2: Deploy to Render

### 2.1 Create a New Web Service

1. **Go to Render Dashboard**
   - Visit [render.com](https://render.com)
   - Sign up or log in

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository containing your code

### 2.2 Configure the Service

**Basic Settings:**
- **Name**: `prayanam-admin` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)

**Build & Deploy:**
- **Build Command**: 
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- **Start Command**: 
  ```bash
  gunicorn travel_platform.wsgi:application
  ```

### 2.3 Set Environment Variables

Click "Environment" tab and add these variables:

**Required Variables:**
```
DEBUG=False
SECRET_KEY=<generate a secure secret key>
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=<from PostgreSQL service>
```

**Optional Variables:**
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
SITE_NAME=Prayanam Admin
SITE_DOMAIN=https://your-app-name.onrender.com
```

### 2.4 Create PostgreSQL Database

1. **Create New Database**
   - Go to Render Dashboard
   - Click "New +" → "PostgreSQL"
   - Name: `prayanam-db`
   - Plan: `Starter` (free tier)
   - Region: Same as your web service

2. **Get Database URL**
   - Copy the "External Database URL"
   - Paste it as `DATABASE_URL` in your web service environment variables

## 🔧 Step 3: Advanced Configuration

### 3.1 Using render.yaml (Alternative Method)

If you prefer using the `render.yaml` file:

1. **Deploy from Blueprint**
   - Click "New +" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect and use `render.yaml`

2. **Manual Configuration**
   - The `render.yaml` file contains all necessary configuration
   - No additional setup required

### 3.2 Custom Domain (Optional)

1. **Add Custom Domain**
   - Go to your service settings
   - Click "Custom Domains"
   - Add your domain (e.g., `admin.prayanam.com`)

2. **Update Environment Variables**
   ```
   ALLOWED_HOSTS=your-app-name.onrender.com,your-custom-domain.com
   SITE_DOMAIN=https://your-custom-domain.com
   ```

## 🚀 Step 4: Deploy and Test

### 4.1 Deploy
1. Click "Create Web Service"
2. Wait for the build to complete (5-10 minutes)
3. Your service will be available at `https://your-app-name.onrender.com`

### 4.2 Test the Admin Panel
1. **Access the Admin Panel**
   - URL: `https://your-app-name.onrender.com/admin-dashboard/`
   - Login: `admin` / `admin123`

2. **Verify Features**
   - Dashboard loads correctly
   - User management works
   - All admin functions are accessible

## 🔐 Step 5: Security Configuration

### 5.1 Change Default Credentials
```bash
# Access your service shell or run locally
python manage.py shell
```

```python
from accounts.models import User
admin = User.objects.get(username='admin')
admin.set_password('your-secure-password')
admin.save()
```

### 5.2 Enable HTTPS (Automatic on Render)
- Render automatically provides HTTPS
- No additional configuration needed

### 5.3 Environment Security
- Never commit sensitive data to Git
- Use Render's environment variables for secrets
- Regularly rotate your SECRET_KEY

## 📊 Step 6: Monitoring and Maintenance

### 6.1 Monitor Performance
- Use Render's built-in metrics
- Monitor response times and error rates
- Set up alerts for downtime

### 6.2 Database Backups
- Render provides automatic backups for paid plans
- For free tier, consider manual backups

### 6.3 Logs
- View logs in Render dashboard
- Monitor for errors and performance issues

## 🛠️ Troubleshooting

### Common Issues

**1. Build Fails**
```
Error: Module not found
```
**Solution**: Ensure all dependencies are in `requirements.txt`

**2. Static Files Not Loading**
```
Error: 404 for static files
```
**Solution**: Check `STATIC_ROOT` and `STATIC_URL` settings

**3. Database Connection Error**
```
Error: could not connect to server
```
**Solution**: Verify `DATABASE_URL` is correct

**4. Admin Panel Not Accessible**
```
Error: 404 Not Found
```
**Solution**: Check URL patterns and ensure admin_dashboard is in INSTALLED_APPS

### Debug Mode
To enable debug mode temporarily:
1. Set `DEBUG=True` in environment variables
2. Redeploy the service
3. Check logs for detailed error messages

## 📈 Performance Optimization

### 1. Enable Caching
```python
# In settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}
```

### 2. Database Optimization
- Use database indexes for frequently queried fields
- Optimize queries using `select_related` and `prefetch_related`

### 3. Static Files
- Use CDN for static files (Render provides this automatically)
- Compress images and CSS/JS files

## 🔄 Updates and Maintenance

### Updating Your Application
1. Make changes to your code
2. Commit and push to GitHub
3. Render automatically redeploys

### Database Migrations
```bash
# Run migrations after code changes
python manage.py makemigrations
python manage.py migrate
```

### Backup Strategy
1. **Database Backups**: Use Render's backup feature
2. **Code Backups**: Your code is in GitHub
3. **Media Files**: Consider using cloud storage (AWS S3, etc.)

## 📞 Support

### Render Support
- Documentation: [render.com/docs](https://render.com/docs)
- Community: [render.com/community](https://render.com/community)

### Admin Panel Support
- Check logs in Render dashboard
- Verify environment variables
- Test locally first

## 🎉 Success!

Once deployed, your Prayanam Admin Panel will be available at:
**https://your-app-name.onrender.com/admin-dashboard/**

### Default Login Credentials:
- **Username**: `admin`
- **Password**: `admin123`

### Next Steps:
1. Change default password
2. Configure email settings
3. Add your domain (optional)
4. Set up monitoring
5. Create additional admin users

---

**Happy Deploying! 🚀**

*For any issues, check the troubleshooting section or contact support.*
