<?php

$servername = "localhost";
$username = "snoopy";
$password = "peanuts";
$dbname = "lablesdb";

$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "UPDATE lableTable SET flag ='N' WHERE sku = 255255255";

if (mysqli_query($conn, $sql)) {
  echo "Record updated successfully";
} else {
  echo "Error updating record: " . mysqli_error($conn);
}

mysqli_close($conn);
?>
