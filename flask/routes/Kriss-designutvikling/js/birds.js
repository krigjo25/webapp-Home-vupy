// Javascript document of Birds...

function modalOpen() {
	document.getElementById('lightbox').style.display = "block";
}
function modalClose() {
	document.getElementById('lightbox').style.display = "none";
}
var slideIndex = 1;
showSlides(slideIndex);

function  toggleSwitch(n) {
	showSlides(slideIndex += n);
}
function currentSwitch(n) {
	showSlides(slideIndex = n);
}
function showSlides(n) {
	var modalSlide = document.getElementsByClassName('modalSlide');
	var ms = document.getElementsByClassName('ms');
	var caption = document.getElementById("caption");
	if (n > modalSlide.length) {slideIndex = 1}
	if (n < 1) {slideIndex = modalSlide.length}
	for (var i = 0, max = modalSlide.length; i < max; i++) {
		modalSlide[i].style.display = "none";
	} 
 for (var i = 0, max = ms.length; i < max; i++ ) {
 	ms[i].className = ms[i].className.replace (" .active", "");
 }
 modalSlide[slideIndex-1].style.display = "block";
ms[slideIndex-1].className += " .active";
caption.innerHTML = ms[slideIndex-1].alt;
}