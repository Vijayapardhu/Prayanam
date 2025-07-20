<?php
session_start();
include('includes/config.php');
if(strlen($_SESSION['alogin'])==0)
	{	
header('location:index.php');
}
else{
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Admin Dashboard</title>
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
/* Dashboard Specific Styles */
.dashboard-hero {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 40px;
    margin-bottom: 32px;
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: slideInDown 0.8s ease;
}

.dashboard-hero::before {
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

.dashboard-hero h1 {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.dashboard-hero p {
    font-size: 1.2rem;
    color: var(--text-secondary);
    margin-bottom: 0;
}

.quick-actions-modern {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    margin-bottom: 32px;
    animation: slideInUp 0.8s ease 0.2s both;
}

.quick-actions-modern h2 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 24px;
    color: var(--text-primary);
}

.quick-actions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
}

.quick-action-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    padding: 24px;
    text-align: center;
    transition: var(--transition);
    cursor: pointer;
    text-decoration: none;
    color: var(--text-primary);
    position: relative;
    overflow: hidden;
}

.quick-action-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.6s ease;
}

.quick-action-card:hover::before {
    left: 100%;
}

.quick-action-card:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.2);
    color: var(--text-primary);
    text-decoration: none;
}

.quick-action-icon {
    width: 60px;
    height: 60px;
    border-radius: var(--border-radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    color: white;
    margin: 0 auto 16px;
    background: var(--primary-gradient);
}

.quick-action-card:hover .quick-action-icon {
    transform: scale(1.1);
}

.quick-action-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 8px;
}

.quick-action-desc {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.analytics-section {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    margin-bottom: 32px;
    animation: slideInUp 0.8s ease 0.4s both;
}

.analytics-section h2 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 24px;
    color: var(--text-primary);
}

.chart-container {
    background: rgba(255, 255, 255, 0.05);
    border-radius: var(--border-radius-sm);
    padding: 24px;
    border: 1px solid var(--border-color);
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

/* Responsive Design */
@media (max-width: 768px) {
    .dashboard-hero h1 {
        font-size: 2rem;
    }
    
    .dashboard-hero p {
        font-size: 1rem;
    }
    
    .quick-actions-grid {
        grid-template-columns: 1fr;
    }
    
    .dashboard-hero,
    .quick-actions-modern,
    .analytics-section {
        padding: 24px;
    }
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

<!-- Floating Background Elements -->
<div class="floating-element"></div>
<div class="floating-element"></div>
<div class="floating-element"></div>

<div class="dashboard-content">
    <!-- Hero Section -->
    <div class="dashboard-hero">
        <h1>Welcome to Prayanam</h1>
        <p>Your ultimate travel management dashboard with real-time insights and powerful tools</p>
    </div>

    <!-- Statistics Grid -->
    <div class="grid-modern grid-4">
        <div class="stat-card users animate-scale-in" style="animation-delay: 0.1s;">
            <div class="stat-icon">
                <i class="fa fa-users"></i>
            </div>
            <div class="stat-number">
                <?php $sql = "SELECT id from tblusers";
                $query = $dbh -> prepare($sql);
                $query->execute();
                $results=$query->fetchAll(PDO::FETCH_OBJ);
                $cnt=$query->rowCount();
                ?>
                <?php echo htmlentities($cnt);?>
            </div>
            <div class="stat-label">Total Users</div>
        </div>

        <div class="stat-card bookings animate-scale-in" style="animation-delay: 0.2s;">
            <div class="stat-icon">
                <i class="fa fa-calendar-check"></i>
            </div>
            <div class="stat-number">
                <?php $sql1 = "SELECT BookingId from tblbooking";
                $query1 = $dbh -> prepare($sql1);
                $query1->execute();
                $results1=$query1->fetchAll(PDO::FETCH_OBJ);
                $cnt1=$query1->rowCount();
                ?>
                <?php echo htmlentities($cnt1);?>
            </div>
            <div class="stat-label">Total Bookings</div>
        </div>

        <div class="stat-card enquiries animate-scale-in" style="animation-delay: 0.3s;">
            <div class="stat-icon">
                <i class="fa fa-envelope"></i>
            </div>
            <div class="stat-number">
                <?php $sql2 = "SELECT id from tblenquiry";
                $query2= $dbh -> prepare($sql2);
                $query2->execute();
                $results2=$query2->fetchAll(PDO::FETCH_OBJ);
                $cnt2=$query2->rowCount();
                ?>
                <?php echo htmlentities($cnt2);?>
            </div>
            <div class="stat-label">Total Enquiries</div>
        </div>

        <div class="stat-card packages animate-scale-in" style="animation-delay: 0.4s;">
            <div class="stat-icon">
                <i class="fa fa-suitcase"></i>
            </div>
            <div class="stat-number">
                <?php $sql3 = "SELECT PackageId from tbltourpackages";
                $query3= $dbh -> prepare($sql3);
                $query3->execute();
                $results3=$query3->fetchAll(PDO::FETCH_OBJ);
                $cnt3=$query3->rowCount();
                ?>
                <?php echo htmlentities($cnt3);?>
            </div>
            <div class="stat-label">Total Packages</div>
        </div>
    </div>

    <!-- Quick Actions -->
    <div class="quick-actions-modern">
        <h2>Quick Actions</h2>
        <div class="quick-actions-grid">
            <a href="create-package.php" class="quick-action-card">
                <div class="quick-action-icon">
                    <i class="fa fa-plus"></i>
                </div>
                <div class="quick-action-title">Create Package</div>
                <div class="quick-action-desc">Add new travel packages</div>
            </a>
            
            <a href="manage-bookings.php" class="quick-action-card">
                <div class="quick-action-icon">
                    <i class="fa fa-calendar"></i>
                </div>
                <div class="quick-action-title">Manage Bookings</div>
                <div class="quick-action-desc">View and manage bookings</div>
            </a>
            
            <a href="manage-enquires.php" class="quick-action-card">
                <div class="quick-action-icon">
                    <i class="fa fa-envelope"></i>
                </div>
                <div class="quick-action-title">View Enquiries</div>
                <div class="quick-action-desc">Check customer enquiries</div>
            </a>
            
            <a href="manage-users.php" class="quick-action-card">
                <div class="quick-action-icon">
                    <i class="fa fa-users"></i>
                </div>
                <div class="quick-action-title">Manage Users</div>
                <div class="quick-action-desc">User management</div>
            </a>
            
            <a href="manage-packages.php" class="quick-action-card">
                <div class="quick-action-icon">
                    <i class="fa fa-suitcase"></i>
                </div>
                <div class="quick-action-title">All Packages</div>
                <div class="quick-action-desc">View all packages</div>
            </a>
            
            <a href="issuetickets.php" class="quick-action-card">
                <div class="quick-action-icon">
                    <i class="fa fa-ticket"></i>
                </div>
                <div class="quick-action-title">Issue Tickets</div>
                <div class="quick-action-desc">Handle support tickets</div>
            </a>
        </div>
    </div>

    <!-- Analytics Section -->
    <div class="analytics-section">
        <h2>Analytics Overview</h2>
        <div class="chart-container">
            <div id="hero-area" style="height: 300px;"></div>
        </div>
    </div>

    <!-- Recent Activity -->
    <div class="glass-card animate-slide-in-up" style="animation-delay: 0.6s;">
        <h2 style="margin-bottom: 24px; font-size: 1.5rem; font-weight: 700;">Recent Activity</h2>
        <div class="table-modern">
            <table>
                <thead>
                    <tr>
                        <th>Activity</th>
                        <th>User</th>
                        <th>Time</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>New booking created</td>
                        <td>John Doe</td>
                        <td>2 minutes ago</td>
                        <td><span class="status-badge success">Completed</span></td>
                    </tr>
                    <tr>
                        <td>Package updated</td>
                        <td>Admin</td>
                        <td>15 minutes ago</td>
                        <td><span class="status-badge info">Updated</span></td>
                    </tr>
                    <tr>
                        <td>Enquiry received</td>
                        <td>Jane Smith</td>
                        <td>1 hour ago</td>
                        <td><span class="status-badge warning">Pending</span></td>
                    </tr>
                    <tr>
                        <td>User registered</td>
                        <td>Mike Johnson</td>
                        <td>2 hours ago</td>
                        <td><span class="status-badge success">Active</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
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
<!-- morris JavaScript -->	
<script src="js/raphael-min.js"></script>
<script src="js/morris.js"></script>
<script>
	$(document).ready(function() {
		//CHARTS
	    function gd(year, day, month) {
			return new Date(year, month - 1, day).getTime();
		}
		
		graphArea2 = Morris.Area({
			element: 'hero-area',
			padding: 10,
        behaveLikeLine: true,
        gridEnabled: false,
        gridLineColor: '#dddddd',
        axes: true,
        resize: true,
        smooth:true,
        pointSize: 0,
        lineWidth: 0,
        fillOpacity:0.85,
			data: [
				{period: '2024 Q1', bookings: 2668, enquiries: 2649, users: 1200},
				{period: '2024 Q2', bookings: 15780, enquiries: 13799, users: 1500},
				{period: '2024 Q3', bookings: 12920, enquiries: 10975, users: 1800},
				{period: '2024 Q4', bookings: 8770, enquiries: 6600, users: 2100},
				{period: '2025 Q1', bookings: 10820, enquiries: 10924, users: 2400},
				{period: '2025 Q2', bookings: 9680, enquiries: 9010, users: 2700}
			],
			lineColors:['#667eea','#00d4aa','#f093fb'],
			xkey: 'period',
            redraw: true,
            ykeys: ['bookings', 'enquiries', 'users'],
            labels: ['Bookings', 'Enquiries', 'Users'],
			pointSize: 2,
			hideHover: 'auto',
			resize: true
		});
		
		// Add interactive effects
		$('.stat-card').hover(function() {
			$(this).find('.stat-icon').css('transform', 'scale(1.1) rotate(5deg)');
		}, function() {
			$(this).find('.stat-icon').css('transform', 'scale(1) rotate(0deg)');
		});
		
		$('.quick-action-card').click(function() {
			// Add click animation
			$(this).css('transform', 'scale(0.95)');
			setTimeout(() => {
				$(this).css('transform', '');
			}, 150);
		});
	   
	});
</script>
</body>
</html>
<?php } ?>