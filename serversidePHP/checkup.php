<?php

$servername = "localhost";
$username = "snoopy";
$password = "peanuts";
$dbname = "lablesdb";

$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
	die("Connection failed: ". mysqli_connect_error());
}

$sql = "SELECT flag FROM lableTable where sku = 255255255";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
	while($row = mysqli_fetch_assoc($result)) {
		echo $row["flag"];
	}
} else {
	echo "0 results";
}

mysqli_close($conn);

?>

