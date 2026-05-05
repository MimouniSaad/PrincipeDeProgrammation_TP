<?php

$url = "http://localhost:5000/students";
$response = file_get_contents($url) ;

//decodage JSON en tableau PHP
$students = json_decode($response,true) ;

echo "<pre>";
print_r($students);
echo "</pre>";
?>