<?php

$servername = "localhost";
$username = "snoopy";
$password = "peanuts";
$dbname = "lablesdb";

echo "we're here";

$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
	die("Connection failed: ". mysqli_connect_error());
}

?>

