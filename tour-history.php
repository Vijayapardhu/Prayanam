<?php
session_start();
error_reporting(0);
include('includes/config.php');
if(strlen($_SESSION['login'])==0)
	{	
header('location:index.php');
}
else{
if(isset($_REQUEST['bkid']))
	{
		$bid=intval($_GET['bkid']);
$email=$_SESSION['login'];
	$sql ="SELECT FromDate FROM tblbooking WHERE UserEmail=:email and BookingId=:bid";
$query= $dbh -> prepare($sql);
$query-> bindParam(':email', $email, PDO::PARAM_STR);
$query-> bindParam(':bid', $bid, PDO::PARAM_STR);
$query-> execute();
$results = $query -> fetchAll(PDO::FETCH_OBJ);
if($query->rowCount() > 0)
{
foreach($results as $result)
{
	 $fdate=$result->FromDate;

	$a=explode("/",$fdate);
	$val=array_reverse($a);
	 $mydate =implode("/",$val);
	$cdate=date('Y/m/d');
	$date1=date_create("$cdate");
	$date2=date_create("$fdate");
 $diff=date_diff($date1,$date2);
echo $df=$diff->format("%a");
if($df>1)
{
$status=2;
$cancelby='u';
$sql = "UPDATE tblbooking SET status=:status,CancelledBy=:cancelby WHERE UserEmail=:email and BookingId=:bid";
$query = $dbh->prepare($sql);
$query -> bindParam(':status',$status, PDO::PARAM_STR);
$query -> bindParam(':cancelby',$cancelby , PDO::PARAM_STR);
$query-> bindParam(':email',$email, PDO::PARAM_STR);
$query-> bindParam(':bid',$bid, PDO::PARAM_STR);
$query -> execute();

$msg="Booking Cancelled successfully";
}
else
{
$error="You can't cancel booking before 24 hours";
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
/* Tour History Specific Styles */
.tour-history-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.tour-history-hero::before {
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

.tour-history-hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 16px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.tour-history-hero p {
    font-size: 1.2rem;
    opacity: 0.9;
}

.tour-history-container {
    background: #ffffff;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 90%;
    margin: 50px auto;
}

.tour-history-header {
    text-align: center;
    margin-bottom: 30px;
}

.tour-history-title {
    font-size: 2rem;
    font-weight: 700;
    color: #34495e;
    margin-bottom: 10px;
}

.tour-history-subtitle {
    color: #7f8c8d;
    font-size: 1rem;
}

.table-responsive {
    overflow-x: auto;
}

.history-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.history-table th,
.history-table td {
    padding: 12px 15px;
    border: 1px solid #ddd;
    text-align: left;
}

.history-table th {
    background-color: #f8f8f8;
    font-weight: 600;
    color: #34495e;
}

.history-table tbody tr:nth-child(even) {
    background-color: #f2f2f2;
}

.history-table tbody tr:hover {
    background-color: #f0f0f0;
}

.status-badge {
    padding: 5px 10px;
    border-radius: 5px;
    font-weight: 600;
    font-size: 0.85rem;
}

.status-badge.pending {
    background-color: #fff3cd;
    color: #f39c12;
}

.status-badge.confirmed {
    background-color: #d4edda;
    color: #28a745;
}

.status-badge.cancelled {
    background-color: #f8d7da;
    color: #dc3545;
}

.action-btn {
    background: linear-gradient(45deg, #e74c3c, #c0392b);
    color: white;
    padding: 8px 15px;
    border: none;
    border-radius: 20px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
}

.action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    color: white;
    text-decoration: none;
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
    .tour-history-hero h1 {
        font-size: 2.5rem;
    }
    
    .tour-history-container {
        margin: 30px 20px;
        padding: 30px;
    }
    
    .history-table th,
    .history-table td {
        padding: 8px 10px;
        font-size: 0.9rem;
    }
}
</style>
</head>
<body>
<?php include('includes/header.php');?>

<!-- Tour History Hero Section -->
<div class="tour-history-hero">
    <div class="container">
        <h1 class="wow zoomIn" data-wow-delay="0.3s">My Tour History</h1>
        <p class="wow fadeInUp" data-wow-delay="0.5s">View all your past and upcoming travel bookings</p>
    </div>
</div>

<!-- Tour History Content Section -->
<div class="tour-history-container wow fadeInUp" data-wow-delay="0.7s">
    <div class="tour-history-header">
        <h2 class="tour-history-title">Your Bookings</h2>
        <p class="tour-history-subtitle">Details of your travel history with Prayanam</p>
    </div>

    <?php if($error){?><div class="alert-modern error"><i class="fa fa-exclamation-triangle"></i><span><?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="alert-modern success"><i class="fa fa-check-circle"></i><span><?php echo htmlentities($msg); ?> </div><?php }?>

    <div class="table-responsive">
        <table class="history-table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Booking Id</th>
                    <th>Package Name</th>
                    <th>From</th>
                    <th><th>To</th>
                    <th>Comment</th>
                    <th>Status</th>
                    <th>Booking Date</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <?php 
                $uemail=$_SESSION['login'];
                $sql = "SELECT tblbooking.BookingId as bookid,tblbooking.PackageId as pkgid,tbltourpackages.PackageName as packagename,tblbooking.FromDate as fromdate,tblbooking.ToDate as todate,tblbooking.Comment as comment,tblbooking.status as status,tblbooking.RegDate as regdate,tblbooking.CancelledBy as cancelby,tblbooking.UpdationDate as upddate from tblbooking join tbltourpackages on tbltourpackages.PackageId=tblbooking.PackageId where UserEmail=:uemail";
                $query = $dbh->prepare($sql);
                $query -> bindParam(':uemail', $uemail, PDO::PARAM_STR);
                $query->execute();
                $results=$query->fetchAll(PDO::FETCH_OBJ);
                $cnt=1;
                if($query->rowCount() > 0)
                {
                foreach($results as $result)
                {	?>
                <tr>
                    <td><?php echo htmlentities($cnt);?></td>
                    <td>#BK<?php echo htmlentities($result->bookid);?></td>
                    <td><a href="package-details.php?pkgid=<?php echo htmlentities($result->pkgid);?>"><?php echo htmlentities($result->packagename);?></a></td>
                    <td><?php echo htmlentities($result->fromdate);?></td>
                    <td><?php echo htmlentities($result->todate);?></td>
                    <td><?php echo htmlentities($result->comment);?></td>
                    <td>
                        <?php 
                        if($result->status==0) {
                            echo "Pending";
                        } else if($result->status==1) {
                            echo "Confirmed";
                        } else if($result->status==2 && $result->cancelby=='u') {
                            echo "Canceled by you at " . $result->upddate;
                        } else if($result->status==2 && $result->cancelby=='a') {
                            echo "Canceled by admin at " . $result->upddate;
                        }
                        ?>
                    </td>
                    <td><?php echo htmlentities($result->regdate);?></td>
                    <td>
                        <?php if($result->status==2) { ?>
                            <span class="status-badge cancelled">Cancelled</span>
                        <?php } else {?>
                            <a href="tour-history.php?bkid=<?php echo htmlentities($result->bookid);?>" onclick="return confirm('Do you really want to cancel booking')" class="action-btn">Cancel</a>
                        <?php }?>
                    </td>
                </tr>
                <?php $cnt=$cnt+1; }} ?>
            </tbody>
        </table>
    </div>
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
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">My Tour History</h3>
		<form name="chngpwd" method="post" onSubmit="return valid();">
		 <?php if($error){?><div class="errorWrap"><strong>ERROR</strong>:<?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="succWrap"><strong>SUCCESS</strong>:<?php echo htmlentities($msg); ?> </div><?php }?>
	<p>
	<table border="1" width="100%">
<tr align="center">
<th>#</th>
<th>Booking Id</th>
<th>Package Name</th>	
<th>From</th>
<th>To</th>
<th>Comment</th>
<th>Status</th>
<th>Booking Date</th>
<th>Action</th>
</tr>
<?php 

$uemail=$_SESSION['login'];;
$sql = "SELECT tblbooking.BookingId as bookid,tblbooking.PackageId as pkgid,tbltourpackages.PackageName as packagename,tblbooking.FromDate as fromdate,tblbooking.ToDate as todate,tblbooking.Comment as comment,tblbooking.status as status,tblbooking.RegDate as regdate,tblbooking.CancelledBy as cancelby,tblbooking.UpdationDate as upddate from tblbooking join tbltourpackages on tbltourpackages.PackageId=tblbooking.PackageId where UserEmail=:uemail";
$query = $dbh->prepare($sql);
$query -> bindParam(':uemail', $uemail, PDO::PARAM_STR);
$query->execute();
$results=$query->fetchAll(PDO::FETCH_OBJ);
$cnt=1;
if($query->rowCount() > 0)
{
foreach($results as $result)
{	?>
<tr align="center">
<td><?php echo htmlentities($cnt);?></td>
<td>#BK<?php echo htmlentities($result->bookid);?></td>
<td><a href="package-details.php?pkgid=<?php echo htmlentities($result->pkgid);?>"><?php echo htmlentities($result->packagename);?></a></td>
<td><?php echo htmlentities($result->fromdate);?></td>
<td><?php echo htmlentities($result->todate);?></td>
<td><?php echo htmlentities($result->comment);?></td>
<td><?php if($result->status==0)
{
echo "Pending";
}
if($result->status==1)
{
echo "Confirmed";
}
if($result->status==2 and  $result->cancelby=='u')
{
echo "Canceled by you at " .$result->upddate;
} 
if($result->status==2 and $result->cancelby=='a')
{
echo "Canceled by admin at " .$result->upddate;

}
?></td>
<td><?php echo htmlentities($result->regdate);?></td>
<?php if($result->status==2)
{
	?><td>Cancelled</td>
<?php } else {?>
<td><a href="tour-history.php?bkid=<?php echo htmlentities($result->bookid);?>" onclick="return confirm('Do you really want to cancel booking')" >Cancel</a></td>
<?php }?>
</tr>
<?php $cnt=$cnt+1; }} ?>
	</table>
		
			</p>
			</form>

		
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