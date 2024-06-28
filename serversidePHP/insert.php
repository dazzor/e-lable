<?php
include_once 'db.php';

echo '<br>';
echo 'snot';
echo '<br>';

$sku = $_POST['sku'];
$price = $_POST['price'];

echo '<br>';
echo $sku;
echo '<br>';
echo $price;
echo '<br>';

$sql = "UPDATE lableTable set price='$price', flag='Y' WHERE sku='$sku'";

echo $sql;
echo'<br>';

if (mysqli_query($conn, $sql)) {
	echo "Record has been updated successfully !";
} else {
	echo "Error: " . $sql . ":-" . mysqli_error($conn);
}

?>

