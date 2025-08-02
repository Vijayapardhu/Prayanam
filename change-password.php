<?php
session_start();
error_reporting(0);
include('includes/config.php');
if(strlen($_SESSION['login'])==0)
	{	
header('location:index.php');
}
else{
if(isset($_POST['submit5']))
	{
$password=$_POST['password'];
$newpassword=$_POST['newpassword'];
$email=$_SESSION['login'];
	$sql ="SELECT Password FROM tblusers WHERE EmailId=:email";
$query= $dbh -> prepare($sql);
$query-> bindParam(':email', $email, PDO::PARAM_STR);
$query-> execute();
$results = $query -> fetchAll(PDO::FETCH_OBJ);
if($query -> rowCount() > 0)
{
    foreach ($results as $result) {
        if (password_verify($password, $result->Password)) {
            $hashed_password = password_hash($newpassword, PASSWORD_DEFAULT);
            $con="update tblusers set Password=:newpassword where EmailId=:email";
            $chngpwd1 = $dbh->prepare($con);
            $chngpwd1-> bindParam(':email', $email, PDO::PARAM_STR);
            $chngpwd1-> bindParam(':newpassword', $hashed_password, PDO::PARAM_STR);
            $chngpwd1->execute();
            $msg="Your Password succesfully changed";
        } else {
            $error="Your current password is wrong";	
        }
    }
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
/* Change Password Specific Styles */
.change-password-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.change-password-hero::before {
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

.change-password-hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 16px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.change-password-hero p {
    font-size: 1.2rem;
    opacity: 0.9;
}

.password-form-container {
    background: #ffffff;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 600px;
    margin: 50px auto;
}

.password-form-header {
    text-align: center;
    margin-bottom: 30px;
}

.password-form-title {
    font-size: 2rem;
    font-weight: 700;
    color: #34495e;
    margin-bottom: 10px;
}

.password-form-subtitle {
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

/* Responsive Design */
@media (max-width: 768px) {
    .change-password-hero h1 {
        font-size: 2.5rem;
    }
    
    .password-form-container {
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
		<h1 class="wow zoomIn animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: zoomIn;">Change Password</h1>
	</div>
</div>
<!--- /banner-1 ---->
<!--- privacy ---->
<div class="privacy">
	<div class="container">
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">Change Password</h3>
		<div class="password-form-container">
        <div class="password-form-header">
            <h2 class="password-form-title">Update Password</h2>
            <p class="password-form-subtitle">Enter your current password and choose a new one</p>
        </div>

        <?php if($error){?><div class="alert-modern error"><i class="fa fa-exclamation-triangle"></i><span><?php echo htmlentities($error); ?></span></div><?php } else if($msg){?><div class="alert-modern success"><i class="fa fa-check-circle"></i><span><?php echo htmlentities($msg); ?></span></div><?php }?>

        <form method="post" class="form-section" name="chngpwd">
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
                <button type="submit" name="submit5" class="btn-modern primary" id="submitBtn">
                    <i class="fa fa-save"></i>
                    Update Password
                </button>
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
<?php } ?>
</head>
<body>
<!-- BODY_PLACEHOLDER -->
</body>
</html>
<?php } ?>