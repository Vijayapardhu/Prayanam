<?php
session_start();
include('includes/config.php');
if(isset($_POST['login']))
{
$uname=$_POST['username'];
$password=md5($_POST['password']);
$sql ="SELECT UserName,Password FROM admin WHERE UserName=:uname and Password=:password";
$query= $dbh -> prepare($sql);
$query-> bindParam(':uname', $uname, PDO::PARAM_STR);
$query-> bindParam(':password', $password, PDO::PARAM_STR);
$query-> execute();
$results=$query->fetchAll(PDO::FETCH_OBJ);
if($query->rowCount() > 0)
{
$_SESSION['alogin']=$_POST['username'];
echo "<script type='text/javascript'> document.location = 'dashboard.php'; </script>";
} else{
	
	echo "<script>alert('Invalid Details');</script>";

}

}

?>

<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Admin Sign in</title>
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
<link rel="stylesheet" href="css/jquery-ui.css"> 
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
/* Login Page Specific Styles */
body {
    background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 50%, #2d3748 100%);
    font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

/* Animated Background */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 80%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(0, 212, 170, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(255, 107, 107, 0.05) 0%, transparent 50%);
    animation: backgroundFloat 20s ease-in-out infinite;
    z-index: -1;
}

@keyframes backgroundFloat {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(-10px, -10px) scale(1.1); }
    66% { transform: translate(10px, 10px) scale(0.9); }
}

/* Floating Elements */
.floating-element {
    position: fixed;
    width: 100px;
    height: 100px;
    background: var(--primary-gradient);
    border-radius: 50%;
    opacity: 0.1;
    animation: float 6s ease-in-out infinite;
    pointer-events: none;
    z-index: -1;
}

.floating-element:nth-child(1) {
    top: 10%;
    left: 10%;
    animation-delay: 0s;
}

.floating-element:nth-child(2) {
    top: 20%;
    right: 10%;
    animation-delay: 2s;
}

.floating-element:nth-child(3) {
    bottom: 20%;
    left: 15%;
    animation-delay: 4s;
}

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
}

.login-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 48px;
    width: 100%;
    max-width: 450px;
    box-shadow: var(--shadow-heavy);
    position: relative;
    overflow: hidden;
    animation: slideInUp 0.8s ease;
}

.login-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.6s ease;
}

.login-container:hover::before {
    left: 100%;
}

.login-header {
    text-align: center;
    margin-bottom: 40px;
}

.login-logo {
    width: 80px;
    height: 80px;
    border-radius: var(--border-radius-sm);
    margin: 0 auto 24px;
    filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));
    animation: logoFloat 3s ease-in-out infinite;
}

@keyframes logoFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.login-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 12px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.login-subtitle {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 0;
}

.login-form {
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

.login-btn {
    width: 100%;
    padding: 16px 24px;
    background: var(--primary-gradient);
    color: white;
    border: none;
    border-radius: var(--border-radius-sm);
    font-weight: 600;
    font-size: 1.1rem;
    cursor: pointer;
    transition: var(--transition);
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.login-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.login-btn:hover::before {
    left: 100%;
}

.login-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.login-btn:active {
    transform: translateY(0);
}

.back-link {
    text-align: center;
    margin-top: 24px;
}

.back-link a {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.back-link a:hover {
    color: var(--text-primary);
    transform: translateX(-4px);
}

/* Error Animation */
.error-shake {
    animation: shake 0.5s ease-in-out;
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
}

/* Loading State */
.login-btn.loading {
    pointer-events: none;
    opacity: 0.8;
}

.login-btn.loading::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    margin: -10px 0 0 -10px;
    border: 2px solid transparent;
    border-top: 2px solid white;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Responsive Design */
@media (max-width: 768px) {
    .login-container {
        margin: 20px;
        padding: 32px;
    }
    
    .login-title {
        font-size: 2rem;
    }
    
    .login-subtitle {
        font-size: 1rem;
    }
    
    .login-logo {
        width: 60px;
        height: 60px;
    }
}

/* Success Animation */
.success-checkmark {
    display: none;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #00d4aa;
    font-size: 2rem;
    animation: checkmark 0.5s ease-in-out;
}

@keyframes checkmark {
    0% { transform: translate(-50%, -50%) scale(0); }
    50% { transform: translate(-50%, -50%) scale(1.2); }
    100% { transform: translate(-50%, -50%) scale(1); }
}
</style>

</head> 
<body>
<!-- Floating Background Elements -->
<div class="floating-element"></div>
<div class="floating-element"></div>
<div class="floating-element"></div>

<div class="login-container">
    <div class="login-header">
        <img src="images/prayanam.png" alt="Prayanam" class="login-logo">
        <h1 class="login-title">Welcome Back</h1>
        <p class="login-subtitle">Sign in to your Prayanam Admin Panel</p>
    </div>
    
    <form method="post" class="login-form" id="loginForm">
        <div class="form-group">
            <label class="form-label">Username</label>
            <input type="text" name="username" class="form-input" placeholder="Enter your username" required>
            <i class="fa fa-user input-icon"></i>
        </div>
        
        <div class="form-group">
            <label class="form-label">Password</label>
            <input type="password" name="password" class="form-input" placeholder="Enter your password" required>
            <i class="fa fa-lock input-icon"></i>
        </div>
        
        <button type="submit" name="login" class="login-btn" id="loginBtn">
            <span class="btn-text">Sign In</span>
            <i class="fa fa-check success-checkmark" id="successCheck"></i>
        </button>
    </form>
    
    <div class="back-link">
        <a href="../index.php">
            <i class="fa fa-arrow-left"></i>
            Back to Home
        </a>
    </div>
</div>

<script>
$(document).ready(function() {
    // Form submission with animation
    $('#loginForm').on('submit', function(e) {
        const btn = $('#loginBtn');
        const btnText = $('.btn-text');
        const successCheck = $('#successCheck');
        
        // Add loading state
        btn.addClass('loading');
        btnText.text('Signing In...');
        
        // Simulate loading time
        setTimeout(() => {
            btn.removeClass('loading');
            btnText.text('Success!');
            successCheck.show();
            
            // Redirect after success animation
            setTimeout(() => {
                // Form will submit normally
            }, 1000);
        }, 1500);
    });
    
    // Input focus effects
    $('.form-input').focus(function() {
        $(this).parent().addClass('focused');
    }).blur(function() {
        $(this).parent().removeClass('focused');
    });
    
    // Add hover effects to form inputs
    $('.form-input').hover(
        function() {
            $(this).css('border-color', 'rgba(255, 255, 255, 0.3)');
        },
        function() {
            if (!$(this).is(':focus')) {
                $(this).css('border-color', 'var(--border-color)');
            }
        }
    );
    
    // Add keyboard shortcuts
    $(document).on('keydown', function(e) {
        if (e.key === 'Enter' && !$('#loginBtn').hasClass('loading')) {
            $('#loginForm').submit();
        }
    });
    
    // Add form validation feedback
    $('.form-input').on('input', function() {
        if ($(this).val().length > 0) {
            $(this).css('border-color', 'rgba(0, 212, 170, 0.3)');
        } else {
            $(this).css('border-color', 'var(--border-color)');
        }
    });
});

// Add CSS for focused state
const style = document.createElement('style');
style.textContent = `
    .form-group.focused .form-label {
        color: #667eea;
    }
    
    .form-group.focused .input-icon {
        color: #667eea;
    }
`;
document.head.appendChild(style);
</script>
</body>
</html>