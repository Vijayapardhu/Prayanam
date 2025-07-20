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
		<title>Prayanam | Manage Issues</title>
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
/* Manage Issues Specific Styles */
.manage-issues-hero {
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

.manage-issues-hero::before {
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

.manage-issues-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.manage-issues-hero p {
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
    grid-template-columns: 1fr auto;
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

.issues-table-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    overflow: hidden;
    animation: slideInUp 0.8s ease 0.4s both;
}

.issues-table {
    width: 100%;
    border-collapse: collapse;
}

.issues-table thead {
    background: rgba(102, 126, 234, 0.1);
}

.issues-table th {
    padding: 20px 16px;
    text-align: left;
    font-weight: 600;
    color: var(--text-primary);
    border-bottom: 1px solid var(--border-color);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.85rem;
}

.issues-table td {
    padding: 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: var(--text-secondary);
    transition: var(--transition);
}

.issues-table tbody tr {
    transition: var(--transition);
}

.issues-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: scale(1.01);
}

.issues-table tbody tr:hover td {
    color: var(--text-primary);
}

.issue-info {
    display: flex;
    align-items: center;
}

.issue-avatar {
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

.issue-name {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.issue-contact {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.issue-title {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.issue-description {
    font-size: 0.85rem;
    color: var(--text-secondary);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.issue-priority {
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
}

.issue-priority.high {
    background: var(--accent-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(255, 107, 107, 0.3);
}

.issue-priority.medium {
    background: var(--warning-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(255, 193, 7, 0.3);
}

.issue-priority.low {
    background: var(--success-gradient);
    color: white;
    box-shadow: 0 2px 8px rgba(67, 233, 123, 0.3);
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

.action-btn.resolve {
    background: rgba(0, 212, 170, 0.2);
    color: #00d4aa;
}

.action-btn.resolve:hover {
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

/* Issue Modal */
.issue-modal {
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

.issue-modal.show {
    opacity: 1;
    visibility: visible;
}

.issue-modal-content {
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

.issue-modal.show .issue-modal-content {
    transform: scale(1);
}

.issue-modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border-color);
}

.issue-modal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
}

.issue-modal-close {
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

.issue-modal-close:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
}

.issue-details-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 24px;
}

.issue-detail-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.issue-detail-label {
    font-size: 0.8rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}

.issue-detail-value {
    color: var(--text-primary);
    font-weight: 500;
}

.issue-description-full {
    grid-column: 1 / -1;
    background: rgba(255, 255, 255, 0.05);
    padding: 16px;
    border-radius: var(--border-radius-sm);
    border: 1px solid var(--border-color);
}

/* Responsive Design */
@media (max-width: 768px) {
    .manage-issues-hero h1 {
        font-size: 2rem;
    }
    
    .controls-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }
    
    .issues-table {
        font-size: 0.9rem;
    }
    
    .issues-table th,
    .issues-table td {
        padding: 12px 8px;
    }
    
    .issue-avatar {
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
    
    .issue-details-grid {
        grid-template-columns: 1fr;
    }
    
    .manage-issues-hero,
    .controls-section,
    .issues-table-container {
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
        <span class="breadcrumb-item active">Manage Issues</span>
    </div>

    <!-- Hero Section -->
    <div class="manage-issues-hero">
        <h1>Manage Issues</h1>
        <p>View and manage all customer support issues in your system</p>
    </div>

    <!-- Controls Section -->
    <div class="controls-section">
        <div class="controls-grid">
            <div class="search-box">
                <i class="fa fa-search"></i>
                <input type="text" id="searchInput" placeholder="Search issues...">
            </div>
            
            <div class="issue-stats">
                <span class="status-badge info" id="issueCount">0 Issues</span>
            </div>
        </div>
    </div>

    <!-- Issues Table -->
    <div class="issues-table-container">
        <div class="table-modern">
            <table class="issues-table">
                <thead>
                    <tr>
                        <th>Customer</th>
                        <th>Issue</th>
                        <th>Description</th>
                        <th>Contact Info</th>
                        <th>Date</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="issuesTableBody">
                    <?php 
                    $sql = "SELECT tblissues.id as id,tblusers.FullName as fname,tblusers.MobileNumber as mnumber,tblusers.EmailId as email,tblissues.Issue as issue,tblissues.Description as Description,tblissues.PostingDate as PostingDate from tblissues join tblusers on tblusers.EmailId=tblissues.UserEmail";
                    $query = $dbh -> prepare($sql);
                    $query->execute();
                    $results=$query->fetchAll(PDO::FETCH_OBJ);
                    $cnt=1;
                    if($query->rowCount() > 0) {
                        foreach($results as $result) {
                            $name = htmlentities($result->fname);
                            $initials = strtoupper(substr($name, 0, 2));
                    ?>
                    <tr data-issue='<?php echo json_encode($result); ?>'>
                        <td>
                            <div class="issue-info">
                                <div class="issue-avatar"><?php echo $initials; ?></div>
                                <div>
                                    <div class="issue-name"><?php echo $name; ?></div>
                                    <div class="issue-contact"><?php echo htmlentities($result->mnumber); ?></div>
                                </div>
                            </div>
                        </td>
                        <td>
                            <div class="issue-title"><?php echo htmlentities($result->issue); ?></div>
                        </td>
                        <td>
                            <div class="issue-description"><?php echo htmlentities($result->Description); ?></div>
                        </td>
                        <td>
                            <div class="issue-contact">
                                <div><?php echo htmlentities($result->mnumber); ?></div>
                                <div><?php echo htmlentities($result->email); ?></div>
                            </div>
                        </td>
                        <td><?php echo htmlentities($result->PostingDate); ?></td>
                        <td>
                            <div class="action-buttons">
                                <button class="action-btn view" onclick="viewIssue(<?php echo $result->id;?>)">
                                    <i class="fa fa-eye"></i>
                                </button>
                                <button class="action-btn resolve" onclick="resolveIssue(<?php echo $result->id;?>)">
                                    <i class="fa fa-check"></i>
                                </button>
                                <button class="action-btn delete" onclick="deleteIssue(<?php echo $result->id;?>)">
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
                Showing <?php echo $cnt-1; ?> issues
            </div>
            <div class="pagination-controls">
                <button class="pagination-btn">Previous</button>
                <button class="pagination-btn active">1</button>
                <button class="pagination-btn">Next</button>
            </div>
        </div>
    </div>
</div>

<!-- Issue Modal -->
<div class="issue-modal" id="issueModal">
    <div class="issue-modal-content">
        <div class="issue-modal-header">
            <h3 class="issue-modal-title">Issue Details</h3>
            <button class="issue-modal-close" onclick="closeModal()">
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
    // Update issue count
    updateIssueCount();
    
    // Search functionality
    $('#searchInput').on('keyup', function() {
        const searchTerm = $(this).val().toLowerCase();
        const rows = $('#issuesTableBody tr');
        let visibleCount = 0;
        
        rows.each(function() {
            const customerName = $(this).find('.issue-name').text().toLowerCase();
            const issueTitle = $(this).find('.issue-title').text().toLowerCase();
            const issueDescription = $(this).find('.issue-description').text().toLowerCase();
            
            if (customerName.includes(searchTerm) || 
                issueTitle.includes(searchTerm) || 
                issueDescription.includes(searchTerm)) {
                $(this).show();
                visibleCount++;
            } else {
                $(this).hide();
            }
        });
        
        updateIssueCount(visibleCount);
    });
    
    // Table row hover effects
    $('.issues-table tbody tr').hover(
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

// Update issue count
function updateIssueCount(count) {
    const totalIssues = count || $('#issuesTableBody tr').length;
    $('#issueCount').text(`${totalIssues} Issues`);
}

// View issue modal
function viewIssue(issueId) {
    const row = $(`tr[data-issue*='"id":"${issueId}"']`);
    const issueData = JSON.parse(row.attr('data-issue'));
    
    const modalContent = `
        <div class="issue-details-grid">
            <div class="issue-detail-item">
                <div class="issue-detail-label">Customer Name</div>
                <div class="issue-detail-value">${issueData.fname}</div>
            </div>
            <div class="issue-detail-item">
                <div class="issue-detail-label">Issue Title</div>
                <div class="issue-detail-value">${issueData.issue}</div>
            </div>
            <div class="issue-detail-item">
                <div class="issue-detail-label">Mobile Number</div>
                <div class="issue-detail-value">${issueData.mnumber}</div>
            </div>
            <div class="issue-detail-item">
                <div class="issue-detail-label">Email</div>
                <div class="issue-detail-value">${issueData.email}</div>
            </div>
            <div class="issue-detail-item">
                <div class="issue-detail-label">Posting Date</div>
                <div class="issue-detail-value">${issueData.PostingDate}</div>
            </div>
            <div class="issue-description-full">
                <div class="issue-detail-label">Description</div>
                <div class="issue-detail-value">${issueData.Description}</div>
            </div>
        </div>
        
        <div class="form-actions">
            <button class="btn-modern success" onclick="resolveIssue(${issueData.id})">
                <i class="fa fa-check"></i>
                Resolve Issue
            </button>
            <button class="btn-modern" onclick="closeModal()">
                <i class="fa fa-times"></i>
                Close
            </button>
        </div>
    `;
    
    $('#modalContent').html(modalContent);
    $('#issueModal').addClass('show');
}

// Resolve issue function
function resolveIssue(issueId) {
    if (confirm('Mark this issue as resolved?')) {
        // Add resolve functionality here
        showAlert('Issue marked as resolved', 'success');
        
        // Remove the row from the table
        $(`tr[data-issue*='"id":"${issueId}"']`).fadeOut(300, function() {
            $(this).remove();
            updateIssueCount();
        });
    }
}

// Delete issue function
function deleteIssue(issueId) {
    if (confirm('Are you sure you want to delete this issue?')) {
        // Add delete functionality here
        showAlert('Issue deleted successfully', 'success');
        
        // Remove the row from the table
        $(`tr[data-issue*='"id":"${issueId}"']`).fadeOut(300, function() {
            $(this).remove();
            updateIssueCount();
        });
    }
}

// Close modal
function closeModal() {
    $('#issueModal').removeClass('show');
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
$(document).on('click', '.issue-modal', function(e) {
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