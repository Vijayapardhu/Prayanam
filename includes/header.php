<?php if($_SESSION['login'])
{?>
<div class="top-header-modern">
    <div class="container d-flex justify-content-between align-items-center py-2">
        <div class="header-left-actions d-flex align-items-center">
            <a href="index.php" class="header-action-item home-link"><i class="fa fa-home"></i> Home</a>
            <a href="profile.php" class="header-action-item">My Profile</a>
            <a href="change-password.php" class="header-action-item">Change Password</a>
            <a href="tour-history.php" class="header-action-item">My Tour History</a>
            <a href="issuetickets.php" class="header-action-item">Issue Tickets</a>
        </div>
        <div class="header-right-actions d-flex align-items-center">
            <span class="welcome-text">Welcome, <?php echo htmlentities($_SESSION['login']);?></span>
            <a href="logout.php" class="header-action-item logout-link">Logout</a>
        </div>
    </div>
</div><?php } else {?>
<div class="top-header-modern">
    <div class="container d-flex justify-content-between align-items-center py-2">
        <div class="header-left-actions d-flex align-items-center">
            <a href="index.php" class="header-action-item home-link"><i class="fa fa-home"></i> Home</a>
            <a href="admin/index.php" class="header-action-item">Admin Login</a>
        </div>
        <div class="header-right-actions d-flex align-items-center">
            <span class="toll-number">Toll Number : 8121505999</span>
            <a href="#" data-toggle="modal" data-target="#myModal" class="header-action-item signup-link">Sign Up</a>
            <a href="#" data-toggle="modal" data-target="#myModal4" class="header-action-item signin-link">Sign In</a>
        </div>
    </div>
</div>
<?php }?>
<!--- /top-header ---->



<!--- header ---->
<div class="header">
	<div class="container">
		<div class="logo wow fadeInDown animated" data-wow-delay=".5s">
			<a href="index.php"><img src="admin/images/prayanam.png" alt="Prayanam"></a>	
		</div>
	
		<div class="lock fadeInDown animated" data-wow-delay=".5s"> 
			<li><i class="fa fa-lock"></i></li>
            <li><div class="securetxt">SAFE &amp; SECURE </div></li>
			<div class="clearfix"></div>
		</div>
		<div class="clearfix"></div>
	</div>
</div>
<!--- /header ---->

<!--- footer-btm ---->
<div class="footer-btm wow fadeInLeft animated" data-wow-delay=".5s">
	<div class="container">
	<div class="navigation">
			<nav class="navbar navbar-default">
				<!-- Brand and toggle get grouped for better mobile display -->
				<div class="navbar-header">
				  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				  </button>
				</div>
				<!-- Collect the nav links, forms, and other content for toggling -->
				<div class="collapse navbar-collapse nav-wil" id="bs-example-navbar-collapse-1">
					<nav class="cl-effect-1">
						<ul class="nav navbar-nav">
							<li><a href="index.php">Home</a></li>
							<li><a href="page.php?type=aboutus">About</a></li>
								<li><a href="package-list.php">Tour Packages</a></li>
								<li><a href="page.php?type=privacy">Privacy Policy</a></li>
								<li><a href="page.php?type=terms">Terms of Use</a></li>
								<li><a href="page.php?type=contact">Contact Us</a></li>
								<?php if($_SESSION['login'])
{?>
								<li>Need Help?<a href="#" data-toggle="modal" data-target="#myModal3"> / Write Us </a>  </li>
								<?php } else { ?>
								<li><a href="enquiry.php"> Enquiry </a>  </li>
								<?php } ?>
								<div class="clearfix"></div>

						</ul>
					</nav>
				</div><!-- /.navbar-collapse -->	
			</nav>
		</div>
		
		<div class="clearfix"></div>
	</div>
</div>