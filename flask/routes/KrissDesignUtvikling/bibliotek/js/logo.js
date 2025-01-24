// This document contains the Javascript used for the Slideshow for logos 
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
    setTimeout(showSlides,2000); // Timer (1000ms) = 1s
}
