<?php
error_reporting(0);
if(isset($_POST['submit']))
{
$fname=$_POST['fname'];
$mnumber=$_POST['mobilenumber'];
$email=$_POST['email'];
$password=password_hash($_POST['password'], PASSWORD_DEFAULT);
$sql="INSERT INTO  tblusers(FullName,MobileNumber,EmailId,Password) VALUES(:fname,:mnumber,:email,:password)";
$query = $dbh->prepare($sql);
$query->bindParam(':fname',$fname,PDO::PARAM_STR);
$query->bindParam(':mnumber',$mnumber,PDO::PARAM_STR);
$query->bindParam(':email',$email,PDO::PARAM_STR);
$query->bindParam(':password',$password,PDO::PARAM_STR);
$query->execute();
$lastInsertId = $dbh->lastInsertId();
if($lastInsertId)
{
$_SESSION['msg']="You are Scuccessfully registered. Now you can login ";
header('location:thankyou.php');
}
else 
{
$_SESSION['msg']="Something went wrong. Please try again.";
header('location:thankyou.php');
}
}
?>
<!--Javascript for check email availabilty-->
<script>
function checkAvailability() {

$("#loaderIcon").show();
jQuery.ajax({
url: "check_availability.php",
data:'emailid='+$("#email").val(),
type: "POST",
success:function(data){
$("#user-availability-status").html(data);
$("#loaderIcon").hide();
},
error:function (){}
});
}
</script>

<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
				<div class="modal-dialog" role="document">
					<div class="modal-content">
						<div class="modal-header">
							<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>						
						</div>
							<section>
								<div class="modal-body modal-spa">
									<div class="login-grids">
										<div class="login-form-container">
                                            <div class="login-form-header">
                                                <h2 class="login-form-title">Create Account</h2>
                                                <p class="login-form-subtitle">Join us today!</p>
                                            </div>
                                            <form name="signup" method="post">
                                                <div class="form-group">
                                                    <label class="form-label">Full Name</label>
                                                    <input type="text" name="fname" class="form-input" placeholder="Enter your full name" required>
                                                </div>
                                                <div class="form-group">
                                                    <label class="form-label">Mobile Number</label>
                                                    <input type="text" name="mobilenumber" class="form-input" maxlength="10" placeholder="Enter your mobile number" required>
                                                </div>
                                                <div class="form-group">
                                                    <label class="form-label">Email</label>
                                                    <input type="email" name="email" class="form-input" id="email" onBlur="checkAvailability()" placeholder="Enter your email address" required>
                                                    <span id="user-availability-status" style="font-size:12px;"></span>
                                                </div>
                                                <div class="form-group">
                                                    <label class="form-label">Password</label>
                                                    <input type="password" name="password" class="form-input" placeholder="Enter your password" required>
                                                </div>
                                                <div class="form-actions">
                                                    <button type="submit" name="submit" id="submit" class="btn-primary">Create Account</button>
                                                </div>
                                            </form>
                                        </div>
											<p>By logging in you agree to our <a href="page.php?type=terms">Terms and Conditions</a> and <a href="page.php?type=privacy">Privacy Policy</a></p>
									</div>
								</div>
							</section>
					</div>
				</div>
			</div>