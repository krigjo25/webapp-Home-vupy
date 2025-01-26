<?php
/*****************************************************
* Tittel : Funksjoner fra boken Webprogrammering 
* Hensikt :  Vise forskjellige annonser til brukerer på forskellige tidspunk, dager mnd osv..
* Laget : 14.05-17
* Last time Edited : 
* Merk:  // forklaring | 
*******************************************************/
function Advertisement($TodaysDate, $TimerStamp, $Day) { // Deklarering av funksjonen
	// deklarering av Variablene  // date(d) = Dagens dato. date(G) = dette tidspunktet (time) date(D) = Dagens dag.
	$TodaysDate = date("d"); 
	$TimerStamp = date("G") + 2;
	$Day = date("D");
	// Hvis dagen er nr 7 og dagensdato er mindre enn 15 og tiden er mindre eller er lik 12 echo ---
	if ( ($day = 7) && ($TodaysDate <= 15) && ($TimerStamp <= 12) ) {
		echo "<img src='http://www.vg.no/spesial/2017/jensen-rettssaken/img/vg.svg' alt= VGtv>";
	} elseif ( ($day = 7) && ($TodaysDate <= 14) && ($TimerStamp <= 13) ) {
		echo "<img src='https://dshmx1qjgoedw.cloudfront.net/logo-dagbladet.png' alt='Mountain View' style='width:304px;height:228px;) alt= Dagbladet>'";
		} else echo "D'oh Something went wrong a 404.";
}