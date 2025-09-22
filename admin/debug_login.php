<?php
session_start();
include('includes/config.php');

echo "<h2>Admin Login Debug Information</h2>";

// Test database connection
echo "<h3>1. Database Connection Test:</h3>";
try {
    $test_query = $dbh->query("SELECT 1");
    echo "✅ Database connection successful<br>";
} catch (PDOException $e) {
    echo "❌ Database connection failed: " . $e->getMessage() . "<br>";
    exit;
}

// Check if admin table exists
echo "<h3>2. Admin Table Check:</h3>";
try {
    $table_query = $dbh->query("SHOW TABLES LIKE 'admin'");
    if ($table_query->rowCount() > 0) {
        echo "✅ Admin table exists<br>";
    } else {
        echo "❌ Admin table does not exist<br>";
        exit;
    }
} catch (PDOException $e) {
    echo "❌ Error checking admin table: " . $e->getMessage() . "<br>";
    exit;
}

// Show admin table structure
echo "<h3>3. Admin Table Structure:</h3>";
try {
    $structure_query = $dbh->query("DESCRIBE admin");
    echo "<table border='1'>";
    echo "<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>";
    while ($row = $structure_query->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr>";
        echo "<td>" . $row['Field'] . "</td>";
        echo "<td>" . $row['Type'] . "</td>";
        echo "<td>" . $row['Null'] . "</td>";
        echo "<td>" . $row['Key'] . "</td>";
        echo "<td>" . $row['Default'] . "</td>";
        echo "<td>" . $row['Extra'] . "</td>";
        echo "</tr>";
    }
    echo "</table>";
} catch (PDOException $e) {
    echo "❌ Error getting table structure: " . $e->getMessage() . "<br>";
}

// Show admin table data
echo "<h3>4. Admin Table Data:</h3>";
try {
    $data_query = $dbh->query("SELECT * FROM admin");
    if ($data_query->rowCount() > 0) {
        echo "<table border='1'>";
        echo "<tr><th>ID</th><th>Username</th><th>Password (MD5)</th></tr>";
        while ($row = $data_query->fetch(PDO::FETCH_ASSOC)) {
            echo "<tr>";
            echo "<td>" . (isset($row['id']) ? $row['id'] : 'N/A') . "</td>";
            echo "<td>" . $row['UserName'] . "</td>";
            echo "<td>" . $row['Password'] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "❌ No admin users found in the table<br>";
    }
} catch (PDOException $e) {
    echo "❌ Error getting admin data: " . $e->getMessage() . "<br>";
}

// Test login with sample credentials
echo "<h3>5. Login Test:</h3>";
if (isset($_POST['test_login'])) {
    $test_username = $_POST['test_username'];
    $test_password = $_POST['test_password'];
    
    echo "Testing login with:<br>";
    echo "Username: " . $test_username . "<br>";
    echo "Password (plain text): " . md5($test_password) . "<br><br>";
    
    $sql = "SELECT UserName,Password FROM admin WHERE UserName=:uname";
    $query = $dbh->prepare($sql);
    $query->bindParam(':uname', $test_username, PDO::PARAM_STR);
    $query->execute();
    $result = $query->fetch(PDO::FETCH_OBJ);
    
    if ($result && password_verify($test_password, $result->Password)) {
        echo "✅ Login test successful!<br>";
    } else {
        echo "❌ Login test failed!<br>";
        
        // Check if username exists
        $check_user = $dbh->prepare("SELECT UserName FROM admin WHERE UserName=:uname");
        $check_user->bindParam(':uname', $test_username, PDO::PARAM_STR);
        $check_user->execute();
        
        if ($check_user->rowCount() > 0) {
            echo "Username exists but password is incorrect<br>";
        } else {
            echo "Username does not exist<br>";
        }
    }
}
?>

<form method="post">
    <h4>Test Login:</h4>
    Username: <input type="text" name="test_username" required><br>
    Password: <input type="password" name="test_password" required><br>
    <input type="submit" name="test_login" value="Test Login">
</form>

<br><br>
<a href="index.php">Back to Admin Login</a> 