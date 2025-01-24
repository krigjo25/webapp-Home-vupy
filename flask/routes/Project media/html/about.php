<?php 
 include '..\html\include-files\metadata.inc.php';

 ?>
 <link href="static/about.css" rel="stylesheet" type="text/css" media="screen">
<script src="resources/js/about.js"></script>
<script src="resources/js/skillbar.js"></script>

<?php
    Title('K-design / utvikling |  About');
?>
</head>
<body>
<?php 
 include '\include-files\header.inc.php';
 // include '../html/inc/header.inc.html';
?>
<main class="background">
<div class="instadesign">
<img src="http://projectmedia.net23.net/pm/portfolio/chips/DSC_0157.jpg" alt="Picture of the designer" class="imgdesign">
<div class="overlay">
  <div class="capiton"> 
  Contact info: <br>
  Mail:<br>
  krigjo25@gmail.com<br>
  </div>
 </div>
</div>
<div id="bars">
  <div class="webdesign" data-percent="70.0">
    <h3><strong>&#35;</strong>Web-Design (HTML, CSS &amp; JavaScript)</h3>
    <canvas class="bar-circle" width="70" height="70"></canvas>
  </div>
  <div class="program" data-percent="25">
    <h3><strong>&#35;</strong>PHP</h3>
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
 include '\include-files\footer.inc.php';
//  include '../html/inc/footer.inc.html';
?>
