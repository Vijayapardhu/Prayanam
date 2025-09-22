<?php
session_start();
if(isset($_POST['signin']))
{
$email=$_POST['email'];
$password=$_POST['password'];
$sql ="SELECT EmailId,Password FROM tblusers WHERE EmailId=:email";
$query= $dbh -> prepare($sql);
$query-> bindParam(':email', $email, PDO::PARAM_STR);
$query-> execute();
$results=$query->fetchAll(PDO::FETCH_OBJ);
if($query->rowCount() > 0)
{
    foreach ($results as $result) {
        if (password_verify($password, $result->Password)) {
            $_SESSION['login']=$_POST['email'];
            echo "<script type='text/javascript'> document.location = 'package-list.php'; </script>";
        } else {
            echo "<script>alert('Invalid Details');</script>";
        }
    }
} else{
	
echo "<script>alert('Invalid Details');</script>";

}

}

?>

<div class="modal fade" id="myModal4" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
				<div class="modal-dialog" role="document">
					<div class="modal-content modal-info">
						<div class="modal-header">
							<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>						
						</div>
						<div class="modal-body modal-spa">
							<div class="login-grids">
								<div class="login-form-container">
                                    <div class="login-form-header">
                                        <h2 class="login-form-title">Sign In</h2>
                                        <p class="login-form-subtitle">Access your account</p>
                                    </div>
                                    <form method="post">
                                        <div class="form-group">
                                            <label class="form-label">Email</label>
                                            <input type="email" name="email" class="form-input" placeholder="Enter your email" required>
                                        </div>
                                        <div class="form-group">
                                            <label class="form-label">Password</label>
                                            <input type="password" name="password" class="form-input" placeholder="Enter your password" required>
                                        </div>
                                        <div class="form-actions">
                                            <button type="submit" name="signin" class="btn-primary">Sign In</button>
                                        </div>
                                        <div class="text-center mt-3">
                                            <a href="forgot-password.php" class="forgot-password-link">Forgot Password?</a>
                                        </div>
                                    </form>
                                </div>
								<p>By logging in you agree to our <a href="page.php?type=terms">Terms and Conditions</a> and <a href="page.php?type=privacy">Privacy Policy</a></p>
							</div>
						</div>
					</div>
				</div>
			</div>