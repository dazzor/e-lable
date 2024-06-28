<?php

$servername = "localhost";
$username = "snoopy";
$password = "peanuts";

$conn = mysqli_connect($servername, $username, $password);

if (!$conn) {
	die("Connection failed: ". mysqli_connect_error());
}

echo "Connected successfully";

?>

