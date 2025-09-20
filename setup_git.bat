@echo off
echo ========================================
echo    Prayanam Admin Panel - Git Setup
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
echo Adding files to Git...
git add .

echo.
echo Checking status...
git status

echo.
echo ========================================
echo    Git Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Configure your Git identity:
echo    git config --global user.name "Your Name"
echo    git config --global user.email "your.email@example.com"
echo.
echo 2. Create a GitHub repository
echo 3. Add remote origin:
echo    git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
echo.
echo 4. Commit and push:
echo    git commit -m "Initial commit: Complete admin panel"
echo    git push -u origin main
echo.
echo 5. Deploy to Render using the deployment guide
echo.
echo For detailed instructions, see: GIT_SETUP_GUIDE.md
echo.
pause
