<?php
session_start();
include('includes/config.php');
if(strlen($_SESSION['alogin'])==0)
	{	
header('location:index.php');
}
else{
if(isset($_GET['eid']))
{
$eid=intval($_GET['eid']);
$status=1;
$sql = "UPDATE tblenquiry SET Status=:status WHERE  id=:eid";
$query = $dbh->prepare($sql);
$query -> bindParam(':status',$status, PDO::PARAM_STR);
$query-> bindParam(':eid',$eid, PDO::PARAM_STR);
$query -> execute();
$msg="Enquiry read successfully";
}
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Manage Enquiries</title>
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
/* Manage Enquiries Specific Styles */
.manage-enquiries-hero {
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

.manage-enquiries-hero::before {
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

.manage-enquiries-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.manage-enquiries-hero p {
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

.enquiries-table-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    overflow: hidden;
    animation: slideInUp 0.8s ease 0.4s both;
}

.enquiries-table {
    width: 100%;
    border-collapse: collapse;
}

.enquiries-table thead {
    background: rgba(102, 126, 234, 0.1);
}

.enquiries-table th {
    padding: 20px 16px;
    text-align: left;
    font-weight: 600;
    color: var(--text-primary);
    border-bottom: 1px solid var(--border-color);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.85rem;
}

.enquiries-table td {
    padding: 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: var(--text-secondary);
    transition: var(--transition);
}

.enquiries-table tbody tr {
    transition: var(--transition);
}

.enquiries-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: scale(1.01);
}

.enquiries-table tbody tr:hover td {
    color: var(--text-primary);
}

.enquiry-info {
    display: flex;
    align-items: center;
}

.enquiry-avatar {
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

.enquiry-name {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.enquiry-contact {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.enquiry-subject {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.enquiry-description {
    font-size: 0.85rem;
    color: var(--text-secondary);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.enquiry-status {
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
    cursor: pointer;
    transition: var(--transition);
}

.enquiry-status.read {
    background: var(--success-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(67, 233, 123, 0.3);
}

.enquiry-status.pending {
    background: var(--warning-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(255, 193, 7, 0.3);
}

.enquiry-status.pending:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(255, 193, 7, 0.4);
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

.action-btn.reply {
    background: rgba(0, 212, 170, 0.2);
    color: #00d4aa;
}

.action-btn.reply:hover {
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

/* Enquiry Modal */
.enquiry-modal {
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

.enquiry-modal.show {
    opacity: 1;
    visibility: visible;
}

.enquiry-modal-content {
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

.enquiry-modal.show .enquiry-modal-content {
    transform: scale(1);
}

.enquiry-modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border-color);
}

.enquiry-modal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
}

.enquiry-modal-close {
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

.enquiry-modal-close:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
}

.enquiry-details-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 24px;
}

.enquiry-detail-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.enquiry-detail-label {
    font-size: 0.8rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}

.enquiry-detail-value {
    color: var(--text-primary);
    font-weight: 500;
}

.enquiry-description-full {
    grid-column: 1 / -1;
    background: rgba(255, 255, 255, 0.05);
    padding: 16px;
    border-radius: var(--border-radius-sm);
    border: 1px solid var(--border-color);
}

/* Responsive Design */
@media (max-width: 768px) {
    .manage-enquiries-hero h1 {
        font-size: 2rem;
    }
    
    .controls-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }
    
    .enquiries-table {
        font-size: 0.9rem;
    }
    
    .enquiries-table th,
    .enquiries-table td {
        padding: 12px 8px;
    }
    
    .enquiry-avatar {
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
    
    .enquiry-details-grid {
        grid-template-columns: 1fr;
    }
    
    .manage-enquiries-hero,
    .controls-section,
    .enquiries-table-container {
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
        <span class="breadcrumb-item active">Manage Enquiries</span>
    </div>

    <!-- Hero Section -->
    <div class="manage-enquiries-hero">
        <h1>Manage Enquiries</h1>
        <p>View and manage all customer enquiries in your system</p>
    </div>

    <!-- Controls Section -->
    <div class="controls-section">
        <div class="controls-grid">
            <div class="search-box">
                <i class="fa fa-search"></i>
                <input type="text" id="searchInput" placeholder="Search enquiries...">
            </div>
            
            <select class="filter-select" id="statusFilter">
                <option value="">All Status</option>
                <option value="read">Read</option>
                <option value="pending">Pending</option>
            </select>
            
            <div class="enquiry-stats">
                <span class="status-badge info" id="enquiryCount">0 Enquiries</span>
            </div>
        </div>
    </div>

    <!-- Enquiries Table -->
    <div class="enquiries-table-container">
        <div class="table-modern">
            <table class="enquiries-table">
                <thead>
                    <tr>
                        <th>Customer</th>
                        <th>Subject</th>
                        <th>Description</th>
                        <th>Contact Info</th>
                        <th>Date</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="enquiriesTableBody">
                    <?php 
                    $sql = "SELECT * from tblenquiry";
                    $query = $dbh -> prepare($sql);
                    $query->execute();
                    $results=$query->fetchAll(PDO::FETCH_OBJ);
                    $cnt=1;
                    if($query->rowCount() > 0) {
                        foreach($results as $result) {
                            $name = htmlentities($result->FullName);
                            $initials = strtoupper(substr($name, 0, 2));
                            $statusClass = $result->Status == 1 ? 'read' : 'pending';
                            $statusText = $result->Status == 1 ? 'Read' : 'Pending';
                    ?>
                    <tr data-enquiry='<?php echo json_encode($result); ?>'>
                        <td>
                            <div class="enquiry-info">
                                <div class="enquiry-avatar"><?php echo $initials; ?></div>
                                <div>
                                    <div class="enquiry-name"><?php echo $name; ?></div>
                                    <div class="enquiry-contact"><?php echo htmlentities($result->MobileNumber); ?></div>
                                </div>
                            </div>
                        </td>
                        <td>
                            <div class="enquiry-subject"><?php echo htmlentities($result->Subject); ?></div>
                        </td>
                        <td>
                            <div class="enquiry-description"><?php echo htmlentities($result->Description); ?></div>
                        </td>
                        <td>
                            <div class="enquiry-contact">
                                <div><?php echo htmlentities($result->MobileNumber); ?></div>
                                <div><?php echo htmlentities($result->EmailId); ?></div>
                            </div>
                        </td>
                        <td><?php echo htmlentities($result->PostingDate); ?></td>
                        <td>
                            <?php if($result->Status==1) { ?>
                                <span class="enquiry-status read">Read</span>
                            <?php } else { ?>
                                <a href="manage-enquires.php?eid=<?php echo htmlentities($result->id);?>" 
                                   class="enquiry-status pending" 
                                   onclick="return confirm('Mark this enquiry as read?')">
                                    Pending
                                </a>
                            <?php } ?>
                        </td>
                        <td>
                            <div class="action-buttons">
                                <button class="action-btn view" onclick="viewEnquiry(<?php echo $result->id;?>)">
                                    <i class="fa fa-eye"></i>
                                </button>
                                <button class="action-btn reply" onclick="replyEnquiry(<?php echo $result->id;?>)">
                                    <i class="fa fa-reply"></i>
                                </button>
                                <button class="action-btn delete" onclick="deleteEnquiry(<?php echo $result->id;?>)">
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
                Showing <?php echo $cnt-1; ?> enquiries
            </div>
            <div class="pagination-controls">
                <button class="pagination-btn">Previous</button>
                <button class="pagination-btn active">1</button>
                <button class="pagination-btn">Next</button>
            </div>
        </div>
    </div>
</div>

<!-- Enquiry Modal -->
<div class="enquiry-modal" id="enquiryModal">
    <div class="enquiry-modal-content">
        <div class="enquiry-modal-header">
            <h3 class="enquiry-modal-title">Enquiry Details</h3>
            <button class="enquiry-modal-close" onclick="closeModal()">
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
    // Update enquiry count
    updateEnquiryCount();
    
    // Search functionality
    $('#searchInput').on('keyup', function() {
        const searchTerm = $(this).val().toLowerCase();
        const rows = $('#enquiriesTableBody tr');
        let visibleCount = 0;
        
        rows.each(function() {
            const customerName = $(this).find('.enquiry-name').text().toLowerCase();
            const subject = $(this).find('.enquiry-subject').text().toLowerCase();
            const description = $(this).find('.enquiry-description').text().toLowerCase();
            
            if (customerName.includes(searchTerm) || 
                subject.includes(searchTerm) || 
                description.includes(searchTerm)) {
                $(this).show();
                visibleCount++;
            } else {
                $(this).hide();
            }
        });
        
        updateEnquiryCount(visibleCount);
    });
    
    // Status filter functionality
    $('#statusFilter').on('change', function() {
        const selectedStatus = $(this).val().toLowerCase();
        const rows = $('#enquiriesTableBody tr');
        let visibleCount = 0;
        
        rows.each(function() {
            const status = $(this).find('.enquiry-status').text().toLowerCase();
            
            if (selectedStatus === '' || status === selectedStatus) {
                $(this).show();
                visibleCount++;
            } else {
                $(this).hide();
            }
        });
        
        updateEnquiryCount(visibleCount);
    });
    
    // Table row hover effects
    $('.enquiries-table tbody tr').hover(
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

// Update enquiry count
function updateEnquiryCount(count) {
    const totalEnquiries = count || $('#enquiriesTableBody tr').length;
    $('#enquiryCount').text(`${totalEnquiries} Enquiries`);
}

// View enquiry modal
function viewEnquiry(enquiryId) {
    const row = $(`tr[data-enquiry*='"id":"${enquiryId}"']`);
    const enquiryData = JSON.parse(row.attr('data-enquiry'));
    
    const modalContent = `
        <div class="enquiry-details-grid">
            <div class="enquiry-detail-item">
                <div class="enquiry-detail-label">Customer Name</div>
                <div class="enquiry-detail-value">${enquiryData.FullName}</div>
            </div>
            <div class="enquiry-detail-item">
                <div class="enquiry-detail-label">Subject</div>
                <div class="enquiry-detail-value">${enquiryData.Subject}</div>
            </div>
            <div class="enquiry-detail-item">
                <div class="enquiry-detail-label">Mobile Number</div>
                <div class="enquiry-detail-value">${enquiryData.MobileNumber}</div>
            </div>
            <div class="enquiry-detail-item">
                <div class="enquiry-detail-label">Email</div>
                <div class="enquiry-detail-value">${enquiryData.EmailId}</div>
            </div>
            <div class="enquiry-detail-item">
                <div class="enquiry-detail-label">Posting Date</div>
                <div class="enquiry-detail-value">${enquiryData.PostingDate}</div>
            </div>
            <div class="enquiry-detail-item">
                <div class="enquiry-detail-label">Status</div>
                <div class="enquiry-detail-value">
                    <span class="enquiry-status ${enquiryData.Status == 1 ? 'read' : 'pending'}">
                        ${enquiryData.Status == 1 ? 'Read' : 'Pending'}
                    </span>
                </div>
            </div>
            <div class="enquiry-description-full">
                <div class="enquiry-detail-label">Description</div>
                <div class="enquiry-detail-value">${enquiryData.Description}</div>
            </div>
        </div>
        
        <div class="form-actions">
            <button class="btn-modern success" onclick="replyEnquiry(${enquiryData.id})">
                <i class="fa fa-reply"></i>
                Reply to Enquiry
            </button>
            <button class="btn-modern" onclick="closeModal()">
                <i class="fa fa-times"></i>
                Close
            </button>
        </div>
    `;
    
    $('#modalContent').html(modalContent);
    $('#enquiryModal').addClass('show');
}

// Reply to enquiry function
function replyEnquiry(enquiryId) {
    // Add reply functionality here
    showAlert('Reply functionality will be implemented here', 'info');
}

// Delete enquiry function
function deleteEnquiry(enquiryId) {
    if (confirm('Are you sure you want to delete this enquiry?')) {
        // Add delete functionality here
        showAlert('Enquiry deleted successfully', 'success');
        
        // Remove the row from the table
        $(`tr[data-enquiry*='"id":"${enquiryId}"']`).fadeOut(300, function() {
            $(this).remove();
            updateEnquiryCount();
        });
    }
}

// Close modal
function closeModal() {
    $('#enquiryModal').removeClass('show');
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
$(document).on('click', '.enquiry-modal', function(e) {
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