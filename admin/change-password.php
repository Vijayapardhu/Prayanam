<?php
session_start();
$error = '';
$msg = '';
include('includes/config.php');
if(strlen($_SESSION['alogin'])==0)
	{	
header('location:index.php');
}
else{
if(isset($_POST['submit']))
{
$password=$_POST['password'];
$newpassword=$_POST['newpassword'];
$username=$_SESSION['alogin'];
$sql ="SELECT Password FROM admin WHERE UserName=:username and Password=:password";
$query= $dbh -> prepare($sql);
$query-> bindParam(':username', $username, PDO::PARAM_STR);
$query-> bindParam(':password', $password, PDO::PARAM_STR);
$query-> execute();
$results = $query->fetchAll(PDO::FETCH_OBJ);
if($query->rowCount() > 0)
{
$con="update admin set Password=:newpassword where UserName=:username";
$chngpwd1 = $dbh->prepare($con);
$chngpwd1-> bindParam(':username', $username, PDO::PARAM_STR);
$chngpwd1-> bindParam(':newpassword', $newpassword, PDO::PARAM_STR);
$chngpwd1->execute();
$msg="Your Password succesfully changed";
}
else {
$error="Your current password is wrong";	
}
}
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Change Password</title>
		<link rel="icon" type="image/png" href="images/prayanam.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- Bootstrap Core CSS -->
<link href="css/bootstrap.min.css" rel='stylesheet' type='text/css' />
<!-- Custom CSS -->
<link href="css/style.css" rel='stylesheet' type='text/css' />
<link rel="stylesheet" href="css/morris.css" type="text/css"/>
<!-- Graph CSS -->
<link href="css/font-awesome.css" rel="stylesheet"> 
<!-- Modern UI CSS -->
<link href="css/modern-ui.css" rel="stylesheet">
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<!-- jQuery -->
<script src="js/jquery-2.1.4.min.js"></script>
<!-- //jQuery -->
<link href='//fonts.googleapis.com/css?family=Roboto:700,500,300,100italic,100,400' rel='stylesheet' type='text/css'/>
<link href='//fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
<!-- lined-icons -->
<link rel="stylesheet" href="css/icon-font.min.css" type='text/css' />
<!-- //lined-icons -->

<style>
/* Change Password Specific Styles */
.change-password-hero {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    margin-bottom: 32px;
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: slideInDown 0.8s ease;
}

.change-password-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--primary-gradient);
    opacity: 0.1;
    z-index: -1;
}

.change-password-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.change-password-hero p {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 0;
}

.password-form-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    max-width: 600px;
    margin: 0 auto;
    animation: slideInUp 0.8s ease 0.2s both;
}

.password-form-header {
    margin-bottom: 32px;
    text-align: center;
}

.password-form-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 12px;
}

.password-form-subtitle {
    color: var(--text-secondary);
    font-size: 1rem;
}

.form-section {
    margin-bottom: 32px;
}

.form-group {
    margin-bottom: 24px;
    position: relative;
}

.form-label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.form-input {
    width: 100%;
    padding: 16px 20px 16px 50px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-primary);
    font-size: 1rem;
    transition: var(--transition);
    backdrop-filter: blur(10px);
}

.form-input:focus {
    outline: none;
    border-color: #667eea;
    background: rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-input::placeholder {
    color: rgba(255, 255, 255, 0.5);
}

.input-icon {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    font-size: 1.1rem;
    transition: var(--transition);
}

.form-input:focus + .input-icon {
    color: #667eea;
}

.password-toggle {
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    font-size: 1.1rem;
    transition: var(--transition);
}

.password-toggle:hover {
    color: var(--text-primary);
}

.password-strength {
    margin-top: 8px;
    padding: 8px 12px;
    border-radius: var(--border-radius-sm);
    font-size: 0.8rem;
    font-weight: 500;
    display: none;
}

.password-strength.weak {
    background: rgba(255, 107, 107, 0.1);
    color: #ff6b6b;
    border: 1px solid rgba(255, 107, 107, 0.3);
}

.password-strength.medium {
    background: rgba(255, 193, 7, 0.1);
    color: #ffc107;
    border: 1px solid rgba(255, 193, 7, 0.3);
}

.password-strength.strong {
    background: rgba(67, 233, 123, 0.1);
    color: #43e97b;
    border: 1px solid rgba(67, 233, 123, 0.3);
}

.password-requirements {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    padding: 16px;
    margin-bottom: 24px;
}

.password-requirements-title {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.requirement-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.requirement-item {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.requirement-item.valid {
    color: #43e97b;
}

.requirement-item.valid i {
    color: #43e97b;
}

.requirement-item i {
    font-size: 0.8rem;
    width: 16px;
    text-align: center;
}

.form-actions {
    display: flex;
    gap: 16px;
    justify-content: center;
    margin-top: 32px;
}

.btn-modern {
    padding: 16px 32px;
    border: none;
    border-radius: var(--border-radius-sm);
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    position: relative;
    overflow: hidden;
}

.btn-modern::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.btn-modern:hover::before {
    left: 100%;
}

.btn-modern.primary {
    background: var(--primary-gradient);
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.btn-modern.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.btn-modern.secondary {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
}

.btn-modern.secondary:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: translateY(-2px);
}

/* Alert Messages */
.alert-modern {
    padding: 16px 20px;
    border-radius: var(--border-radius-sm);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 500;
    animation: slideInDown 0.5s ease;
}

.alert-modern.success {
    background: var(--success-gradient);
    color: white;
    box-shadow: 0 4px 15px rgba(67, 233, 123, 0.3);
}

.alert-modern.error {
    background: var(--accent-gradient);
    color: white;
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
}

.alert-modern i {
    font-size: 1.2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .change-password-hero h1 {
        font-size: 2rem;
    }
    
    .password-form-container {
        padding: 24px;
        margin: 0 20px;
    }
    
    .form-actions {
        flex-direction: column;
    }
    
    .change-password-hero {
        padding: 24px;
    }
}

/* Loading State */
.btn-modern.loading {
    pointer-events: none;
    opacity: 0.8;
}

.btn-modern.loading::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    margin: -10px 0 0 -10px;
    border: 2px solid transparent;
    border-top: 2px solid currentColor;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>

</head> 
<body>
   <div class="page-container">
   <!--/content-inner-->
<div class="left-content">
	   <div class="mother-grid-inner">
<!--header start here-->
<?php include('includes/header.php');?>
<!--header end here-->

<div class="dashboard-content">
    <!-- Breadcrumb -->
    <div class="breadcrumb-modern">
        <a href="dashboard.php" class="breadcrumb-item">Dashboard</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-item active">Change Password</span>
    </div>

    <!-- Hero Section -->
    <div class="change-password-hero">
        <h1>Change Password</h1>
        <p>Update your account password to keep it secure</p>
    </div>

    <!-- Password Form Container -->
    <div class="password-form-container">
        <div class="password-form-header">
            <h2 class="password-form-title">Update Password</h2>
            <p class="password-form-subtitle">Enter your current password and choose a new one</p>
        </div>

        <?php if($error){?>
            <div class="alert-modern error">
                <i class="fa fa-exclamation-triangle"></i>
                <span><?php echo htmlentities($error); ?></span>
            </div>
        <?php } else if($msg){?>
            <div class="alert-modern success">
                <i class="fa fa-check-circle"></i>
                <span><?php echo htmlentities($msg); ?></span>
            </div>
        <?php }?>

        <form method="post" class="form-section">
            <div class="form-group">
                <label class="form-label">Current Password</label>
                <input type="password" name="password" class="form-input" placeholder="Enter your current password" required>
                <i class="fa fa-lock input-icon"></i>
                <button type="button" class="password-toggle" onclick="togglePassword(this)">
                    <i class="fa fa-eye"></i>
                </button>
            </div>

            <div class="form-group">
                <label class="form-label">New Password</label>
                <input type="password" name="newpassword" class="form-input" id="newPassword" placeholder="Enter your new password" required>
                <i class="fa fa-key input-icon"></i>
                <button type="button" class="password-toggle" onclick="togglePassword(this)">
                    <i class="fa fa-eye"></i>
                </button>
                <div class="password-strength" id="passwordStrength"></div>
            </div>

            <div class="form-group">
                <label class="form-label">Confirm New Password</label>
                <input type="password" name="confirmpassword" class="form-input" id="confirmPassword" placeholder="Confirm your new password" required>
                <i class="fa fa-check input-icon"></i>
                <button type="button" class="password-toggle" onclick="togglePassword(this)">
                    <i class="fa fa-eye"></i>
                </button>
            </div>

            <!-- Password Requirements -->
            <div class="password-requirements">
                <div class="password-requirements-title">
                    <i class="fa fa-shield"></i>
                    Password Requirements
                </div>
                <ul class="requirement-list">
                    <li class="requirement-item" id="req-length">
                        <i class="fa fa-circle"></i>
                        At least 8 characters long
                    </li>
                    <li class="requirement-item" id="req-uppercase">
                        <i class="fa fa-circle"></i>
                        Contains uppercase letter
                    </li>
                    <li class="requirement-item" id="req-lowercase">
                        <i class="fa fa-circle"></i>
                        Contains lowercase letter
                    </li>
                    <li class="requirement-item" id="req-number">
                        <i class="fa fa-circle"></i>
                        Contains number
                    </li>
                    <li class="requirement-item" id="req-special">
                        <i class="fa fa-circle"></i>
                        Contains special character
                    </li>
                </ul>
            </div>

            <div class="form-actions">
                <button type="button" class="btn-modern secondary" onclick="window.history.back()">
                    <i class="fa fa-arrow-left"></i>
                    Cancel
                </button>
                <button type="submit" name="submit" class="btn-modern primary" id="submitBtn">
                    <i class="fa fa-save"></i>
                    Update Password
                </button>
            </div>
        </form>
    </div>
</div>

<!--copy rights start here-->
<?php include('includes/footer.php');?>
</div>
</div>

			<!--/sidebar-menu-->
				<?php include('includes/sidebarmenu.php');?>
							  <div class="clearfix"></div>		
							</div>
							<script>
							var toggle = true;
										
							$(".sidebar-icon").click(function() {                
							  if (toggle)
							  {
								$(".page-container").addClass("sidebar-collapsed").removeClass("sidebar-collapsed-back");
								$("#menu span").css({"position":"absolute"});
							  }
							  else
							  {
								$(".page-container").removeClass("sidebar-collapsed").addClass("sidebar-collapsed-back");
								setTimeout(function() {
								  $("#menu span").css({"position":"relative"});
								}, 400);
							  }
											
											toggle = !toggle;
										});
							</script>
<!--js -->
<script src="js/jquery.nicescroll.js"></script>
<script src="js/scripts.js"></script>
<!-- Bootstrap Core JavaScript -->
   <script src="js/bootstrap.min.js"></script>
   <!-- /Bootstrap Core JavaScript -->	   
<script>
$(document).ready(function() {
    // Password strength checker
    $('#newPassword').on('input', function() {
        const password = $(this).val();
        checkPasswordStrength(password);
    });
    
    // Confirm password checker
    $('#confirmPassword').on('input', function() {
        const newPassword = $('#newPassword').val();
        const confirmPassword = $(this).val();
        
        if (confirmPassword && newPassword !== confirmPassword) {
            $(this).css('border-color', '#ff6b6b');
            showAlert('Passwords do not match', 'error');
        } else {
            $(this).css('border-color', 'var(--border-color)');
        }
    });
    
    // Form submission with loading state
    $('form').on('submit', function(e) {
        const newPassword = $('#newPassword').val();
        const confirmPassword = $('#confirmPassword').val();
        
        if (newPassword !== confirmPassword) {
            e.preventDefault();
            showAlert('Passwords do not match', 'error');
            return false;
        }
        
        if (!isPasswordStrong(newPassword)) {
            e.preventDefault();
            showAlert('Password does not meet requirements', 'error');
            return false;
        }
        
        const btn = $('#submitBtn');
        const btnText = btn.find('i').next();
        
        // Add loading state
        btn.addClass('loading');
        btnText.text('Updating...');
        
        // Simulate loading time
        setTimeout(() => {
            btn.removeClass('loading');
            btnText.text('Update Password');
            
            // Show success message
            showAlert('Password updated successfully!', 'success');
        }, 2000);
    });
});

// Toggle password visibility
function togglePassword(button) {
    const input = $(button).siblings('input');
    const icon = $(button).find('i');
    
    if (input.attr('type') === 'password') {
        input.attr('type', 'text');
        icon.removeClass('fa-eye').addClass('fa-eye-slash');
    } else {
        input.attr('type', 'password');
        icon.removeClass('fa-eye-slash').addClass('fa-eye');
    }
}

// Check password strength
function checkPasswordStrength(password) {
    const requirements = {
        length: password.length >= 8,
        uppercase: /[A-Z]/.test(password),
        lowercase: /[a-z]/.test(password),
        number: /\d/.test(password),
        special: /[!@#$%^&*(),.?":{}|<>]/.test(password)
    };
    
    // Update requirement indicators
    $('#req-length').toggleClass('valid', requirements.length);
    $('#req-uppercase').toggleClass('valid', requirements.uppercase);
    $('#req-lowercase').toggleClass('valid', requirements.lowercase);
    $('#req-number').toggleClass('valid', requirements.number);
    $('#req-special').toggleClass('valid', requirements.special);
    
    // Calculate strength
    const validCount = Object.values(requirements).filter(Boolean).length;
    const strengthElement = $('#passwordStrength');
    
    if (password.length === 0) {
        strengthElement.hide();
        return;
    }
    
    strengthElement.show();
    
    if (validCount <= 2) {
        strengthElement.removeClass('medium strong').addClass('weak').text('Weak Password');
    } else if (validCount <= 4) {
        strengthElement.removeClass('weak strong').addClass('medium').text('Medium Password');
    } else {
        strengthElement.removeClass('weak medium').addClass('strong').text('Strong Password');
    }
}

// Check if password meets all requirements
function isPasswordStrong(password) {
    const requirements = {
        length: password.length >= 8,
        uppercase: /[A-Z]/.test(password),
        lowercase: /[a-z]/.test(password),
        number: /\d/.test(password),
        special: /[!@#$%^&*(),.?":{}|<>]/.test(password)
    };
    
    return Object.values(requirements).every(Boolean);
}

// Show alert function
function showAlert(message, type) {
    const alert = $(`
        <div class="alert-modern ${type} animate-slide-in-down">
            <i class="fa fa-${type === 'success' ? 'check-circle' : 'exclamation-triangle'}"></i>
            <span>${message}</span>
        </div>
    `);
    
    $('.password-form-container').prepend(alert);
    
    setTimeout(() => {
        alert.fadeOut(300, function() {
            $(this).remove();
        });
    }, 5000);
}

// Auto-save functionality
let autoSaveTimer;
$('input').on('input', function() {
    clearTimeout(autoSaveTimer);
    autoSaveTimer = setTimeout(() => {
        // Auto-save logic here
        console.log('Auto-saving password form...');
    }, 3000);
});

// Keyboard shortcuts
$(document).on('keydown', function(e) {
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        $('#submitBtn').click();
    }
});
</script>
</body>
</html>
<?php } ?>