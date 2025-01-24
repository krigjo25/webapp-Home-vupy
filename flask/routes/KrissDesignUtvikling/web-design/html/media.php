<?php 
 include '../../bibliotek/php/inc/metadata.inc.php';
 ?>
 <link rel="stylesheet" type="text/css" href="../../bibliotek/fonts/font-awesome/font/fontawesome-webfont.svg">
 <link href="../css/video.css" rel="stylesheet" type="text/css" media="screen">
<script src="../../bibliotek/php/js/media/video.js"></script>
 <?php
 include '../../bibliotek/php/function/tittel.php';
    Title($Kriss,'Media');
?>
<body>
<?php 
 include '../../bibliotek/php/inc/header.inc.php'; 
?>
<main class="design">
 <div id="media_player">
		<video poster="../../portfolio/media/poster/ourstory/10-15.jpg" preload="metadata" title="Our Story">
			 <source src="../../portfolio/media/OurStory/our-story.mp4" type="video/mp4">
		 	 <source src="./video_file.webm" type="video/webm">
		</video>
		<div id="video_time">
            <progress value="0" id="playback"></progress>
            <span id="elapsed">00:00:00</span><span id="duration">00:00:00</span>
        </div>
        <div id="video_seek"> 
            <input type="range" id="seek" title="seek" value="0" min="0" max="0">
        </div>
        <div id="video_controls">
            <button type="button" id="play" title="Play">
                &#xF04B;
            </button>
			<button type="button" id="pause" title="Pause">
                &#xF04C;
            </button>
			<span>
                <label for="volume" title="Volume">&#xf027;</label>
                <input type="range" id="volume" title="volume" min="0" max="1" step=".1" value="1">	
            </span>
		</div>
	</div>
<div class="des">
<hr class="style-video">
#1. Our Story.<br>
created : 20.05-16.
</div>
</main>
<?php 
 include '../../bibliotek/php/inc/footer.inc.php'; 

// include 'footer.inc.html';
?>
