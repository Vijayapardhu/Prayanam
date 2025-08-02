<?php
session_start();
error_reporting(0);
include('includes/config.php');
if(isset($_POST['submit2']))
{
$pid=intval($_GET['pkgid']);
$useremail=$_SESSION['login'];
$fromdate=$_POST['fromdate'];
$todate=$_POST['todate'];
$comment=$_POST['comment'];
$status=0;
$sql="INSERT INTO tblbooking(PackageId,UserEmail,FromDate,ToDate,Comment,status) VALUES(:pid,:useremail,:fromdate,:todate,:comment,:status)";
$query = $dbh->prepare($sql);
$query->bindParam(':pid',$pid,PDO::PARAM_STR);
$query->bindParam(':useremail',$useremail,PDO::PARAM_STR);
$query->bindParam(':fromdate',$fromdate,PDO::PARAM_STR);
$query->bindParam(':todate',$todate,PDO::PARAM_STR);
$query->bindParam(':comment',$comment,PDO::PARAM_STR);
$query->bindParam(':status',$status,PDO::PARAM_STR);
$query->execute();
$lastInsertId = $dbh->lastInsertId();
if($lastInsertId)
{
$msg="Booked Successfully";
}
else 
{
$error="Something went wrong. Please try again";
}

}
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Package Details</title>
		<link rel="icon" type="image/png" href="admin/images/prayanam.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="applijewelleryion/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<link href="css/bootstrap.css" rel='stylesheet' type='text/css' />
<link href="css/style.css" rel='stylesheet' type='text/css' />
<link href='//fonts.googleapis.com/css?family=Open+Sans:400,700,600' rel='stylesheet' type='text/css'>
<link href='//fonts.googleapis.com/css?family=Roboto+Condensed:400,700,300' rel='stylesheet' type='text/css'>
<link href='//fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
<link href="css/font-awesome.css" rel="stylesheet">
<!-- Custom Theme files -->
<script src="js/jquery-1.12.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<!--animate-->
<link href="css/animate.css" rel="stylesheet" type="text/css" media="all">
<script src="js/wow.min.js"></script>
<link rel="stylesheet" href="css/jquery-ui.css" />
	<script>
		 new WOW().init();
	</script>
<script src="js/jquery-ui.js"></script>
					<script>
						$(function() {
						$( "#datepicker,#datepicker1" ).datepicker();
						});
					</script>
<style>
/* Modern Package Details Styles */
.page-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 60px 0;
    text-align: center;
    position: relative;
}

.page-header::before {
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

.page-header-content {
    position: relative;
    z-index: 2;
}

.page-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.package-details-section {
    padding: 60px 0;
    background: #f8f9fa;
}

.package-main {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 30px rgba(0,0,0,0.1);
    margin-bottom: 40px;
}

.package-image-section {
    position: relative;
    height: 400px;
    overflow: hidden;
}

.package-image-section img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.package-info {
    padding: 40px;
}

.package-name {
    font-size: 2.2rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 10px;
}

.package-id {
    color: #7f8c8d;
    font-size: 0.9rem;
    margin-bottom: 20px;
}

.package-meta {
    display: flex;
    gap: 30px;
    margin-bottom: 30px;
    flex-wrap: wrap;
}

.meta-item {
    display: flex;
    align-items: center;
    gap: 10px;
}

.meta-icon {
    width: 40px;
    height: 40px;
    background: #e8f4fd;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #3498db;
}

.meta-text {
    color: #34495e;
    font-weight: 500;
}

.package-features {
    background: #f8f9fa;
    padding: 25px;
    border-radius: 10px;
    margin-bottom: 30px;
}

.features-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 15px;
}

.features-text {
    color: #34495e;
    line-height: 1.6;
}

.package-description {
    margin-bottom: 40px;
}

.description-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 20px;
}

.description-text {
    color: #34495e;
    line-height: 1.8;
    font-size: 1rem;
}

.booking-section {
    background: white;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 5px 30px rgba(0,0,0,0.1);
    position: sticky;
    top: 20px;
}

.booking-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 30px;
    text-align: center;
}

.booking-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.form-label {
    font-weight: 600;
    color: #2c3e50;
    font-size: 0.9rem;
}

.form-input {
    padding: 12px 15px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    font-size: 14px;
    transition: all 0.3s ease;
}

.form-input:focus {
    border-color: #3498db;
    outline: none;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.date-inputs {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}

.package-price {
    background: linear-gradient(45deg, #e74c3c, #c0392b);
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin: 20px 0;
}

.price-label {
    font-size: 0.9rem;
    opacity: 0.9;
    margin-bottom: 5px;
}

.price-amount {
    font-size: 2rem;
    font-weight: 700;
}

.book-btn {
    background: linear-gradient(45deg, #3498db, #2980b9);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 25px;
    font-weight: 600;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
}

.book-btn:hover {
    background: linear-gradient(45deg, #2980b9, #1f5f8b);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.login-prompt {
    text-align: center;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
    margin-top: 20px;
}

.login-prompt p {
    color: #7f8c8d;
    margin-bottom: 15px;
}

.alert {
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    border: none;
}

.alert-success {
    background: #d4edda;
    color: #155724;
    border-left: 4px solid #28a745;
}

.alert-danger {
    background: #f8d7da;
    color: #721c24;
    border-left: 4px solid #dc3545;
}

@media (max-width: 768px) {
    .package-info {
        padding: 25px;
    }
    
    .package-name {
        font-size: 1.8rem;
    }
    
    .package-meta {
        flex-direction: column;
        gap: 15px;
    }
    
    .date-inputs {
        grid-template-columns: 1fr;
    }
    
    .booking-section {
        position: static;
        margin-top: 30px;
    }
}
</style>
</head>
<body>
<?php include('includes/header.php');?>

<!-- Page Header -->
<div class="page-header">
    <div class="page-header-content">
        <div class="container">
            <h1 class="page-title wow fadeInUp" data-wow-delay="0.3s">Package Details</h1>
        </div>
    </div>
</div>

<!-- Package Details Section -->
<div class="package-details-section">
    <div class="container">
        <?php if($error){?><div class="alert alert-danger"><strong>ERROR</strong>:<?php echo htmlentities($error); ?> </div><?php } 
        else if($msg){?><div class="alert alert-success"><strong>SUCCESS</strong>:<?php echo htmlentities($msg); ?> </div><?php }?>
        
        <?php 
        $pid=intval($_GET['pkgid']);
        $sql = "SELECT * from tbltourpackages where PackageId=:pid";
        $query = $dbh->prepare($sql);
        $query -> bindParam(':pid', $pid, PDO::PARAM_STR);
        $query->execute();
        $results=$query->fetchAll(PDO::FETCH_OBJ);
        $cnt=1;
        if($query->rowCount() > 0) {
            foreach($results as $result) { ?>
                <div class="row">
                    <div class="col-lg-8">
                        <div class="package-main wow fadeInUp" data-wow-delay="0.3s">
                            <div class="package-image-section">
                                <img src="admin/pacakgeimages/<?php $images = json_decode($result->pacakgeimages); echo htmlentities($images[0]);?>" alt="<?php echo htmlentities($result->PackageName);?>">
                            </div>
                            <div class="package-info">
                                <h1 class="package-name"><?php echo htmlentities($result->PackageName);?></h1>
                                <p class="package-id">#PKG-<?php echo htmlentities($result->PackageId);?></p>
                                
                                <div class="package-meta">
                                    <div class="meta-item">
                                        <div class="meta-icon">
                                            <i class="fa fa-tag"></i>
                                        </div>
                                        <div class="meta-text">
                                            <strong>Type:</strong> <?php echo htmlentities($result->PackageType);?>
                                        </div>
                                    </div>
                                    <div class="meta-item">
                                        <div class="meta-icon">
                                            <i class="fa fa-map-marker"></i>
                                        </div>
                                        <div class="meta-text">
                                            <strong>Location:</strong> <?php echo htmlentities($result->PackageLocation);?>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="package-features">
                                    <h3 class="features-title">Package Features</h3>
                                    <p class="features-text"><?php echo htmlentities($result->PackageFeatures);?></p>
                                </div>
                                
                                <div class="package-description">
                                    <h3 class="description-title">Package Details</h3>
                                    <p class="description-text"><?php echo htmlentities($result->PackageDetails);?></p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-lg-4">
                        <div class="booking-section wow fadeInUp" data-wow-delay="0.5s">
                            <h3 class="booking-title">Book This Package</h3>
                            
                            <form name="book" method="post" class="booking-form">
                                <div class="date-inputs">
                                    <div class="form-group">
                                        <label class="form-label">From Date</label>
                                        <input class="form-input" id="datepicker" type="text" placeholder="dd-mm-yyyy" name="fromdate" required="">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">To Date</label>
                                        <input class="form-input" id="datepicker1" type="text" placeholder="dd-mm-yyyy" name="todate" required="">
                                    </div>
                                </div>
                                
                                <div class="form-group">
                                    <label class="form-label">Special Requirements</label>
                                    <textarea class="form-input" name="comment" rows="3" placeholder="Any special requirements or comments..."></textarea>
                                </div>
                                
                                <div class="package-price">
                                    <div class="price-label">Package Price</div>
                                    <div class="price-amount">₹<?php echo htmlentities($result->PackagePrice);?></div>
                                </div>
                                
                                <?php if($_SESSION['login']) { ?>
                                    <button type="submit" name="submit2" class="book-btn">Book Now</button>
                                <?php } else { ?>
                                    <div class="login-prompt">
                                        <p>Please login to book this package</p>
                                        <a href="#" data-toggle="modal" data-target="#myModal4" class="book-btn">Login to Book</a>
                                    </div>
                                <?php } ?>
                            </form>
                        </div>
                    </div>
                </div>
            <?php }
        } ?>
    </div>
</div>

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