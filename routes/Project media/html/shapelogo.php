<!DOCTYPE html>
<html lang="en">
<head>
<?php 
 // include '\include-files\metadata.inc.html';
 // include '\include-files\offline_stylesheet.inc.html';
 // include 'include-files\localcssjs\logo\logo.inc.html'
 include '../html/inc/metadata.inc.html'; 
 include '../html/inc/online_stylesheet.inc.html';
 include '../html/inc/shapelogo.inc.html';
 ?>
<!--link href="http://projectmedia.net23.net/pm/css/logo.css" rel="stylesheet" type="text/css" media="screen">
<script src="http://projectmedia.net23.net/pm/js/logo.js"></script-->
<title> Kriss design -utvikling  | Shape logo</title>
</head>
<body>
<?php 
// include '\include-files\header.inc.html';
 include '../html/inc/header.inc.html'; 
?>
<main class="design">

<div id="carousel">
 <div class="slideshow fade">
 <img src="http://projectmedia.net23.net/pm/sample/Desert.jpg" class="img"">
 <div class="capiton"> Los Angels Desert </div>
</div>

<div class="slideshow fade">
 <img src="http://projectmedia.net23.net/pm/sample/Hydrangeas.jpg" class="img" ">
 <div class="capiton"> Rainforesst Hydrangeas </div>
</div>

<div class="slideshow fade">
 <img src="http://projectmedia.net23.net/pm/sample/Jellyfish.jpg" class="img">
 <div class="capiton"> Norwegian jellyfish</div>
</div>
</div>
<br>
<div id="indicator">
  <div class="indicator"></div>
  <div class="indicator"></div>
  <div class="indicator"></div>
</div>
</main>
<?php 
// include '\include-files\footer.inc.html';
 include '../html/inc/footer.inc.html';
?>
<script>  
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var carousel = document.getElementsByClassName("slideshow");
  var indicator = document.getElementsByClassName('indicator');
  for (i = 0; i < carousel.length; i++) {
    carousel[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex> carousel.length) {slideIndex = 1}
  for (i = 0; i < indicator.length; i++) {
      indicator[i].className = indicator[i].className.replace(" active", "");
    }
  carousel[slideIndex-1].style.display = "block";
  indicator[slideIndex-1].className += " active";
    setTimeout(showSlides,5000); // Timer (1000ms) = 1s
}
</script>
</body>
</html>