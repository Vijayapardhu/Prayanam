<?php
session_start();
error_reporting(0);
include('includes/config.php');
?>
<!DOCTYPE HTML>
<html>
<head>
		<title>Prayanam | Discover Amazing Destinations</title>
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
/* Holidify-inspired Modern Design */
.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 100px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.hero-section::before {
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

.hero-content {
    position: relative;
    z-index: 2;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.hero-subtitle {
    font-size: 1.3rem;
    margin-bottom: 40px;
    opacity: 0.9;
}

.search-box {
    background: white;
    border-radius: 50px;
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    max-width: 600px;
    margin: 0 auto;
}

.search-input {
    border: none;
    outline: none;
    padding: 15px 20px;
    border-radius: 25px;
    width: 70%;
    font-size: 16px;
}

.search-btn {
    background: linear-gradient(45deg, #ff6b6b, #ee5a24);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 25px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.search-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.featured-destinations {
    padding: 80px 0;
    background: #f8f9fa;
}

.section-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 50px;
    color: #2c3e50;
}

.package-card {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    margin-bottom: 30px;
    height: 100%;
}

.package-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
}

.package-image {
    height: 200px;
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
    padding: 20px;
}

.package-name {
    font-size: 1.3rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 10px;
}

.package-location {
    color: #7f8c8d;
    font-size: 0.9rem;
    margin-bottom: 10px;
}

.package-features {
    color: #34495e;
    font-size: 0.9rem;
    margin-bottom: 15px;
    line-height: 1.5;
}

.package-price {
    font-size: 1.5rem;
    font-weight: 700;
    color: #e74c3c;
    margin-bottom: 15px;
}

.view-details-btn {
    background: linear-gradient(45deg, #3498db, #2980b9);
    color: white;
    padding: 10px 20px;
    border-radius: 25px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    font-weight: 500;
}

.view-details-btn:hover {
    background: linear-gradient(45deg, #2980b9, #1f5f8b);
    color: white;
    text-decoration: none;
    transform: translateY(-2px);
}

.stats-section {
    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
    color: white;
    padding: 60px 0;
}

.stat-item {
    text-align: center;
    padding: 20px;
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: #3498db;
    margin-bottom: 10px;
}

.stat-label {
    font-size: 1.1rem;
    opacity: 0.9;
}

.destinations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 2.5rem;
    }
    
    .search-box {
        padding: 15px;
    }
    
    .search-input {
        width: 100%;
        margin-bottom: 15px;
    }
    
    .destinations-grid {
        grid-template-columns: 1fr;
    }
}
</style>
</head>
<body>
<?php include('includes/header.php');?>

<!-- Hero Section -->
<div class="hero-section">
    <div class="hero-content">
        <div class="container">
            <h1 class="hero-title wow fadeInUp" data-wow-delay="0.3s">Discover Amazing Destinations</h1>
            <p class="hero-subtitle wow fadeInUp" data-wow-delay="0.5s">Explore the world with Prayanam - Your trusted travel companion</p>
            
            <div class="search-box wow fadeInUp" data-wow-delay="0.7s">
                <form action="package-list.php" method="GET">
                    <input type="text" name="search" class="search-input" placeholder="Where do you want to go?">
                    <button type="submit" class="search-btn">
                        <i class="fa fa-search"></i> Search
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Featured Destinations -->
<div class="featured-destinations">
    <div class="container">
        <h2 class="section-title wow fadeInUp" data-wow-delay="0.3s">Featured Destinations</h2>
        
        <div class="destinations-grid">
            <?php 
            $sql = "SELECT * from tbltourpackages order by rand() limit 6";
            $query = $dbh->prepare($sql);
            $query->execute();
            $results=$query->fetchAll(PDO::FETCH_OBJ);
            $cnt=1;
            if($query->rowCount() > 0) {
                foreach($results as $result) { ?>
                    <div class="package-card wow fadeInUp" data-wow-delay="<?php echo $cnt * 0.1; ?>s">
                        <div class="package-image">
                            <img src="admin/pacakgeimages/<?php echo htmlentities($result->PackageImage);?>" alt="<?php echo htmlentities($result->PackageName);?>">
                        </div>
                        <div class="package-content">
                            <h3 class="package-name"><?php echo htmlentities($result->PackageName);?></h3>
                            <p class="package-location">
                                <i class="fa fa-map-marker"></i> <?php echo htmlentities($result->PackageLocation);?>
                            </p>
                            <p class="package-features"><?php echo htmlentities(substr($result->PackageFetures, 0, 100));?>...</p>
                            <div class="package-price">₹<?php echo htmlentities($result->PackagePrice);?></div>
                            <a href="package-details.php?pkgid=<?php echo htmlentities($result->PackageId);?>" class="view-details-btn">View Details</a>
                        </div>
                    </div>
                <?php $cnt++; }
            } ?>
        </div>
        
        <div class="text-center" style="margin-top: 40px;">
            <a href="package-list.php" class="view-details-btn" style="padding: 15px 30px; font-size: 1.1rem;">
                View All Packages
            </a>
        </div>
    </div>
</div>

<!-- Stats Section -->
<div class="stats-section">
    <div class="container">
        <div class="row">
            <div class="col-md-4">
                <div class="stat-item wow fadeInUp" data-wow-delay="0.3s">
                    <div class="stat-number">80,000+</div>
                    <div class="stat-label">Happy Travelers</div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="stat-item wow fadeInUp" data-wow-delay="0.5s">
                    <div class="stat-number">1,900+</div>
                    <div class="stat-label">Destinations</div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="stat-item wow fadeInUp" data-wow-delay="0.7s">
                    <div class="stat-number">7M+</div>
                    <div class="stat-label">Successful Bookings</div>
                </div>
            </div>
        </div>
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