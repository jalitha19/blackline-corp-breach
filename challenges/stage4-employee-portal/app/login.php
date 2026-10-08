<?php

session_start();

require_once "db.php";


if ($_SERVER["REQUEST_METHOD"] !== "POST") {

    header("Location: index.php");

    exit;

}


$username = $_POST["username"] ?? "";

$password = $_POST["password"] ?? "";


/*
    INTENTIONALLY VULNERABLE CTF CODE

    This query directly concatenates player input.

    It exists ONLY inside the isolated
    Blackline Corp university CTF environment.
*/

$sql = "SELECT id, employee_id, username, full_name, department, role, status "
     . "FROM users "
     . "WHERE username = '$username' AND password = '$password' LIMIT 1";


$result = $conn->query($sql);


if ($result && $result->num_rows > 0) {

    $account = $result->fetch_assoc();


    $_SESSION["authenticated"] = true;

    $_SESSION["username"] =
        $account["username"];

    $_SESSION["full_name"] =
        $account["full_name"];

    $_SESSION["employee_id"] =
        $account["employee_id"];

    $_SESSION["department"] =
        $account["department"];

    $_SESSION["role"] =
        $account["role"];


    header("Location: dashboard.php");

    exit;

}


header("Location: index.php?error=1");

exit;

?>