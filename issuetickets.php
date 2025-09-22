<?php
session_start();
error_reporting(0);
include('includes/config.php');
if(strlen($_SESSION['login'])==0)
	{	
header('location:index.php');
}
else{
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
/* Issue Tickets Specific Styles */
.issue-tickets-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.issue-tickets-hero::before {
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

.issue-tickets-hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 16px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.issue-tickets-hero p {
    font-size: 1.2rem;
    opacity: 0.9;
}

.issue-tickets-container {
    background: #ffffff;
    border-radius: 15px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 90%;
    margin: 50px auto;
}

.issue-tickets-header {
    text-align: center;
    margin-bottom: 30px;
}

.issue-tickets-title {
    font-size: 2rem;
    font-weight: 700;
    color: #34495e;
    margin-bottom: 10px;
}

.issue-tickets-subtitle {
    color: #7f8c8d;
    font-size: 1rem;
}

.table-responsive {
    overflow-x: auto;
}

.issues-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.issues-table th,
.issues-table td {
    padding: 12px 15px;
    border: 1px solid #ddd;
    text-align: left;
}

.issues-table th {
    background-color: #f8f8f8;
    font-weight: 600;
    color: #34495e;
}

.issues-table tbody tr:nth-child(even) {
    background-color: #f2f2f2;
}

.issues-table tbody tr:hover {
    background-color: #f0f0f0;
}

.status-badge {
    padding: 5px 10px;
    border-radius: 5px;
    font-weight: 600;
    font-size: 0.85rem;
}

.status-badge.resolved {
    background-color: #d4edda;
    color: #28a745;
}

.status-badge.pending {
    background-color: #fff3cd;
    color: #f39c12;
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
    .issue-tickets-hero h1 {
        font-size: 2.5rem;
    }
    
    .issue-tickets-container {
        margin: 30px 20px;
        padding: 30px;
    }
    
    .issues-table th,
    .issues-table td {
        padding: 8px 10px;
        font-size: 0.9rem;
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
		<h1 class="wow zoomIn animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: zoomIn;">Issue Tickets</h1>
	</div>
</div>
<!--- /banner-1 ---->
<!--- privacy ---->
<div class="privacy">
	<div class="container">
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">Issue Tickets</h3>
		<div class="issue-tickets-container">
        <div class="issue-tickets-header">
            <h2 class="issue-tickets-title">Your Support Tickets</h2>
            <p class="issue-tickets-subtitle">View the status and details of your submitted issues</p>
        </div>

        <?php if($error){?><div class="alert-modern error"><i class="fa fa-exclamation-triangle"></i><span><?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="alert-modern success"><i class="fa fa-check-circle"></i><span><?php echo htmlentities($msg); ?> </div><?php }?>

        <div class="table-responsive">
            <table class="issues-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Ticket Id</th>
                        <th>Issue</th>
                        <th>Description</th>
                        <th>Admin Remark</th>
                        <th>Reg Date</th>
                        <th>Remark date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <?php 
                    $uemail=$_SESSION['login'];
                    $sql = "SELECT * from tblissues where UserEmail=:uemail";
                    $query = $dbh->prepare($sql);
                    $query -> bindParam(':uemail', $uemail, PDO::PARAM_STR);
                    $query->execute();
                    $results=$query->fetchAll(PDO::FETCH_OBJ);
                    $cnt=1;
                    if($query->rowCount() > 0) {
                        foreach($results as $result) {
                            $statusClass = $result->AdminRemark == '' ? 'pending' : 'resolved';
                            $statusText = $result->AdminRemark == '' ? 'Pending' : 'Resolved';
                    ?>
                    <tr>
                        <td><?php echo htmlentities($cnt);?></td>
                        <td>#TKT-<?php echo htmlentities($result->id);?></td>
                        <td><?php echo htmlentities($result->Issue);?></td>
                        <td><?php echo htmlentities($result->Description);?></td>
                        <td><?php echo htmlentities($result->AdminRemark);?></td>
                        <td><?php echo htmlentities($result->PostingDate);?></td>
                        <td><?php echo htmlentities($result->AdminremarkDate);?></td>
                        <td><span class="status-badge <?php echo $statusClass; ?>"><?php echo $statusText; ?></span></td>
                    </tr>
                    <?php $cnt=$cnt+1; } } ?>
                </tbody>
            </table>
        </div>
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
		<h3 class="wow fadeInDown animated animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: fadeInDown;">Issue Tickets</h3>
		<form name="chngpwd" method="post" onSubmit="return valid();">
		 <?php if($error){?><div class="errorWrap"><strong>ERROR</strong>:<?php echo htmlentities($error); ?> </div><?php } 
				else if($msg){?><div class="succWrap"><strong>SUCCESS</strong>:<?php echo htmlentities($msg); ?> </div><?php }?>
	<p>
	<table border="1" width="100%">
<tr align="center">
<th>#</th>
<th>Ticket Id</th>
<th>Issue</th>	
<th>Description</th>
<th>Admin Remark</th>
<th>Reg Date</th>
<th>Remark date</th>

</tr>
<?php 

$uemail=$_SESSION['login'];;
$sql = "SELECT * from tblissues where UserEmail=:uemail";
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
<td ><?php echo htmlentities($cnt);?></td>
<td width="100">#TKT-<?php echo htmlentities($result->id);?></td>
<td><?php echo htmlentities($result->Issue);?></td>
<td width="300"><?php echo htmlentities($result->Description);?></td>
<td><?php echo htmlentities($result->AdminRemark);?></td>
<td width="100"><?php echo htmlentities($result->PostingDate);?></td>
<td width="100"><?php echo htmlentities($result->AdminremarkDate);?></td>
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
