<?php
session_start();
include('includes/config.php');

echo "<h2>Create Default Admin User</h2>";

// Check if admin table exists
try {
    $table_query = $dbh->query("SHOW TABLES LIKE 'admin'");
    if ($table_query->rowCount() == 0) {
        echo "❌ Admin table does not exist. Creating it now...<br>";
        
        // Create admin table
        $create_table = "CREATE TABLE admin (
            id int(11) NOT NULL AUTO_INCREMENT,
            UserName varchar(50) NOT NULL,
            Password varchar(255) NOT NULL,
            PRIMARY KEY (id)
        )";
        
        $dbh->exec($create_table);
        echo "✅ Admin table created successfully<br>";
    } else {
        echo "✅ Admin table already exists<br>";
    }
} catch (PDOException $e) {
    echo "❌ Error with admin table: " . $e->getMessage() . "<br>";
    exit;
}

// Check if admin users exist
try {
    $check_users = $dbh->query("SELECT COUNT(*) as count FROM admin");
    $user_count = $check_users->fetch(PDO::FETCH_ASSOC)['count'];
    
    if ($user_count == 0) {
        echo "❌ No admin users found. Creating default admin...<br>";
        
        // Create default admin user
        $default_username = "admin";
        $default_password = "admin123"; // You can change this
        $hashed_password = password_hash($default_password, PASSWORD_DEFAULT);
        
        $insert_admin = "INSERT INTO admin (UserName, Password) VALUES (:username, :password)";
        $stmt = $dbh->prepare($insert_admin);
        $stmt->bindParam(':username', $default_username, PDO::PARAM_STR);
        $stmt->bindParam(':password', $hashed_password, PDO::PARAM_STR);
        $stmt->execute();
        
        echo "✅ Default admin user created successfully!<br>";
        echo "Username: <strong>" . $default_username . "</strong><br>";
        echo "Password: <strong>" . $default_password . "</strong><br>";
        echo "<br><strong>Please change this password after first login!</strong><br>";
    } else {
        echo "✅ Admin users already exist (" . $user_count . " users)<br>";
    }
} catch (PDOException $e) {
    echo "❌ Error creating admin user: " . $e->getMessage() . "<br>";
}

// Show current admin users
echo "<h3>Current Admin Users:</h3>";
try {
    $users_query = $dbh->query("SELECT * FROM admin");
    if ($users_query->rowCount() > 0) {
        echo "<table border='1'>";
        echo "<tr><th>ID</th><th>Username</th><th>Password (MD5)</th></tr>";
        while ($row = $users_query->fetch(PDO::FETCH_ASSOC)) {
            echo "<tr>";
            echo "<td>" . $row['id'] . "</td>";
            echo "<td>" . $row['UserName'] . "</td>";
            echo "<td>" . $row['Password'] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    }
} catch (PDOException $e) {
    echo "❌ Error getting admin users: " . $e->getMessage() . "<br>";
}
?>

<br><br>
<a href="index.php">Go to Admin Login</a> | 
<a href="debug_login.php">Debug Login</a> 