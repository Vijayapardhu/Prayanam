<?php
error_reporting(0);
if(isset($_POST['submit']))
{
$issue=$_POST['issue'];
$description=$_POST['description'];
$email=$_SESSION['login'];
$sql="INSERT INTO  tblissues(UserEmail,Issue,Description) VALUES(:email,:issue,:description)";
$query = $dbh->prepare($sql);
$query->bindParam(':issue',$issue,PDO::PARAM_STR);
$query->bindParam(':description',$description,PDO::PARAM_STR);
$query->bindParam(':email',$email,PDO::PARAM_STR);
$query->execute();
$lastInsertId = $dbh->lastInsertId();
if($lastInsertId)
{
$_SESSION['msg']="Info successfully submited ";
echo "<script type='text/javascript'> document.location = 'thankyou.php'; </script>";
}
else 
{
$_SESSION['msg']="Something went wrong. Please try again.";
echo "<script type='text/javascript'> document.location = 'thankyou.php'; </script>";
}
}
?>	

	<div class="modal fade" id="myModal3" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
				<div class="modal-dialog" role="document">
					<div class="modal-content">
						<div class="modal-header">
							<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>						
						</div>
							<section>
							<form name="help" method="post">
								<div class="modal-body modal-spa">
									<div class="write-us-form-container">
                                            <div class="write-us-form-header">
                                                <h2 class="write-us-form-title">How Can We Help You?</h2>
                                                <p class="write-us-form-subtitle">Submit your issue ticket below.</p>
                                            </div>
                                            <form name="help" method="post">
                                                <div class="form-group">
                                                    <label class="form-label">Select Issue</label>
                                                    <select id="country" name="issue" class="form-input" required>
                                                        <option value="">Select Issue</option> 		
                                                        <option value="Booking Issues">Booking Issues</option>
                                                        <option value="Cancellation"> Cancellation</option>
                                                        <option value="Refund">Refund</option>
                                                        <option value="Other">Other</option>														
                                                    </select>
                                                </div>
                                                <div class="form-group">
                                                    <label class="form-label">Description</label>
                                                    <textarea class="form-input" name="description" rows="6" placeholder="Detailed description of your issue" required></textarea>
                                                </div>
                                                <div class="form-actions">
                                                    <button type="submit" name="submit" class="btn-primary">Submit Issue</button>
                                                </div>
                                            </form>
                                        </div>
								</div>
								</form>
							</section>
					</div>
				</div>
			</div>