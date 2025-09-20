/* Custom Admin JavaScript for Image Upload Enhancement */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize image upload functionality
    initImageUpload();
    initImagePreview();
    initDragAndDrop();
});

function initImageUpload() {
    // Find all file inputs with image type
    const fileInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    
    fileInputs.forEach(input => {
        // Create custom file input wrapper
        const wrapper = createFileInputWrapper(input);
        input.parentNode.insertBefore(wrapper, input);
        input.style.display = 'none';
        
        // Add change event listener
        input.addEventListener('change', function(e) {
            handleFileSelect(e, wrapper);
        });
    });
}

function createFileInputWrapper(input) {
    const wrapper = document.createElement('div');
    wrapper.className = 'file-input-wrapper';
    
    const label = document.createElement('label');
    label.className = 'file-input-label';
    label.innerHTML = '<i class="fas fa-upload"></i> Choose Image File';
    label.setAttribute('for', input.id);
    
    wrapper.appendChild(label);
    wrapper.appendChild(input);
    
    return wrapper;
}

function handleFileSelect(event, wrapper) {
    const file = event.target.files[0];
    if (file) {
        // Validate file type
        if (!file.type.startsWith('image/')) {
            showMessage('Please select a valid image file.', 'error');
            return;
        }
        
        // Validate file size (max 5MB)
        if (file.size > 5 * 1024 * 1024) {
            showMessage('Image size should be less than 5MB.', 'error');
            return;
        }
        
        // Show preview
        showImagePreview(file, wrapper);
        
        // Update label
        const label = wrapper.querySelector('.file-input-label');
        label.innerHTML = '<i class="fas fa-check"></i> Image Selected: ' + file.name;
        label.style.background = '#28a745';
    }
}

function showImagePreview(file, wrapper) {
    const reader = new FileReader();
    reader.onload = function(e) {
        // Remove existing preview
        const existingPreview = wrapper.querySelector('.image-preview');
        if (existingPreview) {
            existingPreview.remove();
        }
        
        // Create preview element
        const preview = document.createElement('div');
        preview.className = 'image-preview';
        preview.innerHTML = `
            <img src="${e.target.result}" alt="Preview">
            <div class="image-info">
                <p><strong>File:</strong> ${file.name}</p>
                <p><strong>Size:</strong> ${formatFileSize(file.size)}</p>
                <p><strong>Type:</strong> ${file.type}</p>
            </div>
        `;
        
        // Insert preview after the file input
        wrapper.appendChild(preview);
    };
    reader.readAsDataURL(file);
}

function initImagePreview() {
    // Add preview functionality to existing images
    const imagePreviews = document.querySelectorAll('.image-preview img');
    imagePreviews.forEach(img => {
        img.addEventListener('click', function() {
            openImageModal(this.src, this.alt);
        });
        img.style.cursor = 'pointer';
        img.title = 'Click to view full size';
    });
}

function openImageModal(src, alt) {
    // Create modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        cursor: pointer;
    `;
    
    const img = document.createElement('img');
    img.src = src;
    img.alt = alt;
    img.style.cssText = `
        max-width: 90%;
        max-height: 90%;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    `;
    
    modal.appendChild(img);
    document.body.appendChild(modal);
    
    // Close modal on click
    modal.addEventListener('click', function() {
        document.body.removeChild(modal);
    });
}

function initDragAndDrop() {
    const uploadAreas = document.querySelectorAll('.image-upload-area');
    
    uploadAreas.forEach(area => {
        area.addEventListener('dragover', function(e) {
            e.preventDefault();
            this.classList.add('dragover');
        });
        
        area.addEventListener('dragleave', function(e) {
            e.preventDefault();
            this.classList.remove('dragover');
        });
        
        area.addEventListener('drop', function(e) {
            e.preventDefault();
            this.classList.remove('dragover');
            
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                const file = files[0];
                if (file.type.startsWith('image/')) {
                    // Find associated file input
                    const fileInput = this.parentNode.querySelector('input[type="file"]');
                    if (fileInput) {
                        // Create a new FileList
                        const dt = new DataTransfer();
                        dt.items.add(file);
                        fileInput.files = dt.files;
                        
                        // Trigger change event
                        const event = new Event('change', { bubbles: true });
                        fileInput.dispatchEvent(event);
                    }
                } else {
                    showMessage('Please drop a valid image file.', 'error');
                }
            }
        });
    });
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function showMessage(message, type = 'info') {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.admin-message');
    existingMessages.forEach(msg => msg.remove());
    
    // Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `admin-message image-upload-${type}`;
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 12px 20px;
        border-radius: 4px;
        color: white;
        font-weight: bold;
        z-index: 10001;
        animation: slideIn 0.3s ease;
    `;
    
    if (type === 'error') {
        messageDiv.style.background = '#dc3545';
    } else if (type === 'success') {
        messageDiv.style.background = '#28a745';
    } else {
        messageDiv.style.background = '#007cba';
    }
    
    messageDiv.textContent = message;
    document.body.appendChild(messageDiv);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                if (messageDiv.parentNode) {
                    messageDiv.parentNode.removeChild(messageDiv);
                }
            }, 300);
        }
    }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);
