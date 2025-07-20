<style>
/* Modern Sidebar Menu Styles */
.sidebar-menu {
    position: fixed;
    top: 0;
    left: 0;
    width: 280px;
    height: 100vh;
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border-right: 1px solid var(--border-color);
    z-index: 1000;
    transition: var(--transition);
    overflow-y: auto;
    overflow-x: hidden;
}

.sidebar-menu.collapsed {
    width: 80px;
}

.sidebar-header {
    padding: 24px;
    border-bottom: 1px solid var(--border-color);
    text-align: center;
    position: relative;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    text-decoration: none;
    color: var(--text-primary);
    transition: var(--transition);
}

.sidebar-logo:hover {
    color: var(--text-primary);
    text-decoration: none;
    transform: scale(1.05);
}

.sidebar-logo img {
    width: 40px;
    height: 40px;
    border-radius: var(--border-radius-sm);
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
}

.sidebar-logo-text {
    font-size: 1.2rem;
    font-weight: 700;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    transition: var(--transition);
}

.sidebar-menu.collapsed .sidebar-logo-text {
    opacity: 0;
    transform: translateX(-20px);
}

.sidebar-toggle {
    position: absolute;
    top: 50%;
    right: -15px;
    transform: translateY(-50%);
    width: 30px;
    height: 30px;
    background: var(--primary-gradient);
    border: none;
    border-radius: 50%;
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.9rem;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    transition: var(--transition);
    z-index: 1001;
}

.sidebar-toggle:hover {
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.sidebar-menu.collapsed .sidebar-toggle {
    right: -15px;
}

.sidebar-nav {
    padding: 20px 0;
}

.nav-section {
    margin-bottom: 32px;
}

.nav-section-title {
    padding: 0 24px 12px;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 1px;
    opacity: 0.7;
    transition: var(--transition);
}

.sidebar-menu.collapsed .nav-section-title {
    opacity: 0;
    transform: translateX(-20px);
}

.nav-item {
    position: relative;
    margin: 4px 16px;
}

.nav-link {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 20px;
    color: var(--text-secondary);
    text-decoration: none;
    border-radius: var(--border-radius-sm);
    transition: var(--transition);
    position: relative;
    overflow: hidden;
}

.nav-link::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.6s ease;
}

.nav-link:hover::before {
    left: 100%;
}

.nav-link:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    text-decoration: none;
    transform: translateX(8px);
}

.nav-link.active {
    background: var(--primary-gradient);
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.nav-link.active::after {
    content: '';
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 4px;
    height: 20px;
    background: white;
    border-radius: 2px 0 0 2px;
}

.nav-icon {
    width: 20px;
    text-align: center;
    font-size: 1.1rem;
    transition: var(--transition);
}

.nav-link:hover .nav-icon {
    transform: scale(1.2);
}

.nav-text {
    font-weight: 500;
    transition: var(--transition);
}

.sidebar-menu.collapsed .nav-text {
    opacity: 0;
    transform: translateX(-20px);
}

.nav-badge {
    position: absolute;
    top: 8px;
    right: 8px;
    background: var(--accent-gradient);
    color: white;
    border-radius: 10px;
    padding: 2px 6px;
    font-size: 0.7rem;
    font-weight: 600;
    min-width: 18px;
    text-align: center;
    transition: var(--transition);
}

.sidebar-menu.collapsed .nav-badge {
    opacity: 0;
    transform: scale(0);
}

.nav-link:hover .nav-badge {
    transform: scale(1.1);
}

/* Submenu Styles */
.nav-submenu {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    background: rgba(255, 255, 255, 0.02);
    border-radius: var(--border-radius-sm);
    margin: 4px 0;
}

.nav-submenu.show {
    max-height: 300px;
}

.submenu-item {
    padding: 0 16px;
}

.submenu-link {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 16px;
    color: var(--text-secondary);
    text-decoration: none;
    border-radius: var(--border-radius-sm);
    transition: var(--transition);
    font-size: 0.9rem;
}

.submenu-link:hover {
    background: rgba(255, 255, 255, 0.05);
    color: var(--text-primary);
    text-decoration: none;
    transform: translateX(4px);
}

.submenu-link.active {
    background: rgba(102, 126, 234, 0.1);
    color: #667eea;
}

.submenu-icon {
    width: 16px;
    text-align: center;
    font-size: 0.9rem;
}

/* Sidebar Footer */
.sidebar-footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 20px 24px;
    border-top: 1px solid var(--border-color);
    background: rgba(255, 255, 255, 0.02);
}

.sidebar-menu.collapsed .sidebar-footer {
    opacity: 0;
    transform: translateY(20px);
}

.footer-info {
    text-align: center;
    color: var(--text-secondary);
    font-size: 0.8rem;
}

.footer-version {
    font-weight: 600;
    color: #00d4aa;
}

/* Scrollbar Styling */
.sidebar-menu::-webkit-scrollbar {
    width: 4px;
}

.sidebar-menu::-webkit-scrollbar-track {
    background: transparent;
}

.sidebar-menu::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 2px;
}

.sidebar-menu::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.2);
}

/* Responsive Design */
@media (max-width: 768px) {
    .sidebar-menu {
        transform: translateX(-100%);
    }
    
    .sidebar-menu.mobile-open {
        transform: translateX(0);
    }
    
    .sidebar-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
        opacity: 0;
        visibility: hidden;
        transition: var(--transition);
    }
    
    .sidebar-overlay.show {
        opacity: 1;
        visibility: visible;
    }
}

/* Animation Classes */
.sidebar-menu {
    animation: slideInLeft 0.5s ease;
}

@keyframes slideInLeft {
    from {
        transform: translateX(-100%);
    }
    to {
        transform: translateX(0);
    }
}

.nav-item {
    animation: fadeInUp 0.5s ease;
}

.nav-item:nth-child(1) { animation-delay: 0.1s; }
.nav-item:nth-child(2) { animation-delay: 0.2s; }
.nav-item:nth-child(3) { animation-delay: 0.3s; }
.nav-item:nth-child(4) { animation-delay: 0.4s; }
.nav-item:nth-child(5) { animation-delay: 0.5s; }
.nav-item:nth-child(6) { animation-delay: 0.6s; }
.nav-item:nth-child(7) { animation-delay: 0.7s; }
.nav-item:nth-child(8) { animation-delay: 0.8s; }

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>

<div class="sidebar-menu" id="sidebarMenu">
    <div class="sidebar-header">
        <a href="dashboard.php" class="sidebar-logo">
            <img src="images/prayanam.png" alt="Prayanam">
            <span class="sidebar-logo-text">Prayanam</span>
        </a>
        <button class="sidebar-toggle" onclick="toggleSidebar()">
            <i class="fa fa-bars"></i>
        </button>
    </div>
    
    <nav class="sidebar-nav">
        <div class="nav-section">
            <div class="nav-section-title">Main Navigation</div>
            
            <div class="nav-item">
                <a href="dashboard.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'dashboard.php' ? 'active' : ''; ?>">
                    <i class="fa fa-tachometer nav-icon"></i>
                    <span class="nav-text">Dashboard</span>
                </a>
            </div>
            
            <div class="nav-item">
                <a href="create-package.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'create-package.php' ? 'active' : ''; ?>">
                    <i class="fa fa-plus nav-icon"></i>
                    <span class="nav-text">Create Package</span>
                </a>
            </div>
            
            <div class="nav-item">
                <a href="manage-packages.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'manage-packages.php' ? 'active' : ''; ?>">
                    <i class="fa fa-suitcase nav-icon"></i>
                    <span class="nav-text">Manage Packages</span>
                </a>
            </div>
        </div>
        
        <div class="nav-section">
            <div class="nav-section-title">Bookings & Enquiries</div>
            
            <div class="nav-item">
                <a href="manage-bookings.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'manage-bookings.php' ? 'active' : ''; ?>">
                    <i class="fa fa-calendar nav-icon"></i>
                    <span class="nav-text">Manage Bookings</span>
                    <span class="nav-badge">5</span>
                </a>
            </div>
            
            <div class="nav-item">
                <a href="manage-enquires.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'manage-enquires.php' ? 'active' : ''; ?>">
                    <i class="fa fa-envelope nav-icon"></i>
                    <span class="nav-text">View Enquiries</span>
                    <span class="nav-badge">3</span>
                </a>
            </div>
        </div>
        
        <div class="nav-section">
            <div class="nav-section-title">User Management</div>
            
            <div class="nav-item">
                <a href="manage-users.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'manage-users.php' ? 'active' : ''; ?>">
                    <i class="fa fa-users nav-icon"></i>
                    <span class="nav-text">Manage Users</span>
                </a>
            </div>
            
            <div class="nav-item">
                <a href="issuetickets.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'issuetickets.php' ? 'active' : ''; ?>">
                    <i class="fa fa-ticket nav-icon"></i>
                    <span class="nav-text">Issue Tickets</span>
                    <span class="nav-badge">2</span>
                </a>
            </div>
        </div>
        
        <div class="nav-section">
            <div class="nav-section-title">Settings</div>
            
            <div class="nav-item">
                <a href="change-password.php" class="nav-link <?php echo basename($_SERVER['PHP_SELF']) == 'change-password.php' ? 'active' : ''; ?>">
                    <i class="fa fa-key nav-icon"></i>
                    <span class="nav-text">Change Password</span>
                </a>
            </div>
            
            <div class="nav-item">
                <a href="logout.php" class="nav-link">
                    <i class="fa fa-sign-out nav-icon"></i>
                    <span class="nav-text">Sign Out</span>
                </a>
            </div>
        </div>
    </nav>
    
    <div class="sidebar-footer">
        <div class="footer-info">
            <div>Prayanam Admin</div>
            <div class="footer-version">v2.0.0</div>
        </div>
    </div>
</div>

<!-- Mobile Overlay -->
<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<script>
// Sidebar functionality
function toggleSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('sidebarOverlay');
    
    if (window.innerWidth <= 768) {
        // Mobile behavior
        sidebar.classList.toggle('mobile-open');
        overlay.classList.toggle('show');
    } else {
        // Desktop behavior
        sidebar.classList.toggle('collapsed');
        document.querySelector('.page-container').classList.toggle('sidebar-collapsed');
    }
}

function closeSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('sidebarOverlay');
    
    sidebar.classList.remove('mobile-open');
    overlay.classList.remove('show');
}

// Add hover effects
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(8px)';
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
        });
    });
    
    // Add active state based on current page
    const currentPage = window.location.pathname.split('/').pop();
    const activeLink = document.querySelector(`[href*="${currentPage}"]`);
    
    if (activeLink) {
        activeLink.classList.add('active');
    }
    
    // Add keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeSidebar();
        }
    });
});

// Responsive behavior
window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
        document.getElementById('sidebarOverlay').classList.remove('show');
    }
});
</script>