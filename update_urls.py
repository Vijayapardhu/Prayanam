#!/usr/bin/env python
"""
Script to update all hardcoded URLs to the new domain
"""
import os
import re

def update_urls_in_file(file_path):
    """Update URLs in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update various URL patterns
        replacements = [
            # Localhost URLs
            (r'http://127\.0\.0\.1:8000', 'https://prayanam-91p7.onrender.com'),
            (r'https://prayanam-91p7.onrender.com', 'https://prayanam-91p7.onrender.com'),
            (r'https://prayanam-91p7.onrender.com', 'https://prayanam-91p7.onrender.com'),
            (r'127\.0\.0\.1:8000', 'prayanam-91p7.onrender.com'),
            (r'prayanam-91p7.onrender.com', 'prayanam-91p7.onrender.com'),
            
            # Old domain patterns (if any)
            (r'prayanam\.onrender\.com', 'prayanam-91p7.onrender.com'),
            
            # Email templates and other references
            (r'Prayanam', 'Prayanam'),
            (r'https://prayanam-91p7.onrender.com', 'https://prayanam-91p7.onrender.com'),
        ]
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {file_path}")
            return True
        else:
            print(f"⏭️  No changes: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def find_files_to_update():
    """Find all files that might contain URLs"""
    extensions = ['.py', '.html', '.js', '.css', '.txt', '.md']
    exclude_dirs = ['__pycache__', '.git', 'node_modules', 'venv', 'env', 'migrations']
    
    files_to_update = []
    
    for root, dirs, files in os.walk('.'):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                files_to_update.append(file_path)
    
    return files_to_update

def main():
    """Main function to update all URLs"""
    print("🔄 Starting URL update process...")
    print("📍 New domain: https://prayanam-91p7.onrender.com")
    print()
    
    files_to_update = find_files_to_update()
    print(f"📁 Found {len(files_to_update)} files to check")
    print()
    
    updated_count = 0
    
    for file_path in files_to_update:
        if update_urls_in_file(file_path):
            updated_count += 1
    
    print()
    print(f"✅ Update complete! Updated {updated_count} files")
    print("🌐 All URLs now point to: https://prayanam-91p7.onrender.com")

if __name__ == "__main__":
    main()
