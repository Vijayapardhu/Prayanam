<?php
session_start();
include('includes/config.php');
if(strlen($_SESSION['alogin'])==0)
	{	
header('location:index.php');
}
else{
if(isset($_GET['pid']))
{
$pid=intval($_GET['pid']);
$sql = "SELECT * from TblTourPackages WHERE PackageId=:pid";
$query = $dbh -> prepare($sql);
$query->bindParam(':pid',$pid,PDO::PARAM_STR);
$query->execute();
$results=$query->fetchAll(PDO::FETCH_OBJ);
$cnt=1;
if($query->rowCount() > 0)
{
foreach($results as $result)
{				?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Update Package</title>
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
/* Update Package Specific Styles */
.update-package-hero {
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

.update-package-hero::before {
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

.update-package-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.update-package-hero p {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 0;
}

.package-form-container {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    animation: slideInUp 0.8s ease 0.2s both;
}

.package-form-header {
    margin-bottom: 32px;
    text-align: center;
}

.package-form-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 12px;
}

.package-form-subtitle {
    color: var(--text-secondary);
    font-size: 1rem;
}

.form-section {
    margin-bottom: 32px;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
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

.form-input {
    width: 100%;
    padding: 16px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-primary);
    font-size: 1rem;
    transition: var(--transition);
    backdrop-filter: blur(10px);
}

.form-input:focus {
    outline: none;
    border-color: #667eea;
    background: rgba(255, 255, 255, 0.1);
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-input::placeholder {
    color: rgba(255, 255, 255, 0.5);
}

.form-textarea {
    width: 100%;
    min-height: 120px;
    padding: 16px 20px;
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

.current-image-section {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    padding: 24px;
    margin-bottom: 24px;
}

.current-image-title {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.current-image-display {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

.current-image-item {
    position: relative;
    border-radius: var(--border-radius-sm);
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.current-image-item img {
    width: 120px;
    height: 80px;
    object-fit: cover;
    display: block;
}

.current-image-remove {
    position: absolute;
    top: 4px;
    right: 4px;
    background: rgba(255, 107, 107, 0.9);
    color: white;
    border: none;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    transition: var(--transition);
}

.current-image-remove:hover {
    background: rgba(255, 107, 107, 1);
    transform: scale(1.1);
}

.file-upload-modern {
    position: relative;
    margin-bottom: 24px;
}

.file-upload-modern input[type="file"] {
    position: absolute;
    opacity: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
}

.file-upload-label {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 2px dashed var(--border-color);
    border-radius: var(--border-radius-sm);
    cursor: pointer;
    transition: var(--transition);
    text-align: center;
}

.file-upload-label:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: #667eea;
}

.file-upload-label i {
    font-size: 2rem;
    color: var(--text-secondary);
    margin-bottom: 12px;
}

.file-upload-label span {
    color: var(--text-secondary);
    font-weight: 500;
}

.preview-images {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 16px;
    margin-top: 16px;
}

.preview-item {
    position: relative;
    border-radius: var(--border-radius-sm);
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.preview-item img {
    width: 100%;
    height: 80px;
    object-fit: cover;
    display: block;
}

.preview-remove {
    position: absolute;
    top: 4px;
    right: 4px;
    background: rgba(255, 107, 107, 0.9);
    color: white;
    border: none;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    transition: var(--transition);
}

.preview-remove:hover {
    background: rgba(255, 107, 107, 1);
    transform: scale(1.1);
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

/* Responsive Design */
@media (max-width: 768px) {
    .update-package-hero h1 {
        font-size: 2rem;
    }
    
    .package-form-container {
        padding: 24px;
    }
    
    .form-grid {
        grid-template-columns: 1fr;
    }
    
    .form-actions {
        flex-direction: column;
    }
    
    .current-image-display {
        justify-content: center;
    }
    
    .preview-images {
        grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    }
    
    .update-package-hero {
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
        <a href="manage-packages.php" class="breadcrumb-item">Manage Packages</a>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-item active">Update Package</span>
    </div>

    <!-- Hero Section -->
    <div class="update-package-hero">
        <h1>Update Package</h1>
        <p>Modify and enhance your travel package details</p>
    </div>

    <!-- Package Form Container -->
    <div class="package-form-container">
        <div class="package-form-header">
            <h2 class="package-form-title">Package Information</h2>
            <p class="package-form-subtitle">Update the details for <?php echo htmlentities($result->PackageName); ?></p>
        </div>

        <form method="post" enctype="multipart/form-data" class="form-section">
            <div class="form-grid">
                <div class="form-group">
                    <label class="form-label">Package Name</label>
                    <input type="text" name="packagename" class="form-input" value="<?php echo htmlentities($result->PackageName);?>" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label">Package Type</label>
                    <select name="packagetype" class="form-input" required>
                        <option value="">Select package type</option>
                        <option value="Adventure" <?php if($result->PackageType=='Adventure') echo 'selected'; ?>>Adventure</option>
                        <option value="Relaxation" <?php if($result->PackageType=='Relaxation') echo 'selected'; ?>>Relaxation</option>
                        <option value="Cultural" <?php if($result->PackageType=='Cultural') echo 'selected'; ?>>Cultural</option>
                        <option value="Business" <?php if($result->PackageType=='Business') echo 'selected'; ?>>Business</option>
                        <option value="Family" <?php if($result->PackageType=='Family') echo 'selected'; ?>>Family</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label class="form-label">Package Location</label>
                    <input type="text" name="packagelocation" class="form-input" value="<?php echo htmlentities($result->PackageLocation);?>" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label">Package Price</label>
                    <input type="number" name="packageprice" class="form-input" value="<?php echo htmlentities($result->PackagePrice);?>" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label">Package Features</label>
                    <input type="text" name="packagefeatures" class="form-input" value="<?php echo htmlentities($result->PackageFetures);?>" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label">Package Duration</label>
                    <input type="text" name="packageduration" class="form-input" value="<?php echo htmlentities($result->PackageDuration);?>" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label">Package Date</label>
                    <input type="date" name="packagedate" class="form-input" value="<?php echo htmlentities($result->PackageDate);?>" required>
                </div>
            </div>

            <div class="form-group">
                <label class="form-label">Package Details</label>
                <textarea name="packagedetails" class="form-textarea" required><?php echo htmlentities($result->PackageDetails);?></textarea>
            </div>

            <!-- Current Images Section -->
            <div class="current-image-section">
                <div class="current-image-title">
                    <i class="fa fa-image"></i>
                    Current Package Images
                </div>
                <div class="current-image-display">
                    <?php if($result->PackageImage) { ?>
                        <div class="current-image-item">
                            <img src="pacakgeimages/<?php echo htmlentities($result->PackageImage);?>" alt="Package Image">
                            <button type="button" class="current-image-remove" onclick="removeCurrentImage()">
                                <i class="fa fa-times"></i>
                            </button>
                        </div>
                    <?php } else { ?>
                        <p style="color: var(--text-secondary);">No images uploaded yet</p>
                    <?php } ?>
                </div>
            </div>

            <!-- New Images Upload Section -->
            <div class="form-group">
                <label class="form-label">Upload New Images</label>
                <div class="file-upload-modern">
                    <input type="file" name="packageimage" id="packageimage" multiple accept="image/*">
                    <label for="packageimage" class="file-upload-label">
                        <i class="fa fa-cloud-upload"></i>
                        <span>Click to upload new package images</span>
                    </label>
                </div>
                <div class="preview-images" id="preview-container"></div>
            </div>

            <div class="form-actions">
                <button type="button" class="btn-modern secondary" onclick="window.history.back()">
                    <i class="fa fa-arrow-left"></i>
                    Cancel
                </button>
                <button type="submit" name="submit" class="btn-modern primary" id="updateBtn">
                    <i class="fa fa-save"></i>
                    Update Package
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
$(document).ready(function() {
    // File upload preview
    $('#packageimage').on('change', function() {
        const files = this.files;
        const previewContainer = $('#preview-container');
        previewContainer.empty();
        
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const previewItem = $(`
                        <div class="preview-item">
                            <img src="${e.target.result}" alt="Preview">
                            <button type="button" class="preview-remove" onclick="removePreview(this)">
                                <i class="fa fa-times"></i>
                            </button>
                        </div>
                    `);
                    previewContainer.append(previewItem);
                };
                reader.readAsDataURL(file);
            }
        }
    });
    
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
            btnText.text('Update Package');
            
            // Show success message
            showAlert('Package updated successfully!', 'success');
        }, 2000);
    });
    
    // Auto-resize textarea
    $('.form-textarea').on('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
    
    // Initialize textarea height
    $('.form-textarea').trigger('input');
    
    // Form validation
    $('form').on('submit', function(e) {
        const packageName = $('input[name="packagename"]').val().trim();
        const packageType = $('select[name="packagetype"]').val();
        const packageLocation = $('input[name="packagelocation"]').val().trim();
        const packagePrice = $('input[name="packageprice"]').val();
        
        if (!packageName) {
            e.preventDefault();
            showAlert('Please enter package name', 'error');
            return false;
        }
        
        if (!packageType) {
            e.preventDefault();
            showAlert('Please select package type', 'error');
            return false;
        }
        
        if (!packageLocation) {
            e.preventDefault();
            showAlert('Please enter package location', 'error');
            return false;
        }
        
        if (!packagePrice || packagePrice <= 0) {
            e.preventDefault();
            showAlert('Please enter a valid package price', 'error');
            return false;
        }
    });
});

// Remove preview image
function removePreview(button) {
    $(button).closest('.preview-item').remove();
}

// Remove current image
function removeCurrentImage() {
    if (confirm('Are you sure you want to remove the current image?')) {
        $('.current-image-item').fadeOut(300, function() {
            $(this).remove();
        });
    }
}

// Show alert function
function showAlert(message, type) {
    const alert = $(`
        <div class="alert-modern ${type} animate-slide-in-down">
            <i class="fa fa-${type === 'success' ? 'check-circle' : 'exclamation-triangle'}"></i>
            <span>${message}</span>
        </div>
    `);
    
    $('.package-form-container').prepend(alert);
    
    setTimeout(() => {
        alert.fadeOut(300, function() {
            $(this).remove();
        });
    }, 5000);
}

// Auto-save functionality
let autoSaveTimer;
$('input, textarea, select').on('input change', function() {
    clearTimeout(autoSaveTimer);
    autoSaveTimer = setTimeout(() => {
        // Auto-save logic here
        console.log('Auto-saving package changes...');
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
<?php } } } ?>