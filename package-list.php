<?php
session_start();
error_reporting(0);
include('includes/config.php');

// Search functionality
$search = isset($_GET['search']) ? $_GET['search'] : '';
$location_filter = isset($_GET['location']) ? $_GET['location'] : '';
$price_filter = isset($_GET['price']) ? $_GET['price'] : '';

// Build query with filters
$sql = "SELECT * from tbltourpackages WHERE 1=1";
$params = array();

if (!empty($search)) {
    $sql .= " AND (PackageName LIKE ? OR PackageLocation LIKE ? OR PackageFetures LIKE ?)";
    $search_param = "%$search%";
    $params[] = $search_param;
    $params[] = $search_param;
    $params[] = $search_param;
}

if (!empty($location_filter)) {
    $sql .= " AND PackageLocation LIKE ?";
    $params[] = "%$location_filter%";
}

if (!empty($price_filter)) {
    switch($price_filter) {
        case 'low':
            $sql .= " AND PackagePrice <= 5000";
            break;
        case 'medium':
            $sql .= " AND PackagePrice > 5000 AND PackagePrice <= 15000";
            break;
        case 'high':
            $sql .= " AND PackagePrice > 15000";
            break;
    }
}

$sql .= " ORDER BY PackagePrice ASC";

$query = $dbh->prepare($sql);
$query->execute($params);
$results = $query->fetchAll(PDO::FETCH_OBJ);
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Explore Destinations</title>
		<link rel="icon" type="image/png" href="admin/images/prayanam.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="applijewelleryion/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<link href="css/bootstrap.css" rel='stylesheet' type='text/css' />
<link href="css/style.css" rel='stylesheet' type='text/css' />
<link href='//fonts.googleapis.com/css?family=Open+Sans:400,700,600' rel='stylesheet' type='text/css'>
<link href='//fonts.googleapis.com/css?family=Roboto+Condensed:400,700,300' rel='stylesheet' type='text/css'>
<link href='//fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
<link href="css/font-awesome.css" rel="stylesheet">
<!-- Custom Theme files -->
<script src="js/jquery-1.12.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<!--animate-->
<link href="css/animate.css" rel="stylesheet" type="text/css" media="all">
<script src="js/wow.min.js"></script>
	<script>
		 new WOW().init();
	</script>
<!--//end-animate-->
<style>
/* Modern Package List Styles */
.page-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
    position: relative;
}

.page-header::before {
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

.page-header-content {
    position: relative;
    z-index: 2;
}

.page-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.page-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
}

.filters-section {
    background: white;
    padding: 30px 0;
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
}

.filter-form {
    display: flex;
    gap: 20px;
    align-items: center;
    flex-wrap: wrap;
}

.filter-group {
    flex: 1;
    min-width: 200px;
}

.filter-label {
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 8px;
    display: block;
}

.filter-input, .filter-select {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    font-size: 14px;
    transition: all 0.3s ease;
}

.filter-input:focus, .filter-select:focus {
    border-color: #3498db;
    outline: none;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.filter-btn {
    background: linear-gradient(45deg, #3498db, #2980b9);
    color: white;
    border: none;
    padding: 12px 25px;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
}

.filter-btn:hover {
    background: linear-gradient(45deg, #2980b9, #1f5f8b);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.packages-section {
    padding: 60px 0;
    background: #f8f9fa;
}

.packages-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.package-card {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    height: 100%;
}

.package-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
}

.package-image {
    height: 220px;
    overflow: hidden;
    position: relative;
}

.package-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.package-card:hover .package-image img {
    transform: scale(1.1);
}

.package-content {
    padding: 25px;
}

.package-name {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 10px;
    line-height: 1.3;
}

.package-type {
    background: #e8f4fd;
    color: #3498db;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 15px;
}

.package-location {
    color: #7f8c8d;
    font-size: 0.95rem;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.package-features {
    color: #34495e;
    font-size: 0.9rem;
    margin-bottom: 20px;
    line-height: 1.6;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.package-price {
    font-size: 1.8rem;
    font-weight: 700;
    color: #e74c3c;
    margin-bottom: 20px;
}

.view-details-btn {
    background: linear-gradient(45deg, #3498db, #2980b9);
    color: white;
    padding: 12px 25px;
    border-radius: 25px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    font-weight: 500;
    text-align: center;
    width: 100%;
}

.view-details-btn:hover {
    background: linear-gradient(45deg, #2980b9, #1f5f8b);
    color: white;
    text-decoration: none;
    transform: translateY(-2px);
}

.no-results {
    text-align: center;
    padding: 60px 20px;
    color: #7f8c8d;
}

.no-results i {
    font-size: 4rem;
    margin-bottom: 20px;
    color: #bdc3c7;
}

.results-count {
    text-align: center;
    margin-bottom: 30px;
    color: #7f8c8d;
    font-size: 1.1rem;
}

@media (max-width: 768px) {
    .page-title {
        font-size: 2.2rem;
    }
    
    .filter-form {
        flex-direction: column;
        gap: 15px;
    }
    
    .filter-group {
        width: 100%;
    }
    
    .packages-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
}
</style>
</head>
<body>
<?php include('includes/header.php');?>

<!-- Page Header -->
<div class="page-header">
    <div class="page-header-content">
        <div class="container">
            <h1 class="page-title wow fadeInUp" data-wow-delay="0.3s">Explore Amazing Destinations</h1>
            <p class="page-subtitle wow fadeInUp" data-wow-delay="0.5s">Discover the perfect travel package for your next adventure</p>
        </div>
    </div>
</div>

<!-- Filters Section -->
<div class="filters-section">
    <div class="container">
        <form method="GET" class="filter-form">
            <div class="filter-group">
                <label class="filter-label">Search Destinations</label>
                <input type="text" name="search" class="filter-input" placeholder="Search packages, locations..." value="<?php echo htmlspecialchars($search); ?>">
            </div>
            
            <div class="filter-group">
                <label class="filter-label">Location</label>
                <input type="text" name="location" class="filter-input" placeholder="Enter location..." value="<?php echo htmlspecialchars($location_filter); ?>">
            </div>
            
            <div class="filter-group">
                <label class="filter-label">Price Range</label>
                <select name="price" class="filter-select">
                    <option value="">All Prices</option>
                    <option value="low" <?php echo $price_filter == 'low' ? 'selected' : ''; ?>>Under ₹5,000</option>
                    <option value="medium" <?php echo $price_filter == 'medium' ? 'selected' : ''; ?>>₹5,000 - ₹15,000</option>
                    <option value="high" <?php echo $price_filter == 'high' ? 'selected' : ''; ?>>Above ₹15,000</option>
                </select>
            </div>
            
            <div class="filter-group">
                <label class="filter-label">&nbsp;</label>
                <button type="submit" class="filter-btn">
                    <i class="fa fa-search"></i> Search
                </button>
            </div>
        </form>
    </div>
</div>

<!-- Packages Section -->
<div class="packages-section">
    <div class="container">
        <div class="results-count">
            Found <?php echo $query->rowCount(); ?> package<?php echo $query->rowCount() != 1 ? 's' : ''; ?>
        </div>
        
        <?php if($query->rowCount() > 0) { ?>
            <div class="packages-grid">
                <?php 
                $cnt = 1;
                foreach($results as $result) { ?>
                    <div class="package-card wow fadeInUp" data-wow-delay="<?php echo $cnt * 0.1; ?>s">
                        <div class="package-image">
                            <img src="admin/pacakgeimages/<?php $images = json_decode($result->pacakgeimages); echo htmlentities($images[0]);?>" alt="<?php echo htmlentities($result->PackageName);?>">
                        </div>
                        <div class="package-content">
                            <h3 class="package-name"><?php echo htmlentities($result->PackageName);?></h3>
                            <span class="package-type"><?php echo htmlentities($result->PackageType);?></span>
                            <p class="package-location">
                                <i class="fa fa-map-marker"></i> <?php echo htmlentities($result->PackageLocation);?>
                            </p>
                            <p class="package-features"><?php echo htmlentities($result->PackageFeatures);?></p>
                            <div class="package-price">₹<?php echo htmlentities($result->PackagePrice);?></div>
                            <a href="package-details.php?pkgid=<?php echo htmlentities($result->PackageId);?>" class="view-details-btn">View Details</a>
                        </div>
                    </div>
                <?php $cnt++; } ?>
            </div>
        <?php } else { ?>
            <div class="no-results">
                <i class="fa fa-search"></i>
                <h3>No packages found</h3>
                <p>Try adjusting your search criteria or browse all our packages.</p>
                <a href="package-list.php" class="view-details-btn" style="width: auto; margin-top: 20px;">View All Packages</a>
            </div>
        <?php } ?>
    </div>
</div>

<?php include('includes/footer.php');?>
<!-- signup -->
<?php include('includes/signup.php');?>			
<!-- //signu -->
<!-- signin -->
<?php include('includes/signin.php');?>			
<!-- //signin -->
<!-- write us -->
<?php include('includes/write-us.php');?>			
<!-- //write us -->
</body>
</html>