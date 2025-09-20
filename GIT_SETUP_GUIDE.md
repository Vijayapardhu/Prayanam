# 🔧 Git Setup Guide for Render Deployment

Since Git is not installed or configured on your system, follow this guide to set up Git and push your code to GitHub for Render deployment.

## 📋 Prerequisites

1. **GitHub Account**: Create one at [github.com](https://github.com)
2. **Git Installation**: Download from [git-scm.com](https://git-scm.com)

## 🛠️ Step 1: Install Git

### Windows Installation
1. **Download Git for Windows**
   - Go to [git-scm.com/download/win](https://git-scm.com/download/win)
   - Download the latest version
   - Run the installer with default settings

2. **Verify Installation**
   - Open Command Prompt or PowerShell
   - Run: `git --version`
   - You should see the Git version number

### Alternative: Git Bash
- Git for Windows includes Git Bash
- Use Git Bash instead of Command Prompt for better compatibility

## 🚀 Step 2: Configure Git

### Set up your identity
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Verify configuration
```bash
git config --list
```

## 📁 Step 3: Initialize Git Repository

### Navigate to your project directory
```bash
cd C:\Users\PARDHU\Desktop\prayanam
```

### Initialize Git repository
```bash
git init
```

### Create .gitignore file
```bash
# Create .gitignore file
echo "# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/

# Environment variables
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Static files (will be collected)
staticfiles/
static/admin_dashboard/css/
static/admin_dashboard/js/
static/admin_dashboard/images/

# Logs
logs/
*.log

# Node modules
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Backup files
*.bak
*.backup
*.old" > .gitignore
```

## 📝 Step 4: Add and Commit Files

### Add all files to Git
```bash
git add .
```

### Check what will be committed
```bash
git status
```

### Commit the files
```bash
git commit -m "Initial commit: Complete admin panel with Render deployment configuration"
```

## 🌐 Step 5: Create GitHub Repository

### On GitHub.com
1. **Sign in** to your GitHub account
2. **Click** the "+" icon in the top right
3. **Select** "New repository"
4. **Repository name**: `prayanam-admin-panel`
5. **Description**: `Complete admin panel for Prayanam travel platform with Render deployment`
6. **Visibility**: Public (or Private if you prefer)
7. **DO NOT** initialize with README, .gitignore, or license (we already have these)
8. **Click** "Create repository"

## 🔗 Step 6: Connect Local Repository to GitHub

### Add remote origin
```bash
git remote add origin https://github.com/YOUR_USERNAME/prayanam-admin-panel.git
```

### Replace YOUR_USERNAME with your actual GitHub username

### Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## 🚀 Step 7: Deploy to Render

### Method 1: Using Render Dashboard
1. **Go to** [render.com](https://render.com)
2. **Sign up/Login** with GitHub
3. **Click** "New +" → "Web Service"
4. **Connect** your GitHub repository
5. **Select** `prayanam-admin-panel` repository
6. **Configure** the service:
   - **Name**: `prayanam-admin`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn travel_platform.wsgi:application`

### Method 2: Using render.yaml (Recommended)
1. **Go to** [render.com](https://render.com)
2. **Click** "New +" → "Blueprint"
3. **Connect** your GitHub repository
4. **Select** `prayanam-admin-panel` repository
5. **Render will automatically detect** `render.yaml` and configure everything

## ⚙️ Step 8: Configure Environment Variables

### In Render Dashboard
1. **Go to** your service settings
2. **Click** "Environment" tab
3. **Add** these variables:

```
DEBUG=False
SECRET_KEY=<generate a secure secret key>
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=<from PostgreSQL service>
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
SITE_NAME=Prayanam Admin
SITE_DOMAIN=https://your-app-name.onrender.com
```

## 🗄️ Step 9: Create PostgreSQL Database

1. **Go to** Render Dashboard
2. **Click** "New +" → "PostgreSQL"
3. **Name**: `prayanam-db`
4. **Plan**: `Starter` (free tier)
5. **Copy** the "External Database URL"
6. **Paste** it as `DATABASE_URL` in your web service

## 🎉 Step 10: Deploy and Test

1. **Click** "Create Web Service"
2. **Wait** for deployment (5-10 minutes)
3. **Access** your admin panel at: `https://your-app-name.onrender.com/admin-dashboard/`
4. **Login** with: `admin` / `admin123`

## 🔄 Step 11: Future Updates

### To update your deployed app:
```bash
# Make changes to your code
git add .
git commit -m "Update: Description of changes"
git push origin main
```

Render will automatically redeploy when you push to the main branch.

## 🛠️ Troubleshooting

### Common Issues

**1. Git not found**
- Install Git from [git-scm.com](https://git-scm.com)
- Restart your terminal after installation

**2. Authentication failed**
- Use GitHub CLI or Personal Access Token
- Or use SSH keys for authentication

**3. Repository not found**
- Check the repository URL
- Ensure the repository exists on GitHub

**4. Build fails on Render**
- Check the build logs in Render dashboard
- Verify all dependencies are in requirements.txt

### Quick Commands Reference

```bash
# Initialize repository
git init

# Add files
git add .

# Commit changes
git commit -m "Your commit message"

# Add remote
git remote add origin https://github.com/USERNAME/REPO.git

# Push to GitHub
git push -u origin main

# Check status
git status

# View logs
git log --oneline
```

## 📞 Support

- **Git Documentation**: [git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Help**: [help.github.com](https://help.github.com)
- **Render Documentation**: [render.com/docs](https://render.com/docs)

---

**Next Steps**: After setting up Git and pushing to GitHub, follow the Render deployment guide to get your admin panel live! 🚀
