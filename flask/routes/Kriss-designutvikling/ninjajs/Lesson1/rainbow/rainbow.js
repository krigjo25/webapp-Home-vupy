// JavaScript Document

var rainbowbutton = document.getElementById("rainbow");
var rainbow = ["red", "orange", "yellow", "green", "blue", "indigo","violet"];
function change() {
	document.body.style.background = rainbow[Math.floor(7*Math.random())];
}
rainbowbutton.addEventListener('click', change);