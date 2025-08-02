<style>
/* Professional Interactive Header - Complete Redesign */
.header-main {
    background: rgba(30, 60, 114, 0.55);
    backdrop-filter: blur(18px) saturate(1.2);
    -webkit-backdrop-filter: blur(18px) saturate(1.2);
    border-bottom: 1.5px solid rgba(255,255,255,0.18);
    box-shadow: 0 8px 32px rgba(30,60,114,0.10);
    position: sticky;
    top: 0;
    z-index: 1000;
    border-radius: 0 0 24px 24px;
}

/* SURPRISE: Floating Particles Background */
.header-main::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: 
        radial-gradient(2px 2px at 20px 30px, rgba(255,255,255,0.3), transparent),
        radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.2), transparent),
        radial-gradient(1px 1px at 90px 40px, rgba(255,255,255,0.4), transparent),
        radial-gradient(1px 1px at 130px 80px, rgba(255,255,255,0.3), transparent),
        radial-gradient(2px 2px at 160px 30px, rgba(255,255,255,0.2), transparent);
    background-repeat: repeat;
    background-size: 200px 100px;
    animation: particleFloat 20s linear infinite;
    pointer-events: none;
}

@keyframes particleFloat {
    0% { transform: translateY(0px); }
    100% { transform: translateY(-100px); }
}

.header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 32px;
    min-height: 72px;
}

.logo-section {
    display: flex;
    align-items: center;
    gap: 24px;
}

.logo-w3-agile h1 {
    margin: 0;
    padding: 0;
}

.logo-w3-agile h1 a {
    display: flex;
    align-items: center;
    text-decoration: none;
    padding: 10px 18px;
    border-radius: 16px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    transition: background 0.3s, box-shadow 0.3s;
}

/* SURPRISE: 3D Hover Effect */
.logo-w3-agile h1 a:hover {
    background: rgba(255,255,255,0.18);
    box-shadow: 0 6px 24px rgba(0,212,170,0.10);
}

.logo-w3-agile h1 a::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.6s ease;
}

.logo-w3-agile h1 a:hover::before {
    left: 100%;
}

.logo-w3-agile img {
    max-height: 38px;
    width: auto;
    border-radius: 10px;
    margin-right: 12px;
    box-shadow: 0 0 18px 2px #00d4aa33;
}

.logo-w3-agile h1 a:hover img {
    transform: scale(1.05) rotate(5deg);
    filter: drop-shadow(0 6px 12px rgba(0,0,0,0.3)) hue-rotate(180deg);
}

.brand-text {
    color: white;
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.10);
}

.brand-text::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(90deg, #00d4aa, #0099cc);
    transition: width 0.4s ease;
}

.logo-w3-agile h1 a:hover .brand-text::after {
    width: 100%;
}

.header-actions {
    display: flex;
    align-items: center;
    gap: 24px;
    min-width: 320px;
    justify-content: flex-end;
}

/* SURPRISE: AI Assistant Button */
.ai-assistant {
    color: rgba(255,255,255,0.95);
    font-size: 1.25rem;
    padding: 10px;
    border-radius: 12px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 2px 8px rgba(0,212,170,0.10);
    cursor: pointer;
    transition: background 0.3s, box-shadow 0.3s;
}

@keyframes aiGlow {
    0% { box-shadow: 0 0 20px rgba(255, 107, 107, 0.3); }
    100% { box-shadow: 0 0 30px rgba(255, 107, 107, 0.6); }
}

.ai-assistant:hover {
    background: rgba(0,212,170,0.13);
    box-shadow: 0 6px 24px rgba(0,212,170,0.10);
}

/* Interactive Notification Bell */
.notification-bell {
    position: relative;
    color: rgba(255,255,255,0.95);
    font-size: 1.25rem;
    padding: 10px;
    border-radius: 12px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 2px 8px rgba(30,60,114,0.10);
    cursor: pointer;
    transition: background 0.3s, box-shadow 0.3s;
}

.notification-bell::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background: rgba(255,255,255,0.2);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition: all 0.3s ease;
}

.notification-bell:hover::before {
    width: 100%;
    height: 100%;
}

.notification-bell:hover {
    background: rgba(255,255,255,0.18);
    box-shadow: 0 6px 24px rgba(30,60,114,0.10);
}

.notification-bell:active {
    transform: translateY(0) scale(0.95);
}

.notification-badge {
    position: absolute;
    top: 2px;
    right: 2px;
    background: linear-gradient(135deg, #ff6b6b, #ee5a52);
    color: white;
    border-radius: 50%;
    width: 18px;
    height: 18px;
    font-size: 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    border: 2px solid #1e3c72;
    box-shadow: 0 2px 8px rgba(255, 107, 107, 0.18);
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

/* Interactive Profile Section */
.profile_details {
    position: relative;
    display: flex;
    align-items: center;
}

.profile_details ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.profile_details_drop {
    position: relative;
}

.profile_details_drop .dropdown-toggle {
    display: flex;
    align-items: center;
    padding: 10px 18px;
    background: rgba(255,255,255,0.10);
    border-radius: 16px;
    text-decoration: none;
    color: #1e3c72;
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: background 0.3s, box-shadow 0.3s;
}

.profile_details_drop .dropdown-toggle::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.6s ease;
}

.profile_details_drop .dropdown-toggle:hover::before {
    left: 100%;
}

.profile_details_drop .dropdown-toggle:hover {
    background: rgba(0,212,170,0.13);
    box-shadow: 0 6px 24px rgba(0,212,170,0.10);
}

.profile_img {
    display: flex;
    align-items: center;
    gap: 12px;
}

.prfil-img {
    position: relative;
}

.prfil-img::after {
    content: '';
    position: absolute;
    bottom: -2px;
    right: -2px;
    width: 14px;
    height: 14px;
    background: #00d4aa;
    border-radius: 50%;
    border: 2px solid #1e3c72;
    box-shadow: 0 2px 8px rgba(0, 212, 170, 0.4);
    animation: statusPulse 3s infinite;
}

@keyframes statusPulse {
    0% { box-shadow: 0 2px 8px rgba(0, 212, 170, 0.4); }
    50% { box-shadow: 0 2px 12px rgba(0, 212, 170, 0.6); }
    100% { box-shadow: 0 2px 8px rgba(0, 212, 170, 0.4); }
}

.prfil-img img {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid rgba(255,255,255,0.18);
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
}

.profile_details_drop:hover .prfil-img img {
    border-color: rgba(255,255,255,0.4);
    transform: scale(1.08) rotate(5deg);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

.user-name {
    display: flex;
    flex-direction: column;
    text-align: left;
}

.user-name p {
    margin: 0;
    font-size: 0.7rem;
    color: #1e3c72;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.user-name span {
    font-size: 1rem;
    font-weight: 600;
    color: #1e3c72;
    text-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

.profile_details_drop:hover .user-name p,
.profile_details_drop:hover .user-name span {
    color: white;
}

.fa-angle-down, .fa-angle-up {
    color: #1e3c72;
    margin-left: 10px;
    font-size: 0.9rem;
    transition: transform 0.3s;
}

.dropdown.open .fa-angle-down {
    transform: rotate(180deg);
}

.profile_details_drop:hover .fa-angle-down,
.profile_details_drop:hover .fa-angle-up {
    color: white;
    transform: translateY(1px);
}

/* Interactive Dropdown Menu */
.drp-mnu {
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(16px) saturate(1.2);
    -webkit-backdrop-filter: blur(16px) saturate(1.2);
    border: 1.5px solid rgba(255,255,255,0.18);
    border-radius: 16px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.10);
    padding: 10px 0;
    min-width: 220px;
    margin-top: 10px;
    position: absolute;
    right: 0;
    top: 54px;
    z-index: 1003;
    display: none;
    animation: fadeInDown 0.3s;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-15px) scale(0.95);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.drp-mnu::before {
    content: '';
    position: absolute;
    top: -6px;
    right: 25px;
    width: 0;
    height: 0;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-bottom: 6px solid rgba(30, 60, 114, 0.95);
}

.drp-mnu li {
    margin: 0;
    position: relative;
}

.drp-mnu li a {
    padding: 14px 22px;
    color: #1e3c72;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 500;
    border-radius: 10px;
    font-size: 0.95rem;
    transition: background 0.3s, color 0.3s;
}

.drp-mnu li a::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.5s ease;
}

.drp-mnu li a:hover::before {
    left: 100%;
}

.drp-mnu li a:hover {
    background: linear-gradient(135deg, #00d4aa 0%, #0099cc 100%);
    color: white;
    text-decoration: none;
    transform: translateX(6px) scale(1.03);
}

.drp-mnu li a i {
    width: 18px;
    text-align: center;
    font-size: 1rem;
    transition: transform 0.3s;
}

.drp-mnu li a:hover i {
    transform: scale(1.2);
}

/* SURPRISE: Voice Command Indicator */
.voice-indicator {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #00d4aa, #0099cc);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
    box-shadow: 0 8px 25px rgba(0, 212, 170, 0.3);
    transition: all 0.3s ease;
    z-index: 1002;
    opacity: 0;
    transform: scale(0);
    animation: voiceAppear 0.5s ease forwards 2s;
}

@keyframes voiceAppear {
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.voice-indicator.listening {
    animation: voiceListening 1s ease-in-out infinite;
    background: linear-gradient(135deg, #ff6b6b, #ee5a52);
}

@keyframes voiceListening {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

/* SURPRISE: Floating Action Menu */
.floating-menu {
    position: fixed;
    bottom: 30px;
    right: 30px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 1001;
}

.floating-btn {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    transition: all 0.3s ease;
    opacity: 0;
    transform: translateY(20px);
    animation: floatAppear 0.5s ease forwards;
}

.floating-btn:nth-child(1) { animation-delay: 0.5s; }
.floating-btn:nth-child(2) { animation-delay: 0.7s; }
.floating-btn:nth-child(3) { animation-delay: 0.9s; }

@keyframes floatAppear {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.floating-btn:hover {
    transform: translateY(-5px) scale(1.1);
    box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .header-container {
        padding: 12px 20px;
    }
    
    .logo-w3-agile img {
        max-height: 30px;
    }
    
    .brand-text {
        display: none;
    }
    
    .profile_details_drop .dropdown-toggle {
        padding: 10px 15px;
    }
    
    .user-name {
        display: none;
    }
    
    .prfil-img img {
        width: 36px;
        height: 36px;
    }
    
    .notification-bell {
        font-size: 1.1rem;
        padding: 10px;
    }
    
    .header-actions {
        gap: 15px;
    }
    
    .ai-assistant {
        display: none;
    }
}

/* Header Animation */
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.header-main {
    animation: fadeInDown 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Interactive Hover Effects */
.header-main:hover {
    box-shadow: 0 12px 40px rgba(0,0,0,0.2);
}

/* Loading Animation for Elements */
.logo-section, .header-actions {
    animation: fadeInDown 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.logo-section { animation-delay: 0.1s; }
.header-actions { animation-delay: 0.2s; }

/* Animated Gradient Header */
.header-main {
    background: linear-gradient(270deg, #1e3c72, #2a5298, #00d4aa, #667eea, #ff6b6b, #1e3c72);
    background-size: 1200% 1200%;
    animation: gradientMove 18s ease infinite;
    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
    border-bottom: 1px solid rgba(255,255,255,0.12);
    position: sticky;
    top: 0;
    z-index: 1000;
    overflow: visible;
}
@keyframes gradientMove {
    0% {background-position:0% 50%}
    50% {background-position:100% 50%}
    100% {background-position:0% 50%}
}
/* Glowing Logo */
.logo-w3-agile img {
    box-shadow: 0 0 24px 6px #00d4aa, 0 0 0 0 #fff;
    border-radius: 12px;
    transition: box-shadow 0.4s;
}
.logo-w3-agile img:hover {
    box-shadow: 0 0 48px 12px #ff6b6b, 0 0 0 0 #fff;
    filter: hue-rotate(90deg) brightness(1.2);
}
/* Live Clock */
.live-clock {
    color: #fff;
    font-size: 1.08rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    background: rgba(255,255,255,0.10);
    border-radius: 12px;
    padding: 6px 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
    display: flex;
    align-items: center;
    gap: 8px;
    user-select: none;
    border: 1px solid rgba(255,255,255,0.18);
}
.live-clock i {
    color: #00d4aa;
    font-size: 1.1rem;
}
/* Confetti burst effect */
@keyframes confettiBurst {
    0% {transform: scale(0.2) translateY(0); opacity: 1;}
    80% {transform: scale(1.2) translateY(-60px); opacity: 1;}
    100% {transform: scale(1) translateY(-100px); opacity: 0;}
}
.confetti-piece {
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 2000;
    animation: confettiBurst 1.2s cubic-bezier(.6,-0.28,.74,.05) forwards;
}
</style>

<div class="header-main">
    <div class="header-container">
        <div class="logo-section">
            <div class="logo-w3-agile">
                <h1><a href="dashboard.php">
                    <img src="images/prayanam.png" alt="Prayanam">
                    <span class="brand-text">Prayanam Dashboard</span>
                </a></h1>
            </div>
            <div class="live-clock" id="liveClock"><i class="fa fa-clock-o"></i> <span>--:--:--</span></div>
        </div>
        
        <div class="header-actions">
            <!-- AI Assistant Button -->
            <div class="ai-assistant" onclick="activateAI()">
                <i class="fa fa-robot"></i>
            </div>
            <!-- Notification Bell with Dropdown -->
            <div class="notification-bell" tabindex="0" onclick="toggleNotificationDropdown(event)">
                <i class="fa fa-bell"></i>
                <span class="notification-badge">3</span>
                <div class="notification-dropdown" id="notificationDropdown">
                    <div class="notification-dropdown-header">Notifications</div>
                    <div class="notification-dropdown-list">
                        <div>• New booking received</div>
                        <div>• Customer enquiry pending</div>
                        <div>• System update available</div>
                    </div>
                    <div class="notification-dropdown-footer">
                        <button onclick="markNotificationsRead(); event.stopPropagation();">Mark All Read</button>
                    </div>
                </div>
            </div>
            <!-- Profile Dropdown with Real Username -->
            <div class="profile_details w3l">
                <ul>
                    <li class="dropdown profile_details_drop">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false" onclick="toggleProfileDropdown(event)">
                            <div class="profile_img">    
                                <span class="prfil-img"><img src="images/User-icon.png" alt="Admin"> </span> 
                                <div class="user-name">
                                    <p>Welcome</p>
                                    <span><?php echo isset($_SESSION['alogin']) ? htmlentities($_SESSION['alogin']) : 'Administrator'; ?></span>
                                </div>
                                <i class="fa fa-angle-down"></i>
                                <i class="fa fa-angle-up"></i>
                            </div>    
                        </a>
                        <ul class="dropdown-menu drp-mnu">
                            <li> <a href="dashboard.php"><i class="fa fa-tachometer"></i> Dashboard</a> </li>
                            <li> <a href="change-password.php"><i class="fa fa-user"></i> My Profile</a> </li>
                            <li> <a href="manage-packages.php"><i class="fa fa-suitcase"></i> Manage Packages</a> </li>
                            <li> <a href="manage-bookings.php"><i class="fa fa-calendar"></i> Manage Bookings</a> </li>
                            <li> <a href="manage-enquires.php"><i class="fa fa-envelope"></i> View Enquiries</a> </li>
                            <li> <a href="logout.php"><i class="fa fa-sign-out"></i> Sign Out</a> </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
<script>
// Live Clock
function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2, '0');
    const m = String(now.getMinutes()).padStart(2, '0');
    const s = String(now.getSeconds()).padStart(2, '0');
    document.querySelector('#liveClock span').textContent = `${h}:${m}:${s}`;
}
setInterval(updateClock, 1000);
updateClock();
// Confetti burst on profile click
function confettiBurst(e) {
    e.preventDefault();
    const rect = e.target.closest('.profile_img').getBoundingClientRect();
    for (let i = 0; i < 30; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti-piece';
        confetti.style.left = (rect.left + rect.width/2 + (Math.random()-0.5)*60) + 'px';
        confetti.style.top = (rect.top + rect.height/2) + 'px';
        confetti.style.background = `hsl(${Math.random()*360}, 80%, 60%)`;
        confetti.style.animationDelay = (Math.random()*0.3) + 's';
        document.body.appendChild(confetti);
        setTimeout(() => confetti.remove(), 1400);
    }
}
// Notification dropdown logic
function toggleNotificationDropdown(e) {
    e.stopPropagation();
    var bell = e.currentTarget;
    bell.classList.toggle('open');
    document.addEventListener('click', closeNotificationDropdown);
}
function closeNotificationDropdown(e) {
    var bell = document.querySelector('.notification-bell');
    if (bell) bell.classList.remove('open');
    document.removeEventListener('click', closeNotificationDropdown);
}
function markNotificationsRead() {
    var badge = document.querySelector('.notification-badge');
    if (badge) badge.textContent = '0';
    var bell = document.querySelector('.notification-bell');
    if (bell) bell.classList.remove('open');
}
// Profile dropdown logic
function toggleProfileDropdown(e) {
    e.preventDefault();
    var drop = e.currentTarget.closest('.profile_details_drop');
    drop.classList.toggle('open');
    document.addEventListener('click', closeProfileDropdown);
}
function closeProfileDropdown(e) {
    var drop = document.querySelector('.profile_details_drop');
    if (drop) drop.classList.remove('open');
    document.removeEventListener('click', closeProfileDropdown);
}
</script>

<!-- SURPRISE: Voice Command Indicator -->
<div class="voice-indicator" onclick="toggleVoiceCommands()">
    <i class="fa fa-microphone"></i>
</div>

<!-- SURPRISE: Floating Action Menu -->
<div class="floating-menu">
    <button class="floating-btn" onclick="quickAction('dashboard')" title="Quick Dashboard">
        <i class="fa fa-tachometer"></i>
    </button>
    <button class="floating-btn" onclick="quickAction('create')" title="Create Package">
        <i class="fa fa-plus"></i>
    </button>
    <button class="floating-btn" onclick="quickAction('analytics')" title="Analytics">
        <i class="fa fa-chart-line"></i>
    </button>
</div>

<script>
// SURPRISE: Interactive JavaScript with AI and Voice Commands
document.addEventListener('DOMContentLoaded', function() {
    // Initialize surprise features
    initializeSurprises();
    
    // Notification bell interaction
    const notificationBell = document.querySelector('.notification-bell');
    if (notificationBell) {
        notificationBell.addEventListener('click', function(e) {
            e.preventDefault();
            // Add ripple effect
            const ripple = document.createElement('span');
            ripple.style.position = 'absolute';
            ripple.style.borderRadius = '50%';
            ripple.style.background = 'rgba(255,255,255,0.3)';
            ripple.style.transform = 'scale(0)';
            ripple.style.animation = 'ripple 0.6s linear';
            ripple.style.left = (e.clientX - this.offsetLeft) + 'px';
            ripple.style.top = (e.clientY - this.offsetTop) + 'px';
            ripple.style.width = ripple.style.height = '20px';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
            
            showNotificationPanel();
        });
    }
    
    // Profile dropdown enhancement
    const profileDropdown = document.querySelector('.profile_details_drop');
    if (profileDropdown) {
        const dropdownToggle = profileDropdown.querySelector('.dropdown-toggle');
        const dropdownMenu = profileDropdown.querySelector('.dropdown-menu');
        
        dropdownToggle.addEventListener('click', function(e) {
            e.preventDefault();
            const isOpen = dropdownMenu.classList.contains('show');
            
            document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
                menu.classList.remove('show');
            });
            
            if (!isOpen) {
                dropdownMenu.classList.add('show');
                profileDropdown.classList.add('open');
            } else {
                dropdownMenu.classList.remove('show');
                profileDropdown.classList.remove('open');
            }
        });
        
        document.addEventListener('click', function(e) {
            if (!profileDropdown.contains(e.target)) {
                dropdownMenu.classList.remove('show');
                profileDropdown.classList.remove('open');
            }
        });
    }
    
    // Logo interaction with surprise effect
    const logoLink = document.querySelector('.logo-w3-agile h1 a');
    if (logoLink) {
        logoLink.addEventListener('click', function(e) {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
            
            // SURPRISE: Confetti effect on logo click
            createConfetti();
        });
    }
});

// SURPRISE: Initialize all surprise features
function initializeSurprises() {
    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey || e.metaKey) {
            switch(e.key) {
                case '1':
                    e.preventDefault();
                    window.location.href = 'dashboard.php';
                    break;
                case '2':
                    e.preventDefault();
                    window.location.href = 'create-package.php';
                    break;
                case '3':
                    e.preventDefault();
                    window.location.href = 'manage-bookings.php';
                    break;
                case 'h':
                    e.preventDefault();
                    showHelpPanel();
                    break;
            }
        }
    });
    
    // Add mouse trail effect
    let mouseTrail = [];
    document.addEventListener('mousemove', function(e) {
        mouseTrail.push({x: e.clientX, y: e.clientY, time: Date.now()});
        if (mouseTrail.length > 10) mouseTrail.shift();
        
        // Create sparkle effect
        if (Math.random() < 0.1) {
            createSparkle(e.clientX, e.clientY);
        }
    });
}

// SURPRISE: AI Assistant Function
function activateAI() {
    const aiResponses = [
        "Hello! I'm your AI assistant. How can I help you today?",
        "I can help you manage packages, bookings, and more!",
        "Try saying 'Show dashboard' or 'Create package'",
        "Need help? Just ask me anything!",
        "I'm here to make your work easier!"
    ];
    
    const randomResponse = aiResponses[Math.floor(Math.random() * aiResponses.length)];
    
    showAIPanel(randomResponse);
    
    // Add AI glow effect
    const aiButton = document.querySelector('.ai-assistant');
    aiButton.style.animation = 'aiPulse 0.5s ease-in-out';
    setTimeout(() => {
        aiButton.style.animation = 'aiGlow 3s ease-in-out infinite alternate';
    }, 500);
}

// SURPRISE: Voice Commands
let isListening = false;
function toggleVoiceCommands() {
    const voiceIndicator = document.querySelector('.voice-indicator');
    
    if (!isListening) {
        voiceIndicator.classList.add('listening');
        voiceIndicator.innerHTML = '<i class="fa fa-microphone-slash"></i>';
        isListening = true;
        
        // Simulate voice recognition
        setTimeout(() => {
            const commands = [
                'Navigate to dashboard',
                'Create new package',
                'Show bookings',
                'Open analytics'
            ];
            const randomCommand = commands[Math.floor(Math.random() * commands.length)];
            showVoiceResponse(randomCommand);
        }, 2000);
    } else {
        voiceIndicator.classList.remove('listening');
        voiceIndicator.innerHTML = '<i class="fa fa-microphone"></i>';
        isListening = false;
    }
}

// SURPRISE: Quick Actions
function quickAction(action) {
    const actions = {
        'dashboard': () => window.location.href = 'dashboard.php',
        'create': () => window.location.href = 'create-package.php',
        'analytics': () => showAnalyticsPanel()
    };
    
    if (actions[action]) {
        actions[action]();
    }
}

// SURPRISE: Create Confetti Effect
function createConfetti() {
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.style.position = 'fixed';
        confetti.style.left = Math.random() * window.innerWidth + 'px';
        confetti.style.top = '-10px';
        confetti.style.width = '10px';
        confetti.style.height = '10px';
        confetti.style.background = `hsl(${Math.random() * 360}, 70%, 50%)`;
        confetti.style.borderRadius = '50%';
        confetti.style.pointerEvents = 'none';
        confetti.style.zIndex = '10000';
        confetti.style.animation = `confettiFall ${Math.random() * 3 + 2}s linear forwards`;
        
        document.body.appendChild(confetti);
        
        setTimeout(() => confetti.remove(), 5000);
    }
}

// SURPRISE: Create Sparkle Effect
function createSparkle(x, y) {
    const sparkle = document.createElement('div');
    sparkle.style.position = 'fixed';
    sparkle.style.left = x + 'px';
    sparkle.style.top = y + 'px';
    sparkle.style.width = '4px';
    sparkle.style.height = '4px';
    sparkle.style.background = 'white';
    sparkle.style.borderRadius = '50%';
    sparkle.style.pointerEvents = 'none';
    sparkle.style.zIndex = '9999';
    sparkle.style.animation = 'sparkle 1s ease-out forwards';
    
    document.body.appendChild(sparkle);
    
    setTimeout(() => sparkle.remove(), 1000);
}

// SURPRISE: Show AI Panel
function showAIPanel(message) {
    const panel = document.createElement('div');
    panel.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(30, 60, 114, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 30px;
        min-width: 400px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        z-index: 1001;
        animation: slideInScale 0.3s ease;
        color: white;
        text-align: center;
    `;
    
    panel.innerHTML = `
        <div style="font-size: 3rem; margin-bottom: 20px;">🤖</div>
        <h3 style="margin: 0 0 15px 0; font-size: 1.3rem;">AI Assistant</h3>
        <p style="margin: 0 0 20px 0; font-size: 1rem; opacity: 0.9;">${message}</p>
        <button onclick="this.parentElement.remove()" style="
            background: linear-gradient(135deg, #00d4aa, #0099cc);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 1rem;
        ">Got it!</button>
    `;
    
    document.body.appendChild(panel);
    
    setTimeout(() => {
        if (panel.parentElement) {
            panel.remove();
        }
    }, 5000);
}

// SURPRISE: Show Voice Response
function showVoiceResponse(command) {
    const response = document.createElement('div');
    response.style.cssText = `
        position: fixed;
        bottom: 100px;
        right: 30px;
        background: rgba(0, 212, 170, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        z-index: 1001;
        animation: slideInRight 0.3s ease;
        color: white;
        max-width: 300px;
    `;
    
    response.innerHTML = `
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <i class="fa fa-microphone" style="font-size: 1.2rem;"></i>
            <strong>Voice Command</strong>
        </div>
        <p style="margin: 0; font-size: 0.9rem;">"${command}"</p>
    `;
    
    document.body.appendChild(response);
    
    setTimeout(() => {
        if (response.parentElement) {
            response.remove();
        }
    }, 3000);
}

// SURPRISE: Show Analytics Panel
function showAnalyticsPanel() {
    const panel = document.createElement('div');
    panel.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(30, 60, 114, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 30px;
        min-width: 500px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        z-index: 1001;
        animation: slideInScale 0.3s ease;
        color: white;
    `;
    
    panel.innerHTML = `
        <h3 style="margin: 0 0 20px 0; font-size: 1.3rem;">📊 Quick Analytics</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div style="text-align: center;">
                <div style="font-size: 2rem; margin-bottom: 10px;">📈</div>
                <h4 style="margin: 0 0 5px 0;">Bookings</h4>
                <p style="margin: 0; font-size: 1.5rem; color: #00d4aa;">+15%</p>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2rem; margin-bottom: 10px;">💰</div>
                <h4 style="margin: 0 0 5px 0;">Revenue</h4>
                <p style="margin: 0; font-size: 1.5rem; color: #00d4aa;">+23%</p>
            </div>
        </div>
        <button onclick="this.parentElement.remove()" style="
            background: linear-gradient(135deg, #00d4aa, #0099cc);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 1rem;
            margin-top: 20px;
            width: 100%;
        ">Close</button>
    `;
    
    document.body.appendChild(panel);
}

// SURPRISE: Show Help Panel
function showHelpPanel() {
    const panel = document.createElement('div');
    panel.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(30, 60, 114, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 30px;
        min-width: 400px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        z-index: 1001;
        animation: slideInScale 0.3s ease;
        color: white;
    `;
    
    panel.innerHTML = `
        <h3 style="margin: 0 0 20px 0; font-size: 1.3rem;">🎯 Keyboard Shortcuts</h3>
        <div style="margin-bottom: 15px;">
            <strong>Ctrl + 1:</strong> Dashboard
        </div>
        <div style="margin-bottom: 15px;">
            <strong>Ctrl + 2:</strong> Create Package
        </div>
        <div style="margin-bottom: 15px;">
            <strong>Ctrl + 3:</strong> Manage Bookings
        </div>
        <div style="margin-bottom: 20px;">
            <strong>Ctrl + H:</strong> Show Help
        </div>
        <button onclick="this.parentElement.remove()" style="
            background: linear-gradient(135deg, #00d4aa, #0099cc);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 1rem;
        ">Got it!</button>
    `;
    
    document.body.appendChild(panel);
}

// Notification panel function
function showNotificationPanel() {
    const panel = document.createElement('div');
    panel.style.cssText = `
        position: fixed;
        top: 80px;
        right: 30px;
        background: rgba(30, 60, 114, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 20px;
        min-width: 300px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        z-index: 1001;
        animation: slideInRight 0.3s ease;
    `;
    
    panel.innerHTML = `
        <h3 style="color: white; margin: 0 0 15px 0; font-size: 1.1rem;">Notifications</h3>
        <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">
            <p>• New booking received</p>
            <p>• Customer enquiry pending</p>
            <p>• System update available</p>
        </div>
        <button onclick="this.parentElement.remove()" style="
            background: linear-gradient(135deg, #00d4aa, #0099cc);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            margin-top: 15px;
            cursor: pointer;
            font-size: 0.9rem;
        ">Mark All Read</button>
    `;
    
    document.body.appendChild(panel);
    
    setTimeout(() => {
        if (panel.parentElement) {
            panel.remove();
        }
    }, 5000);
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100%);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInScale {
        from {
            opacity: 0;
            transform: translate(-50%, -50%) scale(0.8);
        }
        to {
            opacity: 1;
            transform: translate(-50%, -50%) scale(1);
        }
    }
    
    @keyframes confettiFall {
        to {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }
    
    @keyframes sparkle {
        0% {
            transform: scale(0) rotate(0deg);
            opacity: 1;
        }
        50% {
            transform: scale(1) rotate(180deg);
            opacity: 1;
        }
        100% {
            transform: scale(0) rotate(360deg);
            opacity: 0;
        }
    }
    
    .dropdown-menu.show {
        display: block !important;
    }
`;
document.head.appendChild(style);
</script>