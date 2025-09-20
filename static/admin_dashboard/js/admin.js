// Admin Dashboard JavaScript

// Global variables
let sidebarOpen = false;
let currentPage = 'dashboard';

// Initialize the admin dashboard
document.addEventListener('DOMContentLoaded', function() {
    initializeAdminDashboard();
    setupEventListeners();
    loadDashboardData();
});

// Initialize admin dashboard
function initializeAdminDashboard() {
    // Set up sidebar toggle
    const sidebarToggle = document.getElementById('sidebar-toggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
    }
    
    // Set up notification system
    setupNotificationSystem();
    
    // Set up real-time updates
    setupRealTimeUpdates();
    
    // Initialize charts
    initializeCharts();
    
    // Set up form handlers
    setupFormHandlers();
}

// Setup event listeners
function setupEventListeners() {
    // Navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const page = this.getAttribute('data-page');
            if (page) {
                navigateToPage(page);
            }
        });
    });
    
    // Search functionality
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', handleSearch);
    }
    
    // Filter buttons
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            applyFilter(filter);
        });
    });
    
    // Bulk action buttons
    const bulkActionBtns = document.querySelectorAll('.bulk-action-btn');
    bulkActionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const action = this.getAttribute('data-action');
            performBulkAction(action);
        });
    });
}

// Toggle sidebar
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    
    sidebarOpen = !sidebarOpen;
    
    if (sidebarOpen) {
        sidebar.classList.add('open');
        mainContent.style.marginLeft = '0';
    } else {
        sidebar.classList.remove('open');
        mainContent.style.marginLeft = '280px';
    }
}

// Navigate to page
function navigateToPage(page) {
    // Update active nav link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('data-page') === page) {
            link.classList.add('active');
        }
    });
    
    // Update page content
    currentPage = page;
    loadPageContent(page);
}

// Load page content
function loadPageContent(page) {
    const contentArea = document.querySelector('.content');
    if (!contentArea) return;
    
    // Show loading state
    contentArea.innerHTML = '<div class="text-center p-4"><div class="loading"></div> Loading...</div>';
    
    // Simulate page load (replace with actual AJAX calls)
    setTimeout(() => {
        switch(page) {
            case 'dashboard':
                loadDashboardContent();
                break;
            case 'users':
                loadUsersContent();
                break;
            case 'places':
                loadPlacesContent();
                break;
            case 'packages':
                loadPackagesContent();
                break;
            case 'bookings':
                loadBookingsContent();
                break;
            case 'analytics':
                loadAnalyticsContent();
                break;
            case 'settings':
                loadSettingsContent();
                break;
            case 'notifications':
                loadNotificationsContent();
                break;
            case 'audit-logs':
                loadAuditLogsContent();
                break;
            case 'bulk-operations':
                loadBulkOperationsContent();
                break;
            case 'data-export':
                loadDataExportContent();
                break;
            default:
                loadDashboardContent();
        }
    }, 500);
}

// Load dashboard content
function loadDashboardContent() {
    const contentArea = document.querySelector('.content');
    contentArea.innerHTML = `
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-header">
                    <div class="stat-icon primary">
                        <i class="fas fa-users"></i>
                    </div>
                </div>
                <div class="stat-value" id="total-users">-</div>
                <div class="stat-label">Total Users</div>
                <div class="stat-change positive">
                    <i class="fas fa-arrow-up"></i>
                    <span id="users-change">+12%</span>
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-header">
                    <div class="stat-icon success">
                        <i class="fas fa-calendar-check"></i>
                    </div>
                </div>
                <div class="stat-value" id="total-bookings">-</div>
                <div class="stat-label">Total Bookings</div>
                <div class="stat-change positive">
                    <i class="fas fa-arrow-up"></i>
                    <span id="bookings-change">+8%</span>
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-header">
                    <div class="stat-icon warning">
                        <i class="fas fa-rupee-sign"></i>
                    </div>
                </div>
                <div class="stat-value" id="total-revenue">-</div>
                <div class="stat-label">Total Revenue</div>
                <div class="stat-change positive">
                    <i class="fas fa-arrow-up"></i>
                    <span id="revenue-change">+15%</span>
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-header">
                    <div class="stat-icon error">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                </div>
                <div class="stat-value" id="total-places">-</div>
                <div class="stat-label">Total Places</div>
                <div class="stat-change positive">
                    <i class="fas fa-arrow-up"></i>
                    <span id="places-change">+5%</span>
                </div>
            </div>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="card">
                <div class="card-header">
                    <h3 class="card-title">Recent Bookings</h3>
                    <p class="card-subtitle">Latest booking activities</p>
                </div>
                <div class="card-body">
                    <div id="recent-bookings">
                        <div class="text-center p-4">
                            <div class="loading"></div>
                            Loading...
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">
                    <h3 class="card-title">System Status</h3>
                    <p class="card-subtitle">Current system health</p>
                </div>
                <div class="card-body">
                    <div id="system-status">
                        <div class="text-center p-4">
                            <div class="loading"></div>
                            Loading...
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    // Load dashboard data
    loadDashboardData();
}

// Load dashboard data
function loadDashboardData() {
    // Load statistics
    fetch('/admin-dashboard/api/stats/')
        .then(response => response.json())
        .then(data => {
            updateDashboardStats(data);
        })
        .catch(error => {
            console.error('Error loading dashboard stats:', error);
        });
    
    // Load recent bookings
    fetch('/admin-dashboard/api/recent-bookings/')
        .then(response => response.json())
        .then(data => {
            updateRecentBookings(data);
        })
        .catch(error => {
            console.error('Error loading recent bookings:', error);
        });
    
    // Load system status
    fetch('/admin-dashboard/api/system-status/')
        .then(response => response.json())
        .then(data => {
            updateSystemStatus(data);
        })
        .catch(error => {
            console.error('Error loading system status:', error);
        });
}

// Update dashboard statistics
function updateDashboardStats(data) {
    const elements = {
        'total-users': data.total_users || 0,
        'total-bookings': data.total_bookings || 0,
        'total-revenue': data.total_revenue || 0,
        'total-places': data.total_places || 0,
        'users-change': data.users_change || '+0%',
        'bookings-change': data.bookings_change || '+0%',
        'revenue-change': data.revenue_change || '+0%',
        'places-change': data.places_change || '+0%'
    };
    
    Object.entries(elements).forEach(([id, value]) => {
        const element = document.getElementById(id);
        if (element) {
            element.textContent = value;
        }
    });
}

// Update recent bookings
function updateRecentBookings(data) {
    const container = document.getElementById('recent-bookings');
    if (!container) return;
    
    if (data.bookings && data.bookings.length > 0) {
        container.innerHTML = data.bookings.map(booking => `
            <div class="flex items-center justify-between p-3 border-b border-gray-200 last:border-b-0">
                <div class="flex items-center space-x-3">
                    <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                        <i class="fas fa-user text-blue-600"></i>
                    </div>
                    <div>
                        <p class="font-medium text-gray-900">${booking.user_name}</p>
                        <p class="text-sm text-gray-500">${booking.package_name}</p>
                    </div>
                </div>
                <div class="text-right">
                    <p class="text-sm font-medium text-gray-900">₹${booking.amount}</p>
                    <p class="text-xs text-gray-500">${booking.date}</p>
                </div>
            </div>
        `).join('');
    } else {
        container.innerHTML = '<p class="text-gray-500 text-center py-4">No recent bookings</p>';
    }
}

// Update system status
function updateSystemStatus(data) {
    const container = document.getElementById('system-status');
    if (!container) return;
    
    const statusItems = [
        { name: 'Database', status: data.database || 'online', color: 'green' },
        { name: 'Email Service', status: data.email || 'online', color: 'green' },
        { name: 'Payment Gateway', status: data.payment || 'online', color: 'green' },
        { name: 'File Storage', status: data.storage || 'online', color: 'green' }
    ];
    
    container.innerHTML = statusItems.map(item => `
        <div class="flex items-center justify-between p-3 border-b border-gray-200 last:border-b-0">
            <div class="flex items-center space-x-3">
                <div class="w-3 h-3 bg-${item.color}-500 rounded-full"></div>
                <span class="font-medium text-gray-900">${item.name}</span>
            </div>
            <span class="text-sm text-${item.color}-600 font-medium">${item.status}</span>
        </div>
    `).join('');
}

// Setup notification system
function setupNotificationSystem() {
    // Check for new notifications periodically
    setInterval(checkNotifications, 30000); // Check every 30 seconds
    
    // Load initial notification count
    loadNotificationCount();
}

// Check for notifications
function checkNotifications() {
    fetch('/admin-dashboard/api/notifications/count/')
        .then(response => response.json())
        .then(data => {
            updateNotificationCount(data.count);
        })
        .catch(error => {
            console.error('Error checking notifications:', error);
        });
}

// Load notification count
function loadNotificationCount() {
    checkNotifications();
}

// Update notification count
function updateNotificationCount(count) {
    const badge = document.querySelector('.notification-badge');
    if (badge) {
        if (count > 0) {
            badge.textContent = count;
            badge.style.display = 'flex';
        } else {
            badge.style.display = 'none';
        }
    }
}

// Setup real-time updates
function setupRealTimeUpdates() {
    // Update dashboard data every 5 minutes
    setInterval(() => {
        if (currentPage === 'dashboard') {
            loadDashboardData();
        }
    }, 300000);
}

// Initialize charts
function initializeCharts() {
    // This would initialize Chart.js charts
    // Implementation depends on specific chart requirements
}

// Setup form handlers
function setupFormHandlers() {
    // Handle form submissions
    const forms = document.querySelectorAll('form[data-ajax="true"]');
    forms.forEach(form => {
        form.addEventListener('submit', handleAjaxFormSubmit);
    });
}

// Handle AJAX form submission
function handleAjaxFormSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const action = form.getAttribute('action');
    const method = form.getAttribute('method') || 'POST';
    
    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.innerHTML = '<div class="loading"></div> Processing...';
    submitBtn.disabled = true;
    
    fetch(action, {
        method: method,
        body: formData,
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification('Success!', data.message || 'Operation completed successfully.', 'success');
            if (data.redirect) {
                window.location.href = data.redirect;
            }
        } else {
            showNotification('Error!', data.message || 'An error occurred.', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error!', 'An error occurred while processing your request.', 'error');
    })
    .finally(() => {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    });
}

// Get CSRF token
function getCSRFToken() {
    const token = document.querySelector('[name=csrfmiddlewaretoken]');
    return token ? token.value : '';
}

// Show notification
function showNotification(title, message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} fixed top-4 right-4 z-50 max-w-sm`;
    notification.innerHTML = `
        <div class="flex items-start">
            <div class="flex-1">
                <h4 class="font-medium">${title}</h4>
                <p class="text-sm mt-1">${message}</p>
            </div>
            <button class="ml-2 text-lg" onclick="this.parentElement.parentElement.remove()">&times;</button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 5000);
}

// Handle search
function handleSearch(e) {
    const query = e.target.value;
    const searchType = e.target.getAttribute('data-search-type') || 'all';
    
    if (query.length < 2) return;
    
    // Implement search functionality
    console.log('Searching for:', query, 'in', searchType);
}

// Apply filter
function applyFilter(filter) {
    console.log('Applying filter:', filter);
    // Implement filter functionality
}

// Perform bulk action
function performBulkAction(action) {
    const selectedItems = getSelectedItems();
    if (selectedItems.length === 0) {
        showNotification('Warning!', 'Please select items to perform this action.', 'warning');
        return;
    }
    
    if (confirm(`Are you sure you want to ${action} ${selectedItems.length} item(s)?`)) {
        // Implement bulk action
        console.log('Performing bulk action:', action, 'on', selectedItems);
    }
}

// Get selected items
function getSelectedItems() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

// Load page-specific content functions
function loadUsersContent() {
    // Implementation for users page
    console.log('Loading users content');
}

function loadPlacesContent() {
    // Implementation for places page
    console.log('Loading places content');
}

function loadPackagesContent() {
    // Implementation for packages page
    console.log('Loading packages content');
}

function loadBookingsContent() {
    // Implementation for bookings page
    console.log('Loading bookings content');
}

function loadAnalyticsContent() {
    // Implementation for analytics page
    console.log('Loading analytics content');
}

function loadSettingsContent() {
    // Implementation for settings page
    console.log('Loading settings content');
}

function loadNotificationsContent() {
    // Implementation for notifications page
    console.log('Loading notifications content');
}

function loadAuditLogsContent() {
    // Implementation for audit logs page
    console.log('Loading audit logs content');
}

function loadBulkOperationsContent() {
    // Implementation for bulk operations page
    console.log('Loading bulk operations content');
}

function loadDataExportContent() {
    // Implementation for data export page
    console.log('Loading data export content');
}

// Utility functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR'
    }).format(amount);
}

function formatDate(date) {
    return new Intl.DateTimeFormat('en-IN', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    }).format(new Date(date));
}

function formatDateTime(date) {
    return new Intl.DateTimeFormat('en-IN', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }).format(new Date(date));
}

// Export functions for global use
window.AdminDashboard = {
    navigateToPage,
    showNotification,
    formatCurrency,
    formatDate,
    formatDateTime
};
