<?php

$servername = "localhost";
$username = "snoopy";
$password = "peanuts";
$dbname = "lablesdb";

$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
	die("Connection failed: ". mysqli_connect_error());
}

$sql = "SELECT sku, item, price FROM lableTable";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
	while($row = mysqli_fetch_assoc($result)) {
		echo "sku: " . $row["sku"]. " - item: " . $row["item"]. " - price: " . $row["price"]. "<br>";
	}
} else {
	echo "0 results";
}

mysqli_close($conn);

?>

