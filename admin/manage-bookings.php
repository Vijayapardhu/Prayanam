<?php
session_start();
include('includes/config.php');
if(strlen($_SESSION['alogin'])==0)
	{	
header('location:index.php');
}
else{
if(isset($_GET['del']))
{
$id=$_GET['del'];
$sql = "delete from tblbooking  WHERE id=:id";
$query = $dbh->prepare($sql);
$query -> bindParam(':id',$id, PDO::PARAM_STR);
$query -> execute();
$msg="Booking deleted successfully";
}
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Manage Bookings</title>
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
/* Manage Bookings Specific Styles */
.manage-bookings-hero {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    margin-bottom: 32px;
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: slideInDown 0.8s ease;
}

.manage-bookings-hero::before {
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

.manage-bookings-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.manage-bookings-hero p {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 0;
}

.controls-section {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 24px;
    margin-bottom: 32px;
    animation: slideInUp 0.8s ease 0.2s both;
}

.controls-grid {
    display: grid;
    grid-template-columns: 1fr auto auto;
    gap: 20px;
    align-items: center;
}

.search-box {
    position: relative;
}

.search-box input {
    width: 100%;
    padding: 12px 20px 12px 50px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-primary);
    font-size: 1rem;
    transition: var(--transition);
    backdrop-filter: blur(10px);
}

.search-box input:focus {
    outline: none;
    border-color: #667eea;
    background: rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.search-box i {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-secondary);
    font-size: 1.1rem;
}

.filter-select {
    padding: 12px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-primary);
    font-size: 1rem;
    transition: var(--transition);
    backdrop-filter: blur(10px);
    cursor: pointer;
}

.filter-select:focus {
    outline: none;
    border-color: #667eea;
    background: rgba(255, 255, 255, 0.1);
}

.bookings-table-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    overflow: hidden;
    animation: slideInUp 0.8s ease 0.4s both;
}

.bookings-table {
    width: 100%;
    border-collapse: collapse;
}

.bookings-table thead {
    background: rgba(102, 126, 234, 0.1);
}

.bookings-table th {
    padding: 20px 16px;
    text-align: left;
    font-weight: 600;
    color: var(--text-primary);
    border-bottom: 1px solid var(--border-color);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.85rem;
}

.bookings-table td {
    padding: 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: var(--text-secondary);
    transition: var(--transition);
}

.bookings-table tbody tr {
    transition: var(--transition);
}

.bookings-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: scale(1.01);
}

.bookings-table tbody tr:hover td {
    color: var(--text-primary);
}

.booking-info {
    display: flex;
    align-items: center;
}

.booking-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--primary-gradient);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 600;
    font-size: 0.9rem;
    margin-right: 12px;
}

.booking-name {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.booking-package {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.booking-dates {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.date-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.85rem;
}

.date-label {
    color: var(--text-secondary);
    font-weight: 500;
}

.date-value {
    color: var(--text-primary);
    font-weight: 600;
}

.booking-status {
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
}

.booking-status.confirmed {
    background: var(--success-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(67, 233, 123, 0.3);
}

.booking-status.pending {
    background: var(--warning-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(255, 193, 7, 0.3);
}

.booking-status.cancelled {
    background: var(--accent-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(255, 107, 107, 0.3);
}

.action-buttons {
    display: flex;
    gap: 8px;
}

.action-btn {
    width: 32px;
    height: 32px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: var(--transition);
    font-size: 0.9rem;
}

.action-btn.view {
    background: rgba(102, 126, 234, 0.2);
    color: #667eea;
}

.action-btn.view:hover {
    background: rgba(102, 126, 234, 0.3);
    transform: scale(1.1);
}

.action-btn.edit {
    background: rgba(0, 212, 170, 0.2);
    color: #00d4aa;
}

.action-btn.edit:hover {
    background: rgba(0, 212, 170, 0.3);
    transform: scale(1.1);
}

.action-btn.delete {
    background: rgba(255, 107, 107, 0.2);
    color: #ff6b6b;
}

.action-btn.delete:hover {
    background: rgba(255, 107, 107, 0.3);
    transform: scale(1.1);
}

.pagination-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 24px;
    background: rgba(255, 255, 255, 0.02);
    border-top: 1px solid var(--border-color);
}

.pagination-info {
    color: var(--text-secondary);
    font-size: 0.9rem;
}

.pagination-controls {
    display: flex;
    gap: 8px;
}

.pagination-btn {
    padding: 8px 12px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-secondary);
    cursor: pointer;
    transition: var(--transition);
    font-size: 0.9rem;
}

.pagination-btn:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
}

.pagination-btn.active {
    background: var(--primary-gradient);
    color: white;
    border-color: #667eea;
}

/* Booking Modal */
.booking-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    opacity: 0;
    visibility: hidden;
    transition: var(--transition);
}

.booking-modal.show {
    opacity: 1;
    visibility: visible;
}

.booking-modal-content {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    max-width: 600px;
    width: 90%;
    max-height: 80vh;
    overflow-y: auto;
    box-shadow: var(--shadow-heavy);
    transform: scale(0.8);
    transition: var(--transition);
}

.booking-modal.show .booking-modal-content {
    transform: scale(1);
}

.booking-modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border-color);
}

.booking-modal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
}

.booking-modal-close {
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 1.5rem;
    cursor: pointer;
    transition: var(--transition);
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.booking-modal-close:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
}

.booking-details-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 24px;
}

.booking-detail-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.booking-detail-label {
    font-size: 0.8rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}

.booking-detail-value {
    color: var(--text-primary);
    font-weight: 500;
}

/* Responsive Design */
@media (max-width: 768px) {
    .manage-bookings-hero h1 {
        font-size: 2rem;
    }
    
    .controls-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }
    
    .bookings-table {
        font-size: 0.9rem;
    }
    
    .bookings-table th,
    .bookings-table td {
        padding: 12px 8px;
    }
    
    .booking-avatar {
        width: 32px;
        height: 32px;
        font-size: 0.8rem;
    }
    
    .action-buttons {
        flex-direction: column;
        gap: 4px;
    }
    
    .pagination-section {
        flex-direction: column;
        gap: 16px;
    }
    
    .booking-details-grid {
        grid-template-columns: 1fr;
    }
    
    .manage-bookings-hero,
    .controls-section,
    .bookings-table-container {
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

<div class="dashboard-content">
    <!-- Breadcrumb -->
    <div class="breadcrumb-modern">
        <a href="dashboard.php" class="breadcrumb-item">Dashboard</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-item active">Manage Bookings</span>
    </div>

    <!-- Hero Section -->
    <div class="manage-bookings-hero">
        <h1>Manage Bookings</h1>
        <p>View and manage all travel bookings in your system</p>
    </div>

    <!-- Controls Section -->
    <div class="controls-section">
        <div class="controls-grid">
            <div class="search-box">
                <i class="fa fa-search"></i>
                <input type="text" id="searchInput" placeholder="Search bookings...">
            </div>
            
            <select class="filter-select" id="statusFilter">
                <option value="">All Status</option>
                <option value="confirmed">Confirmed</option>
                <option value="pending">Pending</option>
                <option value="cancelled">Cancelled</option>
            </select>
            
            <div class="booking-stats">
                <span class="status-badge info" id="bookingCount">0 Bookings</span>
            </div>
        </div>
    </div>

    <!-- Bookings Table -->
    <div class="bookings-table-container">
        <div class="table-modern">
            <table class="bookings-table">
                <thead>
                    <tr>
                        <th>Customer</th>
                        <th>Package</th>
                        <th>Travel Dates</th>
                        <th>Contact Info</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="bookingsTableBody">
                    <?php 
                    $sql = "SELECT tblbooking.BookingId as bookid,tblusers.FullName as fname,tblusers.MobileNumber as mnumber,tblusers.EmailId as email,tbltourpackages.PackageName as pckname,tblbooking.PackageId as pid,tblbooking.FromDate as fdate,tblbooking.ToDate as tdate,tblbooking.Comment as comment,tblbooking.status as status,tblbooking.CancelledBy as cancelby,tblbooking.UpdationDate as upddate from tblusers join  tblbooking on  tblbooking.UserEmail=tblusers.EmailId join tbltourpackages on tbltourpackages.PackageId=tblbooking.PackageId";
                    $query = $dbh -> prepare($sql);
                    $query->execute();
                    $results=$query->fetchAll(PDO::FETCH_OBJ);
                    $cnt=1;
                    if($query->rowCount() > 0) {
                        foreach($results as $result) {
                            $name = htmlentities($result->fname);
                            $initials = strtoupper(substr($name, 0, 2));
                            $statusClass = $result->status == 1 ? 'confirmed' : ($result->status == 2 ? 'cancelled' : 'pending');
                            $statusText = $result->status == 1 ? 'Confirmed' : ($result->status == 2 ? 'Cancelled' : 'Pending');
                    ?>
                    <tr data-booking='<?php echo json_encode($result); ?>'>
                        <td>
                            <div class="booking-info">
                                <div class="booking-avatar"><?php echo $initials; ?></div>
                                <div>
                                    <div class="booking-name"><?php echo $name; ?></div>
                                    <div class="booking-package"><?php echo htmlentities($result->pckname); ?></div>
                                </div>
                            </div>
                        </td>
                        <td><?php echo htmlentities($result->pckname); ?></td>
                        <td>
                            <div class="booking-dates">
                                <div class="date-item">
                                    <span class="date-label">From:</span>
                                    <span class="date-value"><?php echo htmlentities($result->fdate); ?></span>
                                </div>
                                <div class="date-item">
                                    <span class="date-label">To:</span>
                                    <span class="date-value"><?php echo htmlentities($result->tdate); ?></span>
                                </div>
                            </div>
                        </td>
                        <td>
                            <div class="booking-dates">
                                <div class="date-item">
                                    <span class="date-label">Mobile:</span>
                                    <span class="date-value"><?php echo htmlentities($result->mnumber); ?></span>
                                </div>
                                <div class="date-item">
                                    <span class="date-label">Email:</span>
                                    <span class="date-value"><?php echo htmlentities($result->email); ?></span>
                                </div>
                            </div>
                        </td>
                        <td>
                            <span class="booking-status <?php echo $statusClass; ?>"><?php echo $statusText; ?></span>
                        </td>
                        <td>
                            <div class="action-buttons">
                                <button class="action-btn view" onclick="viewBooking(<?php echo $result->bookid;?>)">
                                    <i class="fa fa-eye"></i>
                                </button>
                                <button class="action-btn edit" onclick="editBooking(<?php echo $result->bookid;?>)">
                                    <i class="fa fa-edit"></i>
                                </button>
                                <button class="action-btn delete" onclick="deleteBooking(<?php echo $result->bookid;?>)">
                                    <i class="fa fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                    <?php $cnt=$cnt+1; } } ?>
                </tbody>
            </table>
        </div>
        
        <!-- Pagination -->
        <div class="pagination-section">
            <div class="pagination-info">
                Showing <?php echo $cnt-1; ?> bookings
            </div>
            <div class="pagination-controls">
                <button class="pagination-btn">Previous</button>
                <button class="pagination-btn active">1</button>
                <button class="pagination-btn">Next</button>
            </div>
        </div>
    </div>
</div>

<!-- Booking Modal -->
<div class="booking-modal" id="bookingModal">
    <div class="booking-modal-content">
        <div class="booking-modal-header">
            <h3 class="booking-modal-title">Booking Details</h3>
            <button class="booking-modal-close" onclick="closeModal()">
                <i class="fa fa-times"></i>
            </button>
        </div>
        <div id="modalContent">
            <!-- Modal content will be loaded here -->
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
<script>
$(document).ready(function() {
    // Update booking count
    updateBookingCount();
    
    // Search functionality
    $('#searchInput').on('keyup', function() {
        const searchTerm = $(this).val().toLowerCase();
        const rows = $('#bookingsTableBody tr');
        let visibleCount = 0;
        
        rows.each(function() {
            const customerName = $(this).find('.booking-name').text().toLowerCase();
            const packageName = $(this).find('.booking-package').text().toLowerCase();
            const mobileNumber = $(this).find('td:nth-child(4) .date-value').first().text().toLowerCase();
            
            if (customerName.includes(searchTerm) || 
                packageName.includes(searchTerm) || 
                mobileNumber.includes(searchTerm)) {
                $(this).show();
                visibleCount++;
            } else {
                $(this).hide();
            }
        });
        
        updateBookingCount(visibleCount);
    });
    
    // Status filter functionality
    $('#statusFilter').on('change', function() {
        const selectedStatus = $(this).val().toLowerCase();
        const rows = $('#bookingsTableBody tr');
        let visibleCount = 0;
        
        rows.each(function() {
            const status = $(this).find('.booking-status').text().toLowerCase();
            
            if (selectedStatus === '' || status === selectedStatus) {
                $(this).show();
                visibleCount++;
            } else {
                $(this).hide();
            }
        });
        
        updateBookingCount(visibleCount);
    });
    
    // Table row hover effects
    $('.bookings-table tbody tr').hover(
        function() {
            $(this).find('.action-buttons').css('opacity', '1');
        },
        function() {
            $(this).find('.action-buttons').css('opacity', '0.7');
        }
    );
    
    // Initialize action buttons opacity
    $('.action-buttons').css('opacity', '0.7');
});

// Update booking count
function updateBookingCount(count) {
    const totalBookings = count || $('#bookingsTableBody tr').length;
    $('#bookingCount').text(`${totalBookings} Bookings`);
}

// View booking modal
function viewBooking(bookingId) {
    const row = $(`tr[data-booking*='"bookid":"${bookingId}"']`);
    const bookingData = JSON.parse(row.attr('data-booking'));
    
    const modalContent = `
        <div class="booking-details-grid">
            <div class="booking-detail-item">
                <div class="booking-detail-label">Customer Name</div>
                <div class="booking-detail-value">${bookingData.fname}</div>
            </div>
            <div class="booking-detail-item">
                <div class="booking-detail-label">Package Name</div>
                <div class="booking-detail-value">${bookingData.pckname}</div>
            </div>
            <div class="booking-detail-item">
                <div class="booking-detail-label">From Date</div>
                <div class="booking-detail-value">${bookingData.fdate}</div>
            </div>
            <div class="booking-detail-item">
                <div class="booking-detail-label">To Date</div>
                <div class="booking-detail-value">${bookingData.tdate}</div>
            </div>
            <div class="booking-detail-item">
                <div class="booking-detail-label">Mobile Number</div>
                <div class="booking-detail-value">${bookingData.mnumber}</div>
            </div>
            <div class="booking-detail-item">
                <div class="booking-detail-label">Email</div>
                <div class="booking-detail-value">${bookingData.email}</div>
            </div>
            <div class="booking-detail-item">
                <div class="booking-detail-label">Status</div>
                <div class="booking-detail-value">
                    <span class="booking-status ${bookingData.status == 1 ? 'confirmed' : (bookingData.status == 2 ? 'cancelled' : 'pending')}">
                        ${bookingData.status == 1 ? 'Confirmed' : (bookingData.status == 2 ? 'Cancelled' : 'Pending')}
                    </span>
                </div>
            </div>
            <div class="booking-detail-item">
                <div class="booking-detail-label">Comment</div>
                <div class="booking-detail-value">${bookingData.comment || 'No comment'}</div>
            </div>
        </div>
        
        <div class="form-actions">
            <button class="btn-modern success" onclick="editBooking(${bookingData.bookid})">
                <i class="fa fa-edit"></i>
                Edit Booking
            </button>
            <button class="btn-modern" onclick="closeModal()">
                <i class="fa fa-times"></i>
                Close
            </button>
        </div>
    `;
    
    $('#modalContent').html(modalContent);
    $('#bookingModal').addClass('show');
}

// Edit booking function
function editBooking(bookingId) {
    // Add edit functionality here
    showAlert('Edit functionality will be implemented here', 'info');
}

// Delete booking function
function deleteBooking(bookingId) {
    if (confirm('Are you sure you want to delete this booking?')) {
        $.ajax({
            url: 'manage-bookings.php',
            type: 'GET',
            data: { del: bookingId },
            success: function(response) {
                showAlert('Booking deleted successfully', 'success');
                $(`tr[data-booking*='"bookid":"${bookingId}"']`).fadeOut(300, function() {
                    $(this).remove();
                    updateBookingCount();
                });
            },
            error: function(xhr, status, error) {
                showAlert('Error deleting booking: ' + error, 'error');
            }
        });
    }
}

// Close modal
function closeModal() {
    $('#bookingModal').removeClass('show');
}

// Show alert function
function showAlert(message, type) {
    const alert = $(`
        <div class="alert-modern ${type} animate-slide-in-down">
            <i class="fa fa-${type === 'success' ? 'check-circle' : type === 'warning' ? 'exclamation-triangle' : 'info-circle'}"></i>
            <span>${message}</span>
        </div>
    `);
    
    $('.dashboard-content').prepend(alert);
    
    setTimeout(() => {
        alert.fadeOut(300, function() {
            $(this).remove();
        });
    }, 5000);
}

// Close modal when clicking outside
$(document).on('click', '.booking-modal', function(e) {
    if (e.target === this) {
        closeModal();
    }
});

// Close modal with Escape key
$(document).on('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});
</script>
</body>
</html>
<?php } ?>