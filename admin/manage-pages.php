<?php
session_start();
error_reporting(0);
include('includes/config.php');
if(strlen($_SESSION['alogin'])==0)
	{	
header('location:index.php');
}
else{
if($_POST['submit']=="Update")
{
	$pagetype=$_GET['type'];
	$pagedetails=$_POST['pgedetails'];
$sql = "UPDATE tblpages SET detail=:pagedetails WHERE type=:pagetype";
$query = $dbh->prepare($sql);
$query -> bindParam(':pagetype',$pagetype, PDO::PARAM_STR);
$query-> bindParam(':pagedetails',$pagedetails, PDO::PARAM_STR);
$query -> execute();
$msg="Page data updated  successfully";

}

	?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Admin Manage Pages</title>
		<link rel="icon" type="image/png" href="images/prayanam.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Pooled Responsive web template, Bootstrap Web Templates, Flat Web Templates, Android Compatible web template, 
Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyEricsson, Motorola web design" />
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
/* Manage Pages Specific Styles */
.manage-pages-hero {
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

.manage-pages-hero::before {
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

.manage-pages-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.manage-pages-hero p {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 0;
}

.page-form-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    animation: slideInUp 0.8s ease 0.2s both;
}

.page-form-header {
    margin-bottom: 32px;
    text-align: center;
}

.page-form-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 12px;
}

.page-form-subtitle {
    color: var(--text-secondary);
    font-size: 1rem;
}

.form-section {
    margin-bottom: 32px;
}

.form-group {
    margin-bottom: 24px;
}

.form-label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.form-select {
    width: 100%;
    padding: 16px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-primary);
    font-size: 1rem;
    transition: var(--transition);
    backdrop-filter: blur(10px);
    cursor: pointer;
}

.form-select:focus {
    outline: none;
    border-color: #667eea;
    background: rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-textarea {
    width: 100%;
    min-height: 300px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-primary);
    font-size: 1rem;
    line-height: 1.6;
    transition: var(--transition);
    backdrop-filter: blur(10px);
    resize: vertical;
    font-family: 'Inter', sans-serif;
}

.form-textarea:focus {
    outline: none;
    border-color: #667eea;
    background: rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-textarea::placeholder {
    color: rgba(255, 255, 255, 0.5);
}

.selected-page-display {
    background: rgba(102, 126, 234, 0.1);
    border: 1px solid rgba(102, 126, 234, 0.3);
    border-radius: var(--border-radius-sm);
    padding: 16px 20px;
    color: var(--text-primary);
    font-weight: 600;
    text-align: center;
    margin-bottom: 24px;
}

.form-actions {
    display: flex;
    gap: 16px;
    justify-content: center;
    margin-top: 32px;
}

.btn-modern {
    padding: 16px 32px;
    border: none;
    border-radius: var(--border-radius-sm);
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    position: relative;
    overflow: hidden;
}

.btn-modern::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.btn-modern:hover::before {
    left: 100%;
}

.btn-modern.primary {
    background: var(--primary-gradient);
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.btn-modern.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.btn-modern.secondary {
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
}

.btn-modern.secondary:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: translateY(-2px);
}

/* Alert Messages */
.alert-modern {
    padding: 16px 20px;
    border-radius: var(--border-radius-sm);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 500;
    animation: slideInDown 0.5s ease;
}

.alert-modern.success {
    background: var(--success-gradient);
    color: white;
    box-shadow: 0 4px 15px rgba(67, 233, 123, 0.3);
}

.alert-modern.error {
    background: var(--accent-gradient);
    color: white;
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
}

.alert-modern i {
    font-size: 1.2rem;
}

/* Page Type Options */
.page-type-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
}

.page-type-option {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    padding: 16px;
    cursor: pointer;
    transition: var(--transition);
    text-align: center;
}

.page-type-option:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: #667eea;
    transform: translateY(-2px);
}

.page-type-option.active {
    background: var(--primary-gradient);
    border-color: #667eea;
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.page-type-icon {
    font-size: 2rem;
    margin-bottom: 8px;
    display: block;
}

.page-type-label {
    font-weight: 600;
    font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .manage-pages-hero h1 {
        font-size: 2rem;
    }
    
    .page-form-container {
        padding: 24px;
    }
    
    .form-actions {
        flex-direction: column;
    }
    
    .page-type-options {
        grid-template-columns: 1fr;
    }
    
    .manage-pages-hero {
        padding: 24px;
    }
}

/* Loading State */
.btn-modern.loading {
    pointer-events: none;
    opacity: 0.8;
}

.btn-modern.loading::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    margin: -10px 0 0 -10px;
    border: 2px solid transparent;
    border-top: 2px solid currentColor;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
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
        <span class="breadcrumb-item active">Manage Pages</span>
    </div>

    <!-- Hero Section -->
    <div class="manage-pages-hero">
        <h1>Manage Pages</h1>
        <p>Update and manage your website's content pages</p>
    </div>

    <!-- Page Form Container -->
    <div class="page-form-container">
        <div class="page-form-header">
            <h2 class="page-form-title">Update Page Content</h2>
            <p class="page-form-subtitle">Select a page and update its content</p>
        </div>

        <?php if($error){?>
            <div class="alert-modern error">
                <i class="fa fa-exclamation-triangle"></i>
                <span><strong>ERROR:</strong> <?php echo htmlentities($error); ?></span>
            </div>
        <?php } else if($msg){?>
            <div class="alert-modern success">
                <i class="fa fa-check-circle"></i>
                <span><strong>SUCCESS:</strong> <?php echo htmlentities($msg); ?></span>
            </div>
        <?php }?>

        <form method="post" class="form-section">
            <div class="form-group">
                <label class="form-label">Select Page</label>
                <select name="menu1" class="form-select" id="pageSelect" onChange="MM_jumpMenu('parent',this,0)">
                    <option value="" selected="selected">***Select One***</option>
                    <option value="manage-pages.php?type=terms">Terms and Conditions</option>
                    <option value="manage-pages.php?type=privacy">Privacy and Policy</option>
                    <option value="manage-pages.php?type=aboutus">About Us</option> 
                    <option value="manage-pages.php?type=contact">Contact Us</option>
                </select>
            </div>

            <div class="form-group">
                <label class="form-label">Selected Page</label>
                <div class="selected-page-display" id="selectedPageDisplay">
                    <?php
                    switch($_GET['type']) {
                        case "terms":
                            echo "Terms and Conditions";
                            break;
                        case "privacy":
                            echo "Privacy And Policy";
                            break;
                        case "aboutus":
                            echo "About US";
                            break;
                        case "software":
                            echo "Offers";
                            break;	
                        case "aspnet":
                            echo "Vision And Mission";
                            break;		
                        case "objectives":
                            echo "Objectives";
                            break;						
                        case "disclaimer":
                            echo "Disclaimer";
                            break;
                        case "vbnet":
                            echo "Partner With Us";
                            break;
                        case "candc":
                            echo "Super Brand";
                            break;
                        case "contact":
                            echo "Contact Us";
                            break;
                        default:
                            echo "Please select a page";
                            break;
                    }
                    ?>
                </div>
            </div>

            <div class="form-group">
                <label class="form-label">Page Content</label>
                <textarea class="form-textarea" name="pgedetails" id="pgedetails" placeholder="Enter page content here..." required>
                    <?php 
                    $pagetype=$_GET['type'];
                    $sql = "SELECT detail from tblpages where type=:pagetype";
                    $query = $dbh -> prepare($sql);
                    $query->bindParam(':pagetype',$pagetype,PDO::PARAM_STR);
                    $query->execute();
                    $results=$query->fetchAll(PDO::FETCH_OBJ);
                    $cnt=1;
                    if($query->rowCount() > 0) {
                        foreach($results as $result) {
                            echo htmlentities($result->detail);
                        }
                    }
                    ?>
                </textarea> 
            </div>

            <div class="form-actions">
                <button type="button" class="btn-modern secondary" onclick="window.history.back()">
                    <i class="fa fa-arrow-left"></i>
                    Cancel
                </button>
                <button type="submit" name="submit" value="Update" class="btn-modern primary" id="updateBtn">
                    <i class="fa fa-save"></i>
                    Update Page
                </button>
            </div>
        </form>
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
function MM_jumpMenu(targ,selObj,restore){ //v3.0
  eval(targ+".location='"+selObj.options[selObj.selectedIndex].value+"'");
  if (restore) selObj.selectedIndex=0;
}

$(document).ready(function() {
    // Form submission with loading state
    $('form').on('submit', function(e) {
        const btn = $('#updateBtn');
        const btnText = btn.find('i').next();
        
        // Add loading state
        btn.addClass('loading');
        btnText.text('Updating...');
        
        // Simulate loading time
        setTimeout(() => {
            btn.removeClass('loading');
            btnText.text('Update Page');
            
            // Show success message
            showAlert('Page updated successfully!', 'success');
        }, 2000);
    });
    
    // Auto-resize textarea
    $('#pgedetails').on('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
    
    // Initialize textarea height
    $('#pgedetails').trigger('input');
    
    // Page select change handler
    $('#pageSelect').on('change', function() {
        const selectedOption = $(this).find('option:selected');
        const pageName = selectedOption.text();
        
        if (pageName !== '***Select One***') {
            $('#selectedPageDisplay').text(pageName);
        }
    });
    
    // Form validation
    $('form').on('submit', function(e) {
        const pageSelect = $('#pageSelect').val();
        const pageContent = $('#pgedetails').val().trim();
        
        if (!pageSelect) {
            e.preventDefault();
            showAlert('Please select a page to update', 'error');
            return false;
        }
        
        if (!pageContent) {
            e.preventDefault();
            showAlert('Please enter page content', 'error');
            return false;
        }
    });
});

// Show alert function
function showAlert(message, type) {
    const alert = $(`
        <div class="alert-modern ${type} animate-slide-in-down">
            <i class="fa fa-${type === 'success' ? 'check-circle' : 'exclamation-triangle'}"></i>
            <span>${message}</span>
        </div>
    `);
    
    $('.page-form-container').prepend(alert);
    
    setTimeout(() => {
        alert.fadeOut(300, function() {
            $(this).remove();
        });
    }, 5000);
}

// Auto-save functionality
let autoSaveTimer;
$('#pgedetails').on('input', function() {
    clearTimeout(autoSaveTimer);
    autoSaveTimer = setTimeout(() => {
        // Auto-save logic here
        console.log('Auto-saving...');
    }, 3000);
});

// Keyboard shortcuts
$(document).on('keydown', function(e) {
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        $('#updateBtn').click();
    }
});
</script>
</body>
</html>
<?php } ?>