<!doctype html>
<html lang="en">
<?php 
// include '\include-files\metadata.inc.html';
// include '\include-files\offline_stylesheet.inc.html';
// include '\include-files\localcssjs\media\media.inc.html';
 include '../html/inc/metadata.inc.html'; 
 include '../html/inc/online_stylesheet.inc.html';
 include '../html/inc/media.inc.html';
 ?>
<!--link href="http://projectmedia.net23.net/pm/css/video.css" rel="stylesheet" type="text/css" media="screen">
<script src="http://projectmedia.net23.net/pm/js/video.js"></script-->
<title>Kriss design - utvikling | Media</title>
</head>
<body>
<?php 
// include '\include-files\header.inc.html';
 include '../html/inc/header.inc.html'; 
?>
<main class="design">
 <div id="media_player">
		<video poster="http://projectmedia.net23.net/pm/portfolio/media/video/our-story/10-15.jpg" preload="metadata" title="Our Story">
			 <source src="http://projectmedia.net23.net/pm/portfolio/media/video/our-story/our-story.mp4" type="video/mp4">
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
// include '\include-files\footer.inc.html';
 include '../html/inc/footer.inc.html'; 

// include 'footer.inc.html';
?>
</body>
</html>
