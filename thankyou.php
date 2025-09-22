<?php
session_start();
error_reporting(0);
include('includes/config.php');
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Confirmation </title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
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
/* Thank You Page Specific Styles */
.thankyou-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.thankyou-hero::before {
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

.thankyou-hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 16px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.thankyou-hero p {
    font-size: 1.2rem;
    opacity: 0.9;
}

.thankyou-content-section {
    background: #ffffff;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 800px;
    margin: 50px auto;
    text-align: center;
}

.thankyou-icon {
    font-size: 4rem;
    color: #28a745;
    margin-bottom: 20px;
    animation: bounceIn 0.8s ease-out;
}

.thankyou-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 15px;
}

.thankyou-message {
    font-size: 1.1rem;
    color: #34495e;
    line-height: 1.6;
    margin-bottom: 30px;
}

.back-home-btn {
    background: linear-gradient(45deg, #3498db, #2980b9);
    color: white;
    padding: 12px 30px;
    border: none;
    border-radius: 25px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.back-home-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    color: white;
    text-decoration: none;
}

/* Responsive Design */
@media (max-width: 768px) {
    .thankyou-hero h1 {
        font-size: 2.5rem;
    }
    
    .thankyou-content-section {
        margin: 30px 20px;
        padding: 30px;
    }
    
    .thankyou-title {
        font-size: 2rem;
    }
    
    .thankyou-icon {
        font-size: 3rem;
    }
}
</style>
</head>
<body>
<?php include('includes/header.php');?>

<!-- Thank You Hero Section -->
<div class="thankyou-hero">
    <div class="container">
        <h1 class="wow zoomIn" data-wow-delay="0.3s">Thank You!</h1>
        <p class="wow fadeInUp" data-wow-delay="0.5s">Your request has been successfully processed.</p>
    </div>
</div>

<!-- Thank You Content Section -->
<div class="thankyou-content-section wow fadeInUp" data-wow-delay="0.7s">
    <i class="fa fa-check-circle thankyou-icon"></i>
    <h2 class="thankyou-title">Success!</h2>
    <p class="thankyou-message">
        <?php echo htmlentities($_SESSION['msg']);?>
    </p>
    <a href="index.php" class="back-home-btn">Back to Home</a>
</div>

<?php include('includes/footer.php');?>
<!-- signup -->
<?php include('includes/signup.php');?>	
<!-- signin -->
<?php include('includes/signin.php');?>	
<!-- //signin -->
<!-- write us -->
<?php include('includes/write-us.php');?>	
<!-- //write us -->
</body>
</html>
<!--//end-animate-->
</head>
<body>
<?php include('includes/header.php');?>
<div class="banner-1 ">
	<div class="container">
		<h1 class="wow zoomIn animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: zoomIn;"> Prayanam - Travel Management System</h1>
	</div>
</div>
<!--- /banner-1 ---->
<!--- contact ---->
<div class="contact">
	<div class="container">
	<h3> Confirmation</h3>
		<div class="col-md-10 contact-left">
			<div class="con-top animated wow fadeInUp animated" data-wow-duration="1200ms" data-wow-delay="500ms" style="visibility: visible; animation-duration: 1200ms; animation-delay: 500ms; animation-name: fadeInUp;">
	

              <h4>  <?php echo htmlentities($_SESSION['msg']);?></h4>
            
			</div>
		
			<div class="clearfix"></div>
	</div>
</div>
<!--- /contact ---->
<?php include('includes/footer.php');?>
<!-- sign -->
<?php include('includes/signup.php');?>	
<!-- signin -->
<?php include('includes/signin.php');?>	
<!-- //signin -->
<!-- write us -->
<?php include('includes/write-us.php');?>	
<!-- //write us -->
</body>
</html>