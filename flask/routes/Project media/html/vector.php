<!doctype html>
<html lang="en">
<head>
<?php 
// include '\include-files\metadata.inc.html';
// include '\include-files\offline_stylesheet.inc.html';
// include '\include-files\localcssjs\graphics\vector.inc.html';
 include '../html/inc/metadata.inc.html'; 
 include '../html/inc/online_stylesheet.inc.html'; ?>

<link href="http://projectmedia.net23.net/pm/css/vector.css" rel="stylesheet" type="text/css" media="screen">
<script src="http://projectmedia.net23.net/pm/js/vector.js"></script>

<script src="http://projectmedia.net23.net/pm/js/lightbox.js"></script>

<title>Kriss design / utvikling | Vector graphics</title>
</head>
<body>
<?php 
// include '\include-files\header.inc.html';
 include '../html/inc/header.inc.html';  
?>
<main class="design">
<!--Lightbox-->
<!-- The Image Table -->
  <div class="row">
    <div class="column">
    <img src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/transparancy/Owl-transparacy.png" onclick="modalOpen(); currentSwitch(1)" class="cursor hover-shadow">
    </div>
    <!--<div class="column">
    <img src="" onclick="Openmodal();currentModal(2)" class="cursor hover-shadow">
    </div>
    <div class="column">
    <img src="" onclick="Openmodal();currentModal(3)" class="cursor hover-shadow">
    </div>
        <div class="column">
    <img src="" onclick="Openmodal();currentModal(4)" class="cursor hover-shadow">
    </div-->
  </div>
<!-- End of the Table-->
<!-- Modal box -->
<div id="lightbox" class="modal">
<span class="close" onclick="modalClose()">×</span>
<div class="modal-graphics">

  <div class="modalSlide">
    <div class="nr"> 1 / 4</div>
    <img src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/Owl.png" width="25%">
  </div>

  <div class="modalSlide">
    <div class="nr"> 2 / 4</div>
    <img src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/Owl.png" width="25%">
  </div>

  <div class="modalSlide">
    <div class="nr"> 3 / 4</div>
    <img src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/Owl.png" width="25%">
  </div>
<!--End of the modal box-->

<!-- Previous & next buttons-->
  <a class="prev" onclick="toggleSwitch(-1)">❮</a>
  <a class="next" onclick="toggleSwitch(1)">❯</a>
  
  <div class="caption">
    <p id="caption"></p>
  </div>

  <div class="column">
    <img class="ms cursor" src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/Owl.png" onclick="currentSwitch(1)" alt="Paper Owl">
    </div>
    <div class="column">
      <img class="ms cursor" src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/Owl.png" onclick="currentSwitch(2)" alt="Triangle Owl">
    </div>
     <div class="column">
      <img class="ms cursor" src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/Owl.png" onclick="currentSwitch(3)" alt="Circled Owl">
    </div>
     <div class="column">
      <img class="ms cursor" src="http://projectmedia.net23.net/pm/portfolio/graphics/vector/Owl.png" onclick="currentSwitch(4)" alt="X Owl">
    </div>
  </div>
</div>

</main>
<?php 

// include '\include-files\footer.inc.html';
 include '../html/inc/footer.inc.html';
?>
</body>
</html>
