<?php

$host = getenv("DB_HOST") ?: "database";
$db   = getenv("DB_NAME") ?: "blackline_portal";
$user = getenv("DB_USER") ?: "blackline";
$pass = getenv("DB_PASSWORD") ?: "blackline_lab_password";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {

    http_response_code(500);

    die("Portal database connection unavailable.");

}

$conn->set_charset("utf8mb4");

?>