<?php
$message = $_POST['message'];
$formcontent=" From: $name \n Message: $message";
$recipient = "krigjo25@gmail.com";
$subject = "Feedback form";
$mailheader = "From: projectmedia.com \r\n";
mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
echo "Thank You!";
?>