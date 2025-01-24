<?php 
 include '..\..\bibliotek\php\inc\metadata.inc.php';

 ?>
 <link href="../css/vector.css" rel="stylesheet" type="text/css" media="screen">
<script src="../js/vector.js"></script>
<script src="../js/lightbox.js"></script>
<?php
 include '../../bibliotek/php/function/tittel.php';
    Title($Kriss, 'Vector');
?>
<body>
<?php 
 include '../../bibliotek/php/inc/header.inc.php';  
?>
<main class="design">
<!--Lightbox-->
<!-- The Image Table -->
  <div class="row">
    <div class="column">
    <img src="../../portfolio/vector/Owl.svg" onclick="modalOpen(); currentSwitch(1)" class="cursor hover-shadow">
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
    <img src="../../portfolio/vector/Owl.svg" width="25%">
  </div>

  <div class="modalSlide">
    <div class="nr"> 2 / 4</div>
    <img src="../../portfolio/vector/Owl.svg" width="25%">
  </div>

  <div class="modalSlide">
    <div class="nr"> 3 / 4</div>
    <img src="../../portfolio/vector/Owl.svg" width="25%">
  </div>
<!--End of the modal box-->

<!-- Previous & next buttons-->
  <a class="prev" onclick="toggleSwitch(-1)">❮</a>
  <a class="next" onclick="toggleSwitch(1)">❯</a>
  
  <div class="caption">
    <p id="caption"></p>
  </div>

  <div class="column">
    <img class="ms cursor" src="../../portfolio/vector/Owl.svg" onclick="currentSwitch(1)" alt="Paper Owl">
    </div>
    <div class="column">
      <img class="ms cursor" src="../../portfolio/vector/Owl.svg" onclick="currentSwitch(2)" alt="Triangle Owl">
    </div>
     <div class="column">
      <img class="ms cursor" src="../../portfolio/vector/Owl.svg" onclick="currentSwitch(3)" alt="Circled Owl">
    </div>
     <div class="column">
      <img class="ms cursor" src="../../portfolio/vector/Owl.svg" onclick="currentSwitch(4)" alt="X Owl">
    </div>
  </div>
</div>

</main>
<?php 
 include '../../bibliotek/php/inc/footer.inc.php';
?>