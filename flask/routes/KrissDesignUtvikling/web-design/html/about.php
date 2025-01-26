<?php 
  include '../../bibliotek/php/inc/metadata.inc.php';
  include '../../bibliotek/php/function/tittel.php';
 ?>
  <?php
    Title($Kriss, 'About');
?>
 <link href="../css/about.css" rel="stylesheet" type="text/css" media="screen">
<script src="../../bibliotek/js/mainpages/about.js">
</script>
<script src="../../bibliotek/js/skill/circlebar/skillbar.js"></script>
</head>
<body>
<?php 
 include '../../bibliotek/php/inc/header.inc.php';
?>
<main class="background">
<div class="instadesign">
<img src="../../portfolio/photoshoots/designer/DSC_0157.jpg" alt="Picture of the designer" class="imgdesign">
<div class="overlay">
  <div class="capiton"> 
  Contact info: <br>
  Mail:<br>
  krigjo25@gmail.com<br>
  </div>
 </div>
</div>
<div id="bars">
  <div class="webdesign" data-percent="48.33">
    <h3><strong>&#35;</strong>Web-Design (HTML, CSS &amp; JavaScript)</h3>
    <canvas class="bar-circle" width="70" height="70"></canvas>
  </div>
  <div class="program" data-percent="10">
    <h3><strong>&#35;</strong>php</h3>
    <canvas class="bar-circle" width="70" height="70"></canvas>
  </div>
  <div class="db" data-percent="3">
    <h3><strong>&#35;</strong> Mysql</h3>
    <canvas class="bar-circle" width="70" height="70"></canvas>
  </div>
  <div class="graphics" data-percent="25">
    <h3><strong>&#35;</strong>Graphic Design (PS / vector)</h3>
    <canvas class="bar-circle" width="70" height="70"></canvas>
  </div>
</div>  

</main>
<?php 
 include '../../bibliotek/php/inc/footer.inc.php';
?>
