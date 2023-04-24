<?php

    $name = $_POST["name"];
    $email = $_POST["mail"];
    $phone = $_POST["phone"];
    $message = $_POST["message"];

    $conn = mysqli_connect("localhost", "root", "", "water_quality") or die("connection failed");

    $sql = "INSERT INTO water(name, email, phone, text) VALUES ( '{$name}', '{$email}', '{$phone}', '{$message}')";

    $result = mysqli_query($conn, $sql) or die("Failed");
    mysqli_close($conn);
?>