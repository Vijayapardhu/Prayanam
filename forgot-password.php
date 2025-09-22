<?php
session_start();
error_reporting(0);
include('includes/config.php');
if(isset($_POST['submit50']))
	{
$email=$_POST['email'];
$mobile=$_POST['mobile'];
$newpassword=$_POST['newpassword'];
	$sql ="SELECT EmailId FROM tblusers WHERE EmailId=:email and MobileNumber=:mobile";
$query= $dbh -> prepare($sql);
$query-> bindParam(':email', $email, PDO::PARAM_STR);
$query-> bindParam(':mobile', $mobile, PDO::PARAM_STR);
$query-> execute();
$results = $query -> fetchAll(PDO::FETCH_OBJ);
if($query -> rowCount() > 0)
{
$hashed_password = password_hash($newpassword, PASSWORD_DEFAULT);
$con="update tblusers set Password=:newpassword where EmailId=:email and MobileNumber=:mobile";
$chngpwd1 = $dbh->prepare($con);
$chngpwd1-> bindParam(':email', $email, PDO::PARAM_STR);
$chngpwd1-> bindParam(':mobile', $mobile, PDO::PARAM_STR);
$chngpwd1-> bindParam(':newpassword', $hashed_password, PDO::PARAM_STR);
$chngpwd1->execute();
$msg="Your Password succesfully changed";
}
else {
$error="Email id or Mobile no is invalid";	
}
}

?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Travel Management System</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="keywords" content="Prayanam Travel Management System In PHP" />
<script type="applijewelleryion/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<link href="css/bootstrap.css" rel='stylesheet' type='text/css' />
<link href="css/style.css" rel='stylesheet' type='text/css' />
<link href="css/font-awesome.css" rel="stylesheet">
<link href="css/modern-ui.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="js/jquery-1.12.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<link href="css/animate.css" rel="stylesheet" type="text/css" media="all">
<script src="js/wow.min.js"></script>
	<script>
		 new WOW().init();
	</script>
  <style>
/* Forgot Password Specific Styles */
.forgot-password-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.forgot-password-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('images/hero-bg.jpg') center/cover;
    opacity: 0.3;
    z-index: 1;
}

.forgot-password-hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 16px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.forgot-password-hero p {
    font-size: 1.2rem;
    opacity: 0.9;
}

.password-reset-container {
    background: #ffffff;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 600px;
    margin: 50px auto;
}

.password-reset-header {
    text-align: center;
    margin-bottom: 30px;
}

.password-reset-title {
    font-size: 2rem;
    font-weight: 700;
    color: #34495e;
    margin-bottom: 10px;
}

.password-reset-subtitle {
    color: #7f8c8d;
    font-size: 1rem;
}

.form-group {
    margin-bottom: 20px;
    position: relative;
}

.form-label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #34495e;
    font-size: 0.9rem;
}

.form-input {
    width: 100%;
    padding: 12px 15px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.form-input:focus {
    outline: none;
    border-color: #3498db;
}

.password-toggle {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: #7f8c8d;
    cursor: pointer;
    font-size: 1rem;
}

.password-strength {
    margin-top: 10px;
    padding: 8px 12px;
    border-radius: 5px;
    font-size: 0.85rem;
    font-weight: 500;
    display: none;
}

.password-strength.weak {
    background-color: #ffe0e0;
    color: #e74c3c;
}

.password-strength.medium {
    background-color: #fff3cd;
    color: #f39c12;
}

.password-strength.strong {
    background-color: #d4edda;
    color: #28a745;
}

.password-requirements {
    background: #f8f9fa;
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 20px;
    margin-top: 30px;
}

.password-requirements-title {
    font-weight: 600;
    color: #34495e;
    margin-bottom: 15px;
}

.requirement-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.requirement-item {
    display: flex;
    align-items: center;
    margin-bottom: 8px;
    font-size: 0.9rem;
    color: #7f8c8d;
}

.requirement-item.valid {
    color: #28a745;
}

.requirement-item i {
    margin-right: 8px;
    font-size: 0.8rem;
}

.form-actions {
    text-align: center;
    margin-top: 30px;
}

.btn-primary {
    background: linear-gradient(45deg, #3498db, #2980b9);
    color: white;
    padding: 12px 30px;
    border: none;
    border-radius: 25px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

/* Alert Messages */
.alert-modern {
    padding: 16px 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 500;
    animation: fadeInDown 0.5s ease;
}

.alert-modern.success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.alert-modern.error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.alert-modern i {
    font-size: 1.2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .forgot-password-hero h1 {
        font-size: 2.5rem;
    }
    
    .password-reset-container {
        margin: 30px 20px;
        padding: 30px;
    }
}
</style>
</head>
<body>
<!-- top-header -->
<div class="top-header">
<?php include('includes/header.php');?>
<div class="banner-1 ">
	<div class="container">
		<h1 class="wow zoomIn animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: zoomIn;">Forgot Password</h1>
	</div>
</div>
<!--- /banner-1 ---->
<!--- privacy ---->
<div class="privacy">
	<div class="container">
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">Recover Password</h3>
		<div class="password-reset-container">
        <div class="password-reset-header">
            <h2 class="password-reset-title">Reset Your Password</h2>
            <p class="password-reset-subtitle">Enter your registered email and mobile number to reset your password</p>
        </div>

        <?php if($error){?><div class="alert-modern error"><i class="fa fa-exclamation-triangle"></i><span><?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="alert-modern success"><i class="fa fa-check-circle"></i><span><?php echo htmlentities($msg); ?> </div><?php }?>

        <form name="chngpwd" method="post">
            <div class="form-group">
                <label class="form-label">Email ID</label>
                <input type="email" name="email" class="form-input" placeholder="Enter your registered email" required>
            </div>
            <div class="form-group">
                <label class="form-label">Mobile Number</label>
                <input type="text" name="mobile" class="form-input" maxlength="10" placeholder="Enter your registered mobile number" required>
            </div>
            <div class="form-group">
                <label class="form-label">New Password</label>
                <input type="password" name="newpassword" class="form-input" id="newPassword" placeholder="Enter your new password" required>
                <button type="button" class="password-toggle" onclick="togglePassword(this)">
                    <i class="fa fa-eye"></i>
                </button>
                <div class="password-strength" id="passwordStrength"></div>
            </div>
            <div class="form-group">
                <label class="form-label">Confirm New Password</label>
                <input type="password" name="confirmpassword" class="form-input" id="confirmPassword" placeholder="Confirm your new password" required>
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
                <button type="submit" name="submit50" class="btn-primary">Reset Password</button>
            </div>
        </form>
	</div>
		
	</div>
</div>
<!--- /privacy ---->
<!--- footer-top ---->
<!--- /footer-top ---->
<?php include('includes/footer.php');?>
<!-- signup -->
<?php include('includes/signup.php');?>			
<!-- //signu -->
<!-- signin -->
<?php include('includes/signin.php');?>			
<!-- //signin -->
<!-- write us -->
<?php include('includes/write-us.php');?>
</body>
</html>
</head>
<body>
<!-- top-header -->
<div class="top-header">
<?php include('includes/header.php');?>
<div class="banner-1 ">
	<div class="container">
		<h1 class="wow zoomIn animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: zoomIn;">Prayanam - Travel Management System</h1>
	</div>
</div>
<!--- /banner-1 ---->
<!--- privacy ---->
<div class="privacy">
	<div class="container">
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">Recover Password</h3>
		<div class="password-reset-container">
        <div class="password-reset-header">
            <h2 class="password-reset-title">Reset Your Password</h2>
            <p class="password-reset-subtitle">Enter your registered email and mobile number to reset your password</p>
        </div>

        <?php if($error){?><div class="alert-modern error"><i class="fa fa-exclamation-triangle"></i><span><?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="alert-modern success"><i class="fa fa-check-circle"></i><span><?php echo htmlentities($msg); ?> </div><?php }?>

        <form name="chngpwd" method="post">
            <div class="form-group">
                <label class="form-label">Email ID</label>
                <input type="email" name="email" class="form-input" placeholder="Enter your registered email" required>
            </div>
            <div class="form-group">
                <label class="form-label">Mobile Number</label>
                <input type="text" name="mobile" class="form-input" maxlength="10" placeholder="Enter your registered mobile number" required>
            </div>
            <div class="form-group">
                <label class="form-label">New Password</label>
                <input type="password" name="newpassword" class="form-input" id="newPassword" placeholder="Enter your new password" required>
                <button type="button" class="password-toggle" onclick="togglePassword(this)">
                    <i class="fa fa-eye"></i>
                </button>
                <div class="password-strength" id="passwordStrength"></div>
            </div>
            <div class="form-group">
                <label class="form-label">Confirm New Password</label>
                <input type="password" name="confirmpassword" class="form-input" id="confirmPassword" placeholder="Confirm your new password" required>
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
                <button type="submit" name="submit50" class="btn-primary">Reset Password</button>
            </div>
        </form>
	</div>
		
	</div>
</div>
<!--- /privacy ---->
<!--- footer-top ---->
<!--- /footer-top ---->
<?php include('includes/footer.php');?>
<!-- signup -->
<?php include('includes/signup.php');?>			
<!-- //signu -->
<!-- signin -->
<?php include('includes/signin.php');?>			
<!-- //signin -->
<!-- write us -->
<?php include('includes/write-us.php');?>
</body>
</html>