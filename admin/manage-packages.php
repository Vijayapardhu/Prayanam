<?php
session_start();
include('includes/config.php');
if(strlen($_SESSION['alogin'])==0)
	{	
header('location:index.php');
}
else{

// code for delete
if(isset($_GET['del']))
{
$id=$_GET['del'];
$sql = "delete from TblTourPackages WHERE PackageId=:id";
$query = $dbh->prepare($sql);
$query->bindParam(':id',$id,PDO::PARAM_STR);
$query->execute();
$msg="Package Deleted successfully";
}

?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Manage Packages</title>
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
/* Manage Packages Specific Styles */
.manage-packages-hero {
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

.manage-packages-hero::before {
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

.manage-packages-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.manage-packages-hero p {
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
    min-width: 150px;
}

.filter-select:focus {
    outline: none;
    border-color: #667eea;
    background: rgba(255, 255, 255, 0.1);
}

.packages-table-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    overflow: hidden;
    animation: slideInUp 0.8s ease 0.4s both;
}

.packages-table {
    width: 100%;
    border-collapse: collapse;
}

.packages-table thead {
    background: rgba(102, 126, 234, 0.1);
}

.packages-table th {
    padding: 20px 16px;
    text-align: left;
    font-weight: 600;
    color: var(--text-primary);
    border-bottom: 1px solid var(--border-color);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.85rem;
}

.packages-table td {
    padding: 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: var(--text-secondary);
    transition: var(--transition);
}

.packages-table tbody tr {
    transition: var(--transition);
}

.packages-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: scale(1.01);
}

.packages-table tbody tr:hover td {
    color: var(--text-primary);
}

.package-image {
    width: 60px;
    height: 60px;
    border-radius: var(--border-radius-sm);
    object-fit: cover;
    border: 2px solid var(--border-color);
    transition: var(--transition);
}

.packages-table tbody tr:hover .package-image {
    border-color: #667eea;
    transform: scale(1.1);
}

.package-name {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.package-type {
    font-size: 0.8rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.package-price {
    font-weight: 700;
    color: #00d4aa;
    font-size: 1.1rem;
}

.package-location {
    color: var(--text-secondary);
    font-size: 0.9rem;
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

.action-btn.view {
    background: rgba(102, 126, 234, 0.2);
    color: #667eea;
}

.action-btn.view:hover {
    background: rgba(102, 126, 234, 0.3);
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

/* Modal Styles */
.package-modal {
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

.package-modal.show {
    opacity: 1;
    visibility: visible;
}

.package-modal-content {
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

.package-modal.show .package-modal-content {
    transform: scale(1);
}

.package-modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border-color);
}

.package-modal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
}

.package-modal-close {
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

.package-modal-close:hover {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
}

.package-details-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 24px;
}

.package-detail-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.package-detail-label {
    font-size: 0.8rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}

.package-detail-value {
    color: var(--text-primary);
    font-weight: 500;
}

.package-description {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    padding: 16px;
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 24px;
}

.package-image-modal {
    width: 100%;
    max-height: 300px;
    object-fit: cover;
    border-radius: var(--border-radius-sm);
    margin-bottom: 24px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .manage-packages-hero h1 {
        font-size: 2rem;
    }
    
    .controls-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }
    
    .packages-table {
        font-size: 0.9rem;
    }
    
    .packages-table th,
    .packages-table td {
        padding: 12px 8px;
    }
    
    .package-image {
        width: 40px;
        height: 40px;
    }
    
    .action-buttons {
        flex-direction: column;
        gap: 4px;
    }
    
    .pagination-section {
        flex-direction: column;
        gap: 16px;
    }
    
    .package-details-grid {
        grid-template-columns: 1fr;
    }
    
    .manage-packages-hero,
    .controls-section,
    .packages-table-container {
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
        <span class="breadcrumb-item active">Manage Packages</span>
    </div>

    <!-- Hero Section -->
    <div class="manage-packages-hero">
        <h1>Manage Packages</h1>
        <p>View, edit, and manage all your travel packages in one place</p>
    </div>

    <!-- Controls Section -->
    <div class="controls-section">
        <div class="controls-grid">
            <div class="search-box">
                <i class="fa fa-search"></i>
                <input type="text" id="searchInput" placeholder="Search packages...">
            </div>
            
            <select class="filter-select" id="typeFilter">
                <option value="">All Types</option>
                <option value="Adventure">Adventure</option>
                <option value="Relaxation">Relaxation</option>
                <option value="Cultural">Cultural</option>
                <option value="Business">Business</option>
                <option value="Family">Family</option>
            </select>
            
            <a href="create-package.php" class="btn-modern success">
                <i class="fa fa-plus"></i>
                Add Package
            </a>
        </div>
    </div>

    <!-- Packages Table -->
    <div class="packages-table-container">
        <div class="table-modern">
            <table class="packages-table">
                <thead>
                    <tr>
                        <th>Image</th>
                        <th>Package Details</th>
                        <th>Type</th>
                        <th>Location</th>
                        <th>Price</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="packagesTableBody">
                    <?php if(isset($error)){?><div class="errorWrap"><strong>ERROR</strong>:<?php echo htmlentities($error); ?> </div><?php } 
				else if(isset($msg)){?><div class="succWrap"><strong>SUCCESS</strong>:<?php echo htmlentities($msg); ?> </div><?php }?>
                    <?php
                    $sql = "SELECT * from TblTourPackages";
                    $query = $dbh->prepare($sql);
                    $query->execute();
                    $results=$query->fetchAll(PDO::FETCH_OBJ);
                    $cnt=1;
                    if($query->rowCount() > 0) {
                        foreach($results as $result) {
                    ?>
                    <tr data-package='<?php echo json_encode($result); ?>'>
                        <td>
                            <?php
                            $images = json_decode($result->pacakgeimages);
                            if (!empty($images)) {
                            ?>
                            <img src="pacakgeimages/<?php echo htmlentities($images[0]);?>" 
                                 alt="<?php echo htmlentities($result->PackageName);?>" 
                                 class="package-image">
                            <?php } ?>
                        </td>
                        <td>
                            <div class="package-name"><?php echo htmlentities($result->PackageName);?></div>
                            <div class="package-type"><?php echo htmlentities($result->PackageType);?></div>
                        </td>
                        <td>
                            <span class="status-badge info"><?php echo htmlentities($result->PackageType);?></span>
                        </td>
                        <td>
                            <div class="package-location"><?php echo htmlentities($result->PackageLocation);?></div>
                        </td>
                        <td>
                            <div class="package-price">₹<?php echo htmlentities($result->PackagePrice);?></div>
                        </td>
                        <td>
                            <div class="action-buttons">
                                <button class="action-btn view" onclick="viewPackage(<?php echo $result->PackageId;?>)">
                                    <i class="fa fa-eye"></i>
                                </button>
                                <a href="update-package.php?pid=<?php echo $result->PackageId;?>" class="action-btn edit">
                                    <i class="fa fa-edit"></i>
                                </a>
                                <button class="action-btn delete" onclick="deletePackage(<?php echo $result->PackageId;?>)">
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
                Showing <?php echo $cnt-1; ?> packages
            </div>
            <div class="pagination-controls">
                <button class="pagination-btn">Previous</button>
                <button class="pagination-btn active">1</button>
                <button class="pagination-btn">Next</button>
            </div>
        </div>
    </div>
</div>

<!-- Package Modal -->
<div class="package-modal" id="packageModal">
    <div class="package-modal-content">
        <div class="package-modal-header">
            <h3 class="package-modal-title">Package Details</h3>
            <button class="package-modal-close" onclick="closeModal()">
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
    // Search functionality
    $('#searchInput').on('keyup', function() {
        const searchTerm = $(this).val().toLowerCase();
        const rows = $('#packagesTableBody tr');
        
        rows.each(function() {
            const packageName = $(this).find('.package-name').text().toLowerCase();
            const packageType = $(this).find('.package-type').text().toLowerCase();
            const packageLocation = $(this).find('.package-location').text().toLowerCase();
            
            if (packageName.includes(searchTerm) || 
                packageType.includes(searchTerm) || 
                packageLocation.includes(searchTerm)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
    
    // Filter functionality
    $('#typeFilter').on('change', function() {
        const filterValue = $(this).val().toLowerCase();
        const rows = $('#packagesTableBody tr');
        
        if (filterValue === '') {
            rows.show();
        } else {
            rows.each(function() {
                const packageType = $(this).find('.package-type').text().toLowerCase();
                if (packageType === filterValue) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            });
        }
    });
    
    // Table row hover effects
    $('.packages-table tbody tr').hover(
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

// View package modal
function viewPackage(packageId) {
    const row = $(`tr[data-package*='"PackageId":"${packageId}"']`);
    const packageData = JSON.parse(row.attr('data-package'));
    
    const images = JSON.parse(packageData.pacakgeimages);
    let imageHTML = '';
    if (images && images.length > 0) {
        imageHTML = `<div class="package-images-modal">`;
        images.forEach(image => {
            imageHTML += `<img src="pacakgeimages/${image}" alt="${packageData.PackageName}" class="package-image-modal">`;
        });
        imageHTML += `</div>`;
    }
    
    const modalContent = `
        ${imageHTML}
        
        <div class="package-details-grid">
            <div class="package-detail-item">
                <div class="package-detail-label">Package Name</div>
                <div class="package-detail-value">${packageData.PackageName}</div>
            </div>
            <div class="package-detail-item">
                <div class="package-detail-label">Package Type</div>
                <div class="package-detail-value">${packageData.PackageType}</div>
            </div>
            <div class="package-detail-item">
                <div class="package-detail-label">Location</div>
                <div class="package-detail-value">${packageData.PackageLocation}</div>
            </div>
            <div class="package-detail-item">
                <div class="package-detail-label">Price</div>
                <div class="package-detail-value">₹${packageData.PackagePrice}</div>
            </div>
        </div>
        
        <div class="package-detail-item">
            <div class="package-detail-label">Features</div>
            <div class="package-detail-value">${packageData.PackageFetures}</div>
        </div>
        
        <div class="package-description">
            <strong>Description:</strong><br>
            ${packageData.PackageDetails}
        </div>
        
        <div class="form-actions">
            <a href="update-package.php?pid=${packageData.PackageId}" class="btn-modern success">
                <i class="fa fa-edit"></i>
                Edit Package
            </a>
            <button class="btn-modern" onclick="closeModal()">
                <i class="fa fa-times"></i>
                Close
            </button>
        </div>
    `;
    
    $('#modalContent').html(modalContent);
    $('#packageModal').addClass('show');
}

// Close modal
function closeModal() {
    $('#packageModal').removeClass('show');
}

// Delete package
function deletePackage(packageId) {
    if (confirm('Are you sure you want to delete this package?')) {
        $.ajax({
            url: 'manage-packages.php',
            type: 'GET',
            data: { del: packageId },
            success: function(response) {
                // Assuming PHP returns a success message or redirects
                showAlert('Package deleted successfully', 'success');
                $(`tr[data-package*='"PackageId":"${packageId}"']`).fadeOut(300, function() {
                    $(this).remove();
                });
            },
            error: function(xhr, status, error) {
                showAlert('Error deleting package: ' + error, 'error');
            }
        });
    }
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
$(document).on('click', '.package-modal', function(e) {
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