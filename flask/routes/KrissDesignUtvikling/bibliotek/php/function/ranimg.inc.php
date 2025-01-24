<?php
/*****************************************************
* Tittel : Random Images
* Hensikt :  Sende tilfeldige bilder
* Laget : 15.05-17
* Last time Edited : 
* Merk:  // forklaring | 
*******************************************************/
Ranimg($imagesDir);
function Ranimg($imagesDir) {
$imagesDir = '../../portfoilio/thejulekalender/';
$images = glob($imagesDir . '*.{jpg,jpeg,png,gif}', GLOB_BRACE);
$randomImage = $images[array_rand($images)]; // See comments
}