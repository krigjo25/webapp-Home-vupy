<?php 
 include '../../bibliotek/php/inc/metadata.inc.php';

 ?>
 <link href="../css/portfolio.css" rel="stylesheet" type="text/css" media="screen">
<!--
<script src="/logo.js"></script>
<script src="/video.js"></script>
<script src="/vector.js"></script>-->
 <?php
 include '../../bibliotek/php/function/tittel.php';
    Title($Kriss, 'portfolio');

 include '../../bibliotek/php/inc/header.inc.php'; 
?>
<main class="background">
<div class='pageOption'>
  <a href='../html/animations.php' class='option' data-inf='animations'>
    <img src='../../portfolio/portfolio/animation.jpg'>
  </a>
 <div class="capiton"> Media </div>
 <div class="capiton"> Animations </div>
  <a href='../html/media.php' class='option' data-inf='Vector'>
    <img src='../../portfolio/portfolio/animation.jpg'>
  </a>
</div>
<div class='pageOption'>
  <a href='../html/photoshoot.php' class='option' data-inf='photoshoot'>
    <img src='../../portfolio/portfolio/graphic.jpg'>
  </a>
 <div class="capiton"> Vector </div>
 <div class="capiton"> Photoshoot </div>
  <a href='../html/vector.php' class='option' data-inf='Vector'>
    <img src='../../portfolio/portfolio/graphic.jpg'>
  </a>
</div>
<div class='pageOption'>
  <a href='../html/logo.php' class='option' data-inf='type logo'>
    <img src='../../portfolio/portfolio/logo.jpg'>
  </a>
 <div class="capiton"> Shape logo </div>
 <div class="capiton"> Typographic logo </div>
  <a href='../html/shapelogo.php' class='option' data-inf='Logo shape'>
    <img src='../../portfolio/portfolio/logo.jpg'>
  </a>
</div>

<div class='pageOption'>
  <a href='../html/screencastprev.php' class='option' data-inf='previous web-projects'>
    <img src='../../portfolio/portfolio/logo.jpg'>
  </a>
 <div class="capiton"> Current Web-project </div>
 <div class="capiton"> Previously Web-projects </div>
  <a href='../html/screencast current.php' class='option' data-inf='current / next web-project'>
    <img src='../../portfolio/portfolio/logo.jpg'>
  </a>
</div>
</main>
<?php 
 include '../../bibliotek/php/inc/footer.inc.php';
?>