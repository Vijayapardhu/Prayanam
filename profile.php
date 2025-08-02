<?php
session_start();
error_reporting(0);
include('includes/config.php');
if(strlen($_SESSION['login'])==0)
	{	
header('location:index.php');
}
else{
if(isset($_POST['submit6']))
	{
$name=$_POST['name'];
$mobileno=$_POST['mobileno'];
$email=$_SESSION['login'];

$sql="update tblusers set FullName=:name,MobileNumber=:mobileno where EmailId=:email";
$query = $dbh->prepare($sql);
$query->bindParam(':name',$name,PDO::PARAM_STR);
$query->bindParam(':mobileno',$mobileno,PDO::PARAM_STR);
$query->bindParam(':email',$email,PDO::PARAM_STR);
$query->execute();
$msg="Profile Updated Successfully";
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
/* Profile Page Specific Styles */
.profile-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.profile-hero::before {
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

.profile-hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 16px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.profile-hero p {
    font-size: 1.2rem;
    opacity: 0.9;
}

.profile-form-container {
    background: #ffffff;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 700px;
    margin: 50px auto;
}

.profile-form-header {
    text-align: center;
    margin-bottom: 30px;
}

.profile-form-title {
    font-size: 2rem;
    font-weight: 700;
    color: #34495e;
    margin-bottom: 10px;
}

.profile-form-subtitle {
    color: #7f8c8d;
    font-size: 1rem;
}

.form-group {
    margin-bottom: 20px;
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
    .profile-hero h1 {
        font-size: 2.5rem;
    }
    
    .profile-form-container {
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
		<h1 class="wow zoomIn animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: zoomIn;">User Profile</h1>
	</div>
</div>
<!--- /banner-1 ---->
<!--- privacy ---->
<div class="privacy">
	<div class="container">
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">My Profile</h3>
		<div class="profile-form-container">
        <div class="profile-form-header">
            <h2 class="profile-form-title">Update Your Profile</h2>
            <p class="profile-form-subtitle">Keep your personal information up to date</p>
        </div>

        <?php if($error){?><div class="alert-modern error"><i class="fa fa-exclamation-triangle"></i><span><?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="alert-modern success"><i class="fa fa-check-circle"></i><span><?php echo htmlentities($msg); ?> </div><?php }?>

        <form name="chngpwd" method="post">
            <?php 
            $useremail=$_SESSION['login'];
            $sql = "SELECT * from tblusers where EmailId=:useremail";
            $query = $dbh -> prepare($sql);
            $query -> bindParam(':useremail',$useremail, PDO::PARAM_STR);
            $query->execute();
            $results=$query->fetchAll(PDO::FETCH_OBJ);
            $cnt=1;
            if($query->rowCount() > 0)
            {
            foreach($results as $result)
            {	?>
            <div class="form-group">
                <label class="form-label">Full Name</label>
                <input type="text" name="name" value="<?php echo htmlentities($result->FullName);?>" class="form-input" required>
            </div> 

            <div class="form-group">
                <label class="form-label">Mobile Number</label>
                <input type="text" class="form-input" name="mobileno" maxlength="10" value="<?php echo htmlentities($result->MobileNumber);?>" required>
            </div>

            <div class="form-group">
                <label class="form-label">Email Id</label>
                <input type="email" class="form-input" name="email" value="<?php echo htmlentities($result->EmailId);?>" readonly>
            </div>
            
            <div class="form-group">
                <label class="form-label">Last Updation Date</label>
                <input type="text" class="form-input" value="<?php echo htmlentities($result->UpdationDate);?>" readonly>
            </div>

            <div class="form-group">	
                <label class="form-label">Registration Date</label>
                <input type="text" class="form-input" value="<?php echo htmlentities($result->RegDate);?>" readonly>
            </div>
            <?php }} ?>

            <div class="form-actions">
                <button type="submit" name="submit6" class="btn-primary">Update Profile</button>
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
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">My Profile</h3>
		<div class="profile-form-container">
        <div class="profile-form-header">
            <h2 class="profile-form-title">Update Your Profile</h2>
            <p class="profile-form-subtitle">Keep your personal information up to date</p>
        </div>

        <?php if($error){?><div class="alert-modern error"><i class="fa fa-exclamation-triangle"></i><span><?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="alert-modern success"><i class="fa fa-check-circle"></i><span><?php echo htmlentities($msg); ?> </div><?php }?>

        <form name="chngpwd" method="post">
            <?php 
            $useremail=$_SESSION['login'];
            $sql = "SELECT * from tblusers where EmailId=:useremail";
            $query = $dbh -> prepare($sql);
            $query -> bindParam(':useremail',$useremail, PDO::PARAM_STR);
            $query->execute();
            $results=$query->fetchAll(PDO::FETCH_OBJ);
            $cnt=1;
            if($query->rowCount() > 0)
            {
            foreach($results as $result)
            {	?>
            <div class="form-group">
                <label class="form-label">Full Name</label>
                <input type="text" name="name" value="<?php echo htmlentities($result->FullName);?>" class="form-input" required>
            </div> 

            <div class="form-group">
                <label class="form-label">Mobile Number</label>
                <input type="text" class="form-input" name="mobileno" maxlength="10" value="<?php echo htmlentities($result->MobileNumber);?>" required>
            </div>

            <div class="form-group">
                <label class="form-label">Email Id</label>
                <input type="email" class="form-input" name="email" value="<?php echo htmlentities($result->EmailId);?>" readonly>
            </div>
            
            <div class="form-group">
                <label class="form-label">Last Updation Date</label>
                <input type="text" class="form-input" value="<?php echo htmlentities($result->UpdationDate);?>" readonly>
            </div>

            <div class="form-group">	
                <label class="form-label">Registration Date</label>
                <input type="text" class="form-input" value="<?php echo htmlentities($result->RegDate);?>" readonly>
            </div>
            <?php }} ?>

            <div class="form-actions">
                <button type="submit" name="submit6" class="btn-primary">Update Profile</button>
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