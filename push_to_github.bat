@echo off
echo ========================================
echo    Push to GitHub Repository
echo    https://github.com/Vijayapardhu/Prayanam.git
echo ========================================
echo.

echo Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed!
    echo.
    echo Please install Git from: https://git-scm.com/download/win
    echo After installation, restart this script.
    echo.
    pause
    exit /b 1
)

echo Git is installed!
echo.

echo Initializing Git repository...
git init

echo.
echo Adding remote origin...
git remote add origin https://github.com/Vijayapardhu/Prayanam.git

echo.
echo Creating .gitignore file...
(
echo # Python
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo *.so
echo .Python
echo build/
echo develop-eggs/
echo dist/
echo downloads/
echo eggs/
echo .eggs/
echo lib/
echo lib64/
echo parts/
echo sdist/
echo var/
echo wheels/
echo *.egg-info/
echo .installed.cfg
echo *.egg
echo.
echo # Django
echo *.log
echo local_settings.py
echo db.sqlite3
echo db.sqlite3-journal
echo media/
echo.
echo # Environment variables
echo .env
echo .venv
echo env/
echo venv/
echo ENV/
echo env.bak/
echo venv.bak/
echo.
echo # IDE
echo .vscode/
echo .idea/
echo *.swp
echo *.swo
echo.
echo # OS
echo .DS_Store
echo .DS_Store?
echo ._*
echo .Spotlight-V100
echo .Trashes
echo ehthumbs.db
echo Thumbs.db
echo.
echo # Static files ^(will be collected^)
echo staticfiles/
echo.
echo # Logs
echo logs/
echo *.log
echo.
echo # Node modules
echo node_modules/
echo npm-debug.log*
echo yarn-debug.log*
echo yarn-error.log*
echo.
echo # Backup files
echo *.bak
echo *.backup
echo *.old
) > .gitignore

echo.
echo Adding all files to Git...
git add .

echo.
echo Checking status...
git status

echo.
echo ========================================
echo    Ready to Commit and Push
echo ========================================
echo.
echo Please configure your Git identity first:
echo.
echo git config --global user.name "Vijayapardhu"
echo git config --global user.email "your-email@example.com"
echo.
echo Then run these commands:
echo.
echo git commit -m "Complete admin panel implementation with Render deployment"
echo git branch -M main
echo git push -u origin main
echo.
echo Or press any key to continue with the commit...
pause

echo.
echo Committing changes...
git commit -m "Complete admin panel implementation with Render deployment configuration

- Added comprehensive admin dashboard with all CRUD operations
- Implemented user management, content management, and system administration  
- Added real-time analytics and reporting features
- Created bulk operations and data export functionality
- Added notification system and audit logging
- Configured for Render deployment with production settings
- Added complete static files and templates
- Implemented role-based access control and security features"

echo.
echo Setting main branch...
git branch -M main

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo    Push Complete!
echo ========================================
echo.
echo Your code has been pushed to:
echo https://github.com/Vijayapardhu/Prayanam.git
echo.
echo Next steps:
echo 1. Go to https://render.com
echo 2. Sign up/login with GitHub
echo 3. Click "New +" → "Blueprint"
echo 4. Connect your repository: Vijayapardhu/Prayanam
echo 5. Render will automatically configure everything
echo.
echo For detailed instructions, see: RENDER_DEPLOYMENT.md
echo.
pause
