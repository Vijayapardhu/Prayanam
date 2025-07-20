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
		<title>Prayanam | Create Package</title>
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
/* Create Package Specific Styles */
.create-package-hero {
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

.create-package-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--secondary-gradient);
    opacity: 0.1;
    z-index: -1;
}

.create-package-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
    background: var(--secondary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.create-package-hero p {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 0;
}

.form-section {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    padding: 32px;
    margin-bottom: 32px;
    animation: slideInUp 0.8s ease 0.2s both;
}

.form-section h2 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 24px;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 12px;
}

.form-section h2 i {
    color: #00d4aa;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
}

.form-group-full {
    grid-column: 1 / -1;
}

.file-upload-modern {
    position: relative;
    display: inline-block;
    width: 100%;
}

.file-upload-modern input[type=file] {
    position: absolute;
    left: -9999px;
}

.file-upload-label {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 2px dashed var(--border-color);
    border-radius: var(--border-radius-sm);
    cursor: pointer;
    transition: var(--transition);
    color: var(--text-secondary);
    font-weight: 500;
}

.file-upload-label:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: #00d4aa;
    color: var(--text-primary);
}

.file-upload-label i {
    font-size: 1.5rem;
    color: #00d4aa;
}

.preview-images {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 16px;
    margin-top: 16px;
}

.preview-image {
    position: relative;
    aspect-ratio: 1;
    border-radius: var(--border-radius-sm);
    overflow: hidden;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
}

.preview-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.preview-image .remove-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    width: 24px;
    height: 24px;
    background: rgba(255, 107, 107, 0.9);
    border: none;
    border-radius: 50%;
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    transition: var(--transition);
}

.preview-image .remove-btn:hover {
    background: rgba(255, 107, 107, 1);
    transform: scale(1.1);
}

.form-actions {
    display: flex;
    gap: 16px;
    justify-content: flex-end;
    margin-top: 32px;
    padding-top: 24px;
    border-top: 1px solid var(--border-color);
}

.form-actions .btn-modern {
    min-width: 120px;
}

/* Progress Indicator */
.progress-indicator {
    display: flex;
    justify-content: center;
    margin-bottom: 32px;
    animation: slideInDown 0.8s ease 0.1s both;
}

.progress-step {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-sm);
    color: var(--text-secondary);
    font-weight: 500;
    transition: var(--transition);
}

.progress-step.active {
    background: var(--secondary-gradient);
    color: white;
    border-color: #00d4aa;
    box-shadow: 0 4px 15px rgba(0, 212, 170, 0.3);
}

.progress-step.completed {
    background: rgba(67, 233, 123, 0.1);
    color: #43e97b;
    border-color: #43e97b;
}

.progress-step i {
    font-size: 1.1rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .create-package-hero h1 {
        font-size: 2rem;
    }
    
    .form-grid {
        grid-template-columns: 1fr;
    }
    
    .form-actions {
        flex-direction: column;
    }
    
    .progress-indicator {
        flex-direction: column;
        gap: 8px;
    }
    
    .create-package-hero,
    .form-section {
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
        <span class="breadcrumb-item active">Create Package</span>
    </div>

    <!-- Hero Section -->
    <div class="create-package-hero">
        <h1>Create New Package</h1>
        <p>Design and launch amazing travel experiences for your customers</p>
    </div>

    <!-- Progress Indicator -->
    <div class="progress-indicator">
        <div class="progress-step active">
            <i class="fa fa-edit"></i>
            <span>Package Details</span>
        </div>
        <div class="progress-step">
            <i class="fa fa-image"></i>
            <span>Images</span>
        </div>
        <div class="progress-step">
            <i class="fa fa-check"></i>
            <span>Review</span>
        </div>
    </div>

    <!-- Package Form -->
    <form method="post" enctype="multipart/form-data" class="form-section">
        <h2><i class="fa fa-suitcase"></i> Package Information</h2>
        
        <div class="form-grid">
            <div class="form-group">
                <label class="form-label">Package Name</label>
                <input type="text" name="packagename" class="form-input" placeholder="Enter package name" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Package Type</label>
                <select name="packagetype" class="form-input" required>
                    <option value="">Select package type</option>
                    <option value="Adventure">Adventure</option>
                    <option value="Relaxation">Relaxation</option>
                    <option value="Cultural">Cultural</option>
                    <option value="Business">Business</option>
                    <option value="Family">Family</option>
                </select>
            </div>
            
            <div class="form-group">
                <label class="form-label">Package Location</label>
                <input type="text" name="packagelocation" class="form-input" placeholder="Enter location" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Package Price</label>
                <input type="number" name="packageprice" class="form-input" placeholder="Enter price" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Package Features</label>
                <input type="text" name="packagefeatures" class="form-input" placeholder="Enter features (comma separated)" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Package Details</label>
                <textarea name="packagedetails" class="form-input form-textarea" placeholder="Enter detailed description" required></textarea>
            </div>
            
            <div class="form-group">
                <label class="form-label">Package Duration</label>
                <input type="text" name="packageduration" class="form-input" placeholder="e.g., 3 Days 2 Nights" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Package Date</label>
                <input type="date" name="packagedate" class="form-input" required>
            </div>
        </div>

        <!-- Image Upload Section -->
        <div class="form-section" style="margin-top: 32px;">
            <h2><i class="fa fa-image"></i> Package Images</h2>
            
            <div class="file-upload-modern">
                <input type="file" name="packageimage" id="packageimage" multiple accept="image/*">
                <label for="packageimage" class="file-upload-label">
                    <i class="fa fa-cloud-upload"></i>
                    <span>Click to upload package images</span>
                </label>
            </div>
            
            <div class="preview-images" id="preview-container"></div>
        </div>

        <!-- Form Actions -->
        <div class="form-actions">
            <button type="button" class="btn-modern warning" onclick="window.history.back()">
                <i class="fa fa-arrow-left"></i>
                Cancel
            </button>
            <button type="submit" name="submit" class="btn-modern success">
                <i class="fa fa-save"></i>
                Create Package
            </button>
        </div>
    </form>
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
    $('#packageimage').change(function() {
        const files = this.files;
        const previewContainer = $('#preview-container');
        previewContainer.empty();
        
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const preview = $(`
                        <div class="preview-image">
                            <img src="${e.target.result}" alt="Preview">
                            <button type="button" class="remove-btn" onclick="removePreview(this)">
                                <i class="fa fa-times"></i>
                            </button>
                        </div>
                    `);
                    previewContainer.append(preview);
                };
                reader.readAsDataURL(file);
            }
        }
    });
    
    // Form validation and enhancement
    $('form').on('submit', function(e) {
        const requiredFields = $(this).find('[required]');
        let isValid = true;
        
        requiredFields.each(function() {
            if (!$(this).val()) {
                isValid = false;
                $(this).addClass('error');
                $(this).focus();
                return false;
            } else {
                $(this).removeClass('error');
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            showAlert('Please fill in all required fields', 'warning');
        }
    });
    
    // Add input focus effects
    $('.form-input').focus(function() {
        $(this).parent().addClass('focused');
    }).blur(function() {
        $(this).parent().removeClass('focused');
    });
    
    // Add form section animations
    $('.form-section').each(function(index) {
        $(this).css('animation-delay', (0.2 + index * 0.1) + 's');
    });
});

// Remove preview image
function removePreview(button) {
    $(button).parent().fadeOut(300, function() {
        $(this).remove();
    });
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

// Add CSS for form enhancements
const style = document.createElement('style');
style.textContent = `
    .form-group.focused .form-label {
        color: #00d4aa;
    }
    
    .form-input.error {
        border-color: #ff6b6b;
        box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.1);
    }
    
    .form-input.error:focus {
        border-color: #ff6b6b;
        box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.2);
    }
`;
document.head.appendChild(style);
</script>
</body>
</html>
<?php } ?>